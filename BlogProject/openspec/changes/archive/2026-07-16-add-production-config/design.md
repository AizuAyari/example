## Context

`settings.py` currently has a hardcoded `SECRET_KEY` (already pushed to GitHub across multiple prior commits — compromised), `DEBUG = True` unconditionally, `ALLOWED_HOSTS = []`, and no static-file serving story beyond Django's dev-server default (which does not serve static files when `DEBUG = False`). There is no `requirements.txt`, `Procfile`, or WSGI server dependency in the project yet. The target host is Render (decided in the Exercise 11 discussion), a single-process PaaS with an ephemeral filesystem and git-push (or `render.yaml`) deploys.

## Goals / Non-Goals

**Goals:**
- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and the database URL are sourced from environment variables, with no secret committed to git.
- The app runs correctly both locally (`DEBUG=True` via `.env`) and in a production-like mode (`DEBUG=False`) without code changes — only environment variables differ.
- Static files are served correctly with `DEBUG=False` via WhiteNoise, without a separate static file host.
- The app is deployable on Render via `requirements.txt` + `Procfile`/`render.yaml` + `gunicorn`.

**Non-Goals:**
- Media file (`FileField`/`ImageField`) storage — no model has file fields yet; deferred until a feature needs it.
- Migrating off SQLite to PostgreSQL — out of scope for this change (SQLite on Render's ephemeral disk is a known limitation to flag, not solve here, since the project has no production database provisioned yet).
- CI/CD pipeline, automatic deploys on push, or zero-downtime deploy strategy — just the app-level config needed to deploy manually.
- ASGI/async support — the app has no async views or websockets, so WSGI via gunicorn is sufficient.

## Decisions

- **`django-environ` for env var loading** (over `python-decouple` or raw `os.environ`): widely used in Django projects, supports `.env` file parsing and typed casting (`env.bool(...)`, `env.list(...)`) in one call, and integrates cleanly with `environ.Env.read_env()` at the top of `settings.py`. Alternative considered: `python-decouple` — functionally similar, `django-environ` chosen for its `env.db_url()` helper which will matter once/if a real database URL is introduced later.
- **Rotate `SECRET_KEY`, don't just relocate it**: since the current key is in git history (multiple commits), moving it to `.env` without changing its value leaves a compromised key in production. Generate a fresh key with `django.core.management.utils.get_random_secret_key()` and put only the new value in the local (untracked) `.env`; the old value is left in git history as a known-bad artifact (out of scope to scrub history).
- **`DEBUG` defaults to `False`** in `settings.py` (`env.bool("DEBUG", default=False)`) so that forgetting to set the env var fails safe (no debug info leak) rather than failing open. Local development explicitly sets `DEBUG=True` in `.env`.
- **`ALLOWED_HOSTS` from a comma-separated env var** (`env.list("ALLOWED_HOSTS", default=[])`), so the Render domain is configured via Render's dashboard/`render.yaml` environment section, not hardcoded or wildcarded.
- **WhiteNoise over S3/CDN for static files**: the app has a handful of small CSS/static assets — WhiteNoise serves them directly from the gunicorn process with in-memory caching and compression, avoiding the operational overhead of a separate static host for a project this size. `STORAGES["staticfiles"]["BACKEND"]` set to `whitenoise.storage.CompressedManifestStaticFilesStorage`.
- **`gunicorn` + `Procfile`/`render.yaml`**: `web: gunicorn BlogProject.wsgi:application` is the standard, minimal Render Python web service pattern; no ASGI server (uvicorn/daphne) needed since nothing in the app is async.
- **`requirements.txt` via `pip freeze`** rather than adopting `pyproject.toml`/`uv` project-wide: the existing `.venv` was built with plain `pip`, and Render's Python buildpack looks for `requirements.txt` by default — matching the existing toolchain is simpler than introducing a new one as part of this change.

## Risks / Trade-offs

- [Risk] SQLite on Render's ephemeral disk means the database resets on every redeploy — this change does not solve that (a Postgres migration is future work) → Mitigation: documented explicitly in `.env.example`/README-style comments as a known limitation, not silently hidden.
- [Risk] Forgetting to set `SECRET_KEY` in the deploy environment will crash the app on startup (no fallback default) → Mitigation: intentional fail-fast behavior — a running app with a missing/weak secret key is worse than a crashed one; `.env.example` documents the required variable clearly.
- [Risk] Local developers who pull this change will hit an immediate crash running `manage.py` until they create `.env` → Mitigation: this is the explicitly accepted **BREAKING** change noted in the proposal; `.env.example` plus a clear error message (Django's default `ImproperlyConfigured` when `env("SECRET_KEY")` is missing) makes the fix obvious.
- [Risk] WhiteNoise's `CompressedManifestStaticFilesStorage` requires `collectstatic` to be run at build/deploy time, or static URLs will 404 → Mitigation: documented in `render.yaml`/`Procfile` build step (`python manage.py collectstatic --noinput`).

## Migration Plan

1. Add `django-environ`, `whitenoise`, `gunicorn` to the venv and freeze to `requirements.txt`.
2. Update `settings.py` to read `SECRET_KEY`/`DEBUG`/`ALLOWED_HOSTS` from environment, add WhiteNoise middleware + storage config.
3. Create `.env` locally (untracked) with a freshly generated `SECRET_KEY` and `DEBUG=True`; commit `.env.example` with placeholder values and comments.
4. Add `Procfile`/`render.yaml` with the gunicorn start command and `collectstatic` build step.
5. Verify locally: `runserver` still works with `.env`, and a `DEBUG=False` + `collectstatic` smoke test serves static files correctly via WhiteNoise.
6. No rollback beyond reverting the commit — no data migration involved.
