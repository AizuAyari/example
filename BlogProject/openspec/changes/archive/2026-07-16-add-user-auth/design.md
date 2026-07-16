## Context

The Blogs app (`blog` Django app) currently has no templates and no authentication — `blog/views.py` returns raw `HttpResponse` strings, and `blog/urls.py` only exposes `home`, `articles/`, `articles/<id>/`. `Article.author` already references `settings.AUTH_USER_MODEL`, but nothing populates it via a real session. `TEMPLATES['APP_DIRS']` is `True`, so per-app `blog/templates/blog/*.html` will be discovered automatically once created.

## Goals / Non-Goals

**Goals:**
- Let a visitor register an account with a unique username and securely hashed password.
- Let a registered user log in and log out via session-based auth.
- Reflect auth state in a shared header on every page (login/register links vs. welcome message/logout).

**Non-Goals:**
- Article posting/authorization (a separate future change).
- Password reset / email verification flows.
- Social auth or third-party login providers.
- API/DRF authentication (this app is server-rendered only).

## Decisions

- **Use Django's built-in `User` model and auth views/forms** (`UserCreationForm` as the base for registration, `django.contrib.auth.views.LoginView`/`LogoutView` or thin wrappers in `blog/views.py`) instead of a custom user model or hand-rolled password hashing. Rationale: smallest surface area, battle-tested security, and matches the existing `Article.author` FK to `AUTH_USER_MODEL`.
- **Registration form lives in `blog/forms.py` (new file)**, subclassing `UserCreationForm` to control which fields are shown and to surface a clear "username already taken" error (Django's `UserCreationForm` already validates uniqueness via `User.username`'s unique constraint — no custom query needed).
- **Session-based auth, not token-based**, since this is a server-rendered template app with no API client to serve.
- **Single shared base template** (`blog/templates/blog/base.html`) owns the header and uses `{% if user.is_authenticated %}` to switch between "ログイン / 新規登録" and "ようこそ、{{ user.username }} さん / ログアウト". Existing and new pages extend this base so the header toggle is automatic everywhere, not duplicated per-view.
- **Routes added to `blog/urls.py`** (`register/`, `login/`, `logout/`) rather than a new `accounts` app, since the app is still small and this keeps routing centralized.

## Risks / Trade-offs

- [Introducing templates for the first time touches every existing view (`home`, `article_list`, `article_detail`) since they must now extend `base.html` to show the header] → Mitigation: convert those views to minimal templates as part of this change so the header is consistent app-wide; keep their content unchanged otherwise.
- [`UserCreationForm`'s default password validators may reject short/simple passwords, which can confuse manual testing] → Mitigation: keep Django's default `AUTH_PASSWORD_VALIDATORS`; document expected password rules in the registration template.
- [Logout via `LogoutView` defaults to requiring POST in newer Django versions] → Mitigation: implement logout as a POST form (button), not a GET link, to match Django 5+/6 conventions.

## Migration Plan

1. Add `blog/forms.py` with the registration form.
2. Add `register`, `login_view`, `logout_view` to `blog/views.py` and wire them in `blog/urls.py`.
3. Add `blog/templates/blog/base.html` with the dynamic header, plus `register.html` and `login.html`.
4. Convert existing views (`home`, `article_list`, `article_detail`) to render templates extending `base.html`, preserving current content.
5. Manually verify: register a new user, duplicate-username error, login, logout, header state on each page.

No database migration is required (uses Django's built-in `User` model).

## Open Questions

- None — scope is limited to registration, login/logout, and header state as agreed with the user.
