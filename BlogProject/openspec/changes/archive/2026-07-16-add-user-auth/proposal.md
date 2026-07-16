## Why

The Blogs currently has no way to identify who is browsing or posting. Every view is anonymous and article authorship (`Article.author`) cannot be tied to a real login session. Adding registration and login/logout is required before any authenticated capability (e.g. posting articles) can be built.

## What Changes

- Add a user registration view/form that creates accounts via Django's built-in `User` model, rejecting duplicate usernames with a visible error.
- Add login and logout views using Django's built-in authentication views/forms.
- Add a shared header (base template) that dynamically switches between "ログイン / 新規登録" links (anonymous) and "ようこそ、<username> さん / ログアウト" (authenticated).
- Introduce `blog/forms.py` (new) for the registration form.
- Wire new routes into `blog/urls.py` for register/login/logout.
- Add HTML templates (registration form, login form, base layout with the dynamic header) since the app currently has no template directory.

## Capabilities

### New Capabilities
- `user-auth`: User registration, login/logout, and session-aware header display for the blog app.

### Modified Capabilities
(none — no existing specs to modify)

## Impact

- `blog/forms.py` (new): registration form definition.
- `blog/views.py`: add `register`, `login_view`/reuse of Django auth views, `logout_view`.
- `blog/urls.py`: add `register/`, `login/`, `logout/` routes.
- HTML templates (new): base layout with dynamic header, registration page, login page.
- No changes to `blog/models.py` — uses Django's built-in `User` model, no new model required.
