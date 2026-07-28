# AGENTS.md

## Project scope

"The Blogs" is a Django blog app: user registration/login, article posting, and incremental article search/filtering powered by HTMX. Deployed to production on Render.com.

The app itself lives under `BlogProject/`:

- `BlogProject/BlogProject/` — project settings (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`)
- `BlogProject/blog/` — the app: models, views, forms, templates, tests
- `BlogProject/openspec/` — per-feature design docs (proposal / design / tasks / specs)

`main.py`, `example.py`, and the root `pyproject.toml` dependencies are leftovers from an unrelated exercise and are not part of this app (see `README.md`).

## Important project conventions

- Business logic lives directly in `blog/views.py` — the app is small enough that a services/selectors split would be over-engineering.
- Templates (`blog/templates/blog/`) and CSS (`blog/static/blog/css/style.css`) are fully separated from Python: no HTML generation in views, no styling logic in templates beyond Django template tags.
- HTMX (vanilla `htmx.org` via CDN, no `django-htmx`) powers incremental search/filtering. `hx-get` requests are served by `article_search()`, which renders only the partial `blog/_article_list_results.html`.
- Forms live in `blog/forms.py` using Django's built-in `ModelForm` / `UserCreationForm` rather than hand-rolled validation.

## Commands

- Run server: `cd BlogProject && python manage.py runserver`
- Run tests: `cd BlogProject && pytest`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Seed demo data: `python manage.py seed_articles` (idempotent, safe to re-run)
- Lint: `ruff check .`

## Things that are easy to break

- `_filter_articles()` in `blog/views.py` is shared by both `article_list` (full page) and `article_search` (HTMX partial) — changes must keep both call sites working.
- `Article.Meta.ordering = ["-created_at"]` is relied on by tests that assert newest-first ordering.
- `settings.py` reads `SECRET_KEY` / `DEBUG` / `ALLOWED_HOSTS` from the environment via `django-environ` — never hardcode secrets back into `settings.py`.

## Change coupling

If you change:

- `Article` / `Keyword` models → also check migrations, `admin.py`, and the sample data in `seed_articles.py`
- `_filter_articles()` → also check both `article_list` and `article_search` views and their templates
- `base.html` nav markup → also check the hamburger-menu JS/CSS in `style.css`

## Constraints

- Do not edit old migrations; create a new one instead.
- Prefer small, targeted changes over broad refactors — this is coursework, graded incrementally per numbered "Exercise".

## Documentation use

- Use `BlogProject/openspec/specs/*` as the canonical source for feature-level design and acceptance criteria (`article-creation`, `article-search`, `interface-design`, `production-deployment`, `user-auth`).
- New feature-sized work should go through the OpenSpec propose → apply → archive workflow (see `.claude/skills/openspec-*`) before merging.
- Keep `README.md`'s run/deployment instructions in sync with the actual Render config (`Procfile`, `render.yaml`, `requirements.txt`).

## Testing expectations

- Add or update tests in `blog/tests.py` for new views, forms, or model behavior.
- Run `pytest` before opening a PR.
