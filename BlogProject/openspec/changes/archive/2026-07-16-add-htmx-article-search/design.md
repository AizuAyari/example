## Context

`article_list` (`blog/views.py`) currently renders three hardcoded Japanese strings — it never touches the `Article` model. The `Article` model already has `title`, `content`, `author` (FK to `User`), and `created_at`, which cover keyword, author, and date filtering with no schema change needed. The project has no JS build tooling; HTMX (loaded via CDN per project decision) is a good fit because it adds dynamic partial-page updates via HTML attributes, not hand-written JS.

## Goals / Non-Goals

**Goals:**
- Real, DB-backed article list with keyword (title/content substring), author, and date filtering.
- Filtering updates only the results region via HTMX, without a full page reload.
- One shared filtering function so the initial page load and the HTMX partial endpoint can't drift out of sync.
- Seed data so the feature is demonstrable out of the box.

**Non-Goals:**
- Pagination, sorting controls, or full-text search (e.g. Postgres FTS) — plain `icontains` substring matching is sufficient for this exercise.
- Tag/`Keyword`-model-based search — explicitly deferred; keyword search matches `title`/`content` only.
- Article creation/editing UI — out of scope; seeding is done via a management command, not a form.
- Race-condition-proof request ordering (see Risks) — acceptable for this exercise's scale.

## Decisions

- **Shared filter function, two views**: a module-level `_filter_articles(request)` in `blog/views.py` builds the `Article.objects` queryset from `request.GET` (`q`, `author`, `date`) using Django ORM `Q` objects. `article_list(request)` (full page, `GET /articles/`) and a new `article_search(request)` (partial, `GET /articles/search/`) both call it — the only difference is which template they render. Rationale: keeps filtering logic in one place; the alternative (duplicating filter logic per view) risks the two endpoints silently diverging.
- **Partial template reuse via `{% include %}`**: `blog/templates/blog/_article_list_results.html` renders just the `<ul class="article-list">` (or "no results" message). `article_list.html` includes it for the initial render; `article_search` renders it directly (no `base.html` extension) for HTMX swaps. Rationale: standard Django/HTMX pattern — one fragment template, no duplicated markup.
- **HTMX wiring on the filter `<form>`, not each input**: the form carries `hx-get="{% url 'article_search' %}" hx-target="#article-results" hx-swap="innerHTML" hx-trigger="input changed delay:300ms, change"`. HTMX serializes all form fields on every trigger. Rationale: simpler than wiring `hx-get`/`hx-include` per-field, and naturally covers keyword (debounced keyup via `input`), author `<select>`, and date `<input type="date">` with one declaration.
- **GET, not POST, for the search endpoint**: filtering is idempotent/read-only, so `GET` is correct REST semantics and needs no CSRF token, matching HTMX's simplest usage pattern.
- **Author filter as a `<select>`** populated from `User.objects.filter(articles__isnull=False).distinct().order_by("username")` — only shows authors who actually have articles, keeping the dropdown relevant.
- **Date filter matches `created_at__date`** against a single `<input type="date">` value (exact day match) — simplest interpretation of "date filter" without adding a date-range UI.
- **Seed command** (`blog/management/commands/seed_articles.py`) creates ~5 sample articles across 2 authors with varied `title`/`content` (so keyword search has real matches) and is idempotent via `get_or_create(title=...)` so re-running it doesn't create duplicates.

## Risks / Trade-offs

- [Risk] Fast typing can fire overlapping requests where an older (slower) response resolves after a newer one, briefly showing stale results → Mitigation: `delay:300ms` on the `input` trigger debounces most keystrokes; full request-ordering guarantees (`hx-sync`) are out of scope for this exercise's scale.
- [Risk] The `article_search` partial endpoint returns a bare HTML fragment (no `<html>`/`base.html`) and is reachable directly by URL, which would look broken if visited as a page → Mitigation: intentional HTMX fragment-endpoint pattern; acceptable since it's an internal endpoint not linked from navigation.
- [Risk] CDN-hosted HTMX means the search UI silently degrades (JS behavior missing, but the plain `<form>` still GET-submits and full-page-reloads to the same results) if the CDN is unreachable → Mitigation: accepted per project decision; the `<form>`'s native `action`/`method` fallback still works without HTMX/JS.
- [Risk] Substring (`icontains`) search on `content` over many/long articles could get slow at scale → Mitigation: acceptable for this exercise's small dataset; not a concern with ~5 seed articles.

## Migration Plan

Additive only: new view, new URL, new templates, new management command. No changes to existing models/migrations. Run `python manage.py seed_articles` once locally (idempotent, safe to re-run) to populate demo data.
