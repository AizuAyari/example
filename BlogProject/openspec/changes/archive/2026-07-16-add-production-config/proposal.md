## Why

Exercise 11 requires answering the deployment "four questions" (app server, static files, media files, hosting) and hardening `settings.py` for production. Today `settings.py` hardcodes `SECRET_KEY`, has `DEBUG = True`, and `ALLOWED_HOSTS = []` — none of which are safe to deploy as-is, and the current `SECRET_KEY` is already committed to git history so it must be treated as compromised.

## What Changes

- Split settings so `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` are read from environment variables (via `django-environ`), with safe non-debug defaults, instead of being hardcoded.
- Generate a new `SECRET_KEY` (rotating the one that leaked into git history) and remove the old one from the tracked settings file.
- Add `.env` to `.gitignore` and commit an `.env.example` documenting required variables.
- Add WhiteNoise for static file serving in production (`whitenoise.middleware.WhiteNoiseMiddleware` + compressed manifest storage), so no separate static file server/CDN is required.
- Add `gunicorn` as the WSGI application server for production (no ASGI — the app has no async views/websockets).
- Add a `requirements.txt` (pinned via `pip freeze`) and a `Procfile`/`render.yaml` so the app is deployable on Render as-is.
- **BREAKING**: running the app now requires an `.env` file (or equivalent environment variables) locally — `manage.py` commands will fail without `SECRET_KEY` set, since there is no insecure fallback default.

## Capabilities

### New Capabilities
- `production-deployment`: Environment-based configuration, static file serving, and deployment artifacts needed to run the app safely outside local development.

### Modified Capabilities
_None — this changes how settings are sourced and how the app is served, not any existing behavioral requirement from `user-auth`, `interface-design`, or `article-search`._

## Impact

- Affected files: `BlogProject/settings.py` (env-based config), `.gitignore` (repo root), new files: `.env.example`, `requirements.txt`, `Procfile` (or `render.yaml`).
- New dependencies: `django-environ`, `whitenoise`, `gunicorn`.
- Media file handling (`FileField`/`ImageField` storage) is explicitly out of scope — no model currently has file/image fields, so there is nothing to configure yet.
- Local development workflow changes: developers must copy `.env.example` to `.env` and set `SECRET_KEY` before running `manage.py runserver`.
