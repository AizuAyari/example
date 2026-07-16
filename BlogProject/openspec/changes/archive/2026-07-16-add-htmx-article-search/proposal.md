## Why

Exercise 10 requires designing and implementing at least one HTMX-powered dynamic interaction. The article list page is the natural fit: it currently renders three hardcoded placeholder titles instead of real `Article` records, and has no way to search or filter. Adding an HTMX-driven incremental search turns it into a real, data-backed feature while demonstrating a partial-page update pattern (no full-page reload, no hand-written JavaScript).

## What Changes

- Replace the hardcoded `titles` list in `article_list` view with a real `Article.objects` queryset.
- Add search/filter controls above the article list: a keyword text input (matches `title`/`content` substring), an author dropdown, and a date filter.
- Add an HTMX-powered partial-update flow: typing in the keyword field or changing a filter re-fetches and replaces only the article list fragment, via `hx-get`/`hx-trigger` — the surrounding page does not reload.
- Add a new view that returns just the filtered article list fragment (HTML partial), reused by both the initial full-page render and the HTMX partial requests.
- Load HTMX via CDN `<script>` in `base.html`.
- Seed the database with several sample articles (different authors, dates, and content/keywords) via a Django management command, so search/filter has meaningful data to demonstrate against.

## Capabilities

### New Capabilities
- `article-search`: Keyword and filter-based search over articles, with HTMX-driven incremental (partial-page) updates to the results list.

### Modified Capabilities
_None — `interface-design` and `user-auth` requirements are unaffected; this adds new behavior to the article list page without changing existing auth or styling requirements._

## Impact

- Affected files: `blog/views.py` (new/updated `article_list` logic, new partial view), `blog/urls.py` (new route for the partial endpoint), `blog/templates/blog/article_list.html` (search/filter form + HTMX attributes), new partial template (e.g. `blog/templates/blog/_article_list_results.html`), `blog/templates/blog/base.html` (HTMX CDN script tag).
- New file: a Django management command (e.g. `blog/management/commands/seed_articles.py`) to create sample `Article` rows for demo/testing.
- No changes to `blog/models.py` — `Article` already has `title`, `content`, `author`, `created_at`, which cover the required search/filter fields.
- New runtime dependency: HTMX (loaded via CDN, no Python/npm package required).
