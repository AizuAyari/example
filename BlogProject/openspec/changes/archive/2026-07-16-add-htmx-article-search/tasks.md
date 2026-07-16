## 1. Seed Data

- [x] 1.1 Create `blog/management/commands/seed_articles.py` creating ~5 sample `Article` rows across 2 authors, with varied titles/content/dates, idempotent via `get_or_create(title=...)`
- [x] 1.2 Run `python manage.py seed_articles` locally and verify articles exist in the dev DB

## 2. Backend Filtering

- [x] 2.1 Add `_filter_articles(request)` helper in `blog/views.py` building an `Article.objects` queryset filtered by `q` (title/content `icontains`), `author` (id), and `date` (`created_at__date`) from `request.GET`, combined with AND semantics
- [x] 2.2 Update `article_list(request)` to use `_filter_articles` and pass the queryset plus the author dropdown options to the template
- [x] 2.3 Add `article_search(request)` view that calls `_filter_articles` and renders only the results partial
- [x] 2.4 Add `articles/search/` route to `blog/urls.py` named `article_search`

## 3. Templates

- [x] 3.1 Create `blog/templates/blog/_article_list_results.html` rendering the article `<ul>` or a "no results" message
- [x] 3.2 Update `article_list.html` to add the keyword/author/date filter `<form>` (with `hx-get`, `hx-target="#article-results"`, `hx-swap="innerHTML"`, `hx-trigger="input changed delay:300ms, change"`) and an `#article-results` container that includes `_article_list_results.html`
- [x] 3.3 Add HTMX CDN `<script>` tag to `base.html`

## 4. Verification

- [x] 4.1 Manually test keyword search (match, no-match) in the browser, confirming no full page reload occurs
- [x] 4.2 Manually test author filter and date filter individually and combined with keyword
- [x] 4.3 Write pytest tests for `_filter_articles`/`article_list`/`article_search` covering keyword, author, date, combined, and no-results cases
- [x] 4.4 Run `pytest` to confirm no regressions — 27/27 passed
