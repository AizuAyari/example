## 1. Dependencies

- [x] 1.1 Install `django-environ`, `whitenoise`, `gunicorn` into the venv
- [x] 1.2 Generate `requirements.txt` via `pip freeze`

## 2. Settings Hardening

- [x] 2.1 Add `environ.Env` setup at the top of `settings.py` and call `env.read_env()` pointing at the project's `.env`
- [x] 2.2 Replace hardcoded `SECRET_KEY` with `env("SECRET_KEY")` (no insecure fallback)
- [x] 2.3 Replace `DEBUG = True` with `env.bool("DEBUG", default=False)`
- [x] 2.4 Replace `ALLOWED_HOSTS = []` with `env.list("ALLOWED_HOSTS", default=[])`
- [x] 2.5 Add `whitenoise.middleware.WhiteNoiseMiddleware` to `MIDDLEWARE` immediately after `SecurityMiddleware`
- [x] 2.6 Add `STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"` and `STATIC_ROOT`

## 3. Secrets and Local Env

- [x] 3.1 Generate a fresh `SECRET_KEY` via `django.core.management.utils.get_random_secret_key()`
- [x] 3.2 Create local `.env` (untracked) with the new `SECRET_KEY` and `DEBUG=True`
- [x] 3.3 Add `.env` to the repo-root `.gitignore`
- [x] 3.4 Create `.env.example` documenting `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` with placeholder/comment values

## 4. Deployment Artifacts

- [x] 4.1 Create `Procfile` with `web: gunicorn BlogProject.wsgi:application` and a `release`/build step running `collectstatic` and `migrate`
- [x] 4.2 Create `render.yaml` describing the web service, build command (`pip install -r requirements.txt && python manage.py collectstatic --noinput`), and start command

## 5. Verification

- [x] 5.1 Run `manage.py runserver` locally with `.env` present, confirm the app still works (register/login/article search) — `manage.py check` clean, `/articles/` and static CSS both 200
- [x] 5.2 Temporarily set `DEBUG=False` locally, run `collectstatic`, and confirm the stylesheet still loads (WhiteNoise serving works) — verified on a second instance (port 8001), both page and CSS returned 200
- [x] 5.3 Confirm `manage.py runserver` fails with a clear error when `.env`/`SECRET_KEY` is absent (fail-fast behavior) — observed `ImproperlyConfigured: Set the SECRET_KEY environment variable` before `.env` was created
- [x] 5.4 Run `pytest` to confirm no regressions — 27/27 passed
