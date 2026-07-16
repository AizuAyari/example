## 1. Registration

- [x] 1.1 Create `blog/forms.py` with a `RegisterForm` subclassing `UserCreationForm`
- [x] 1.2 Add `register` view in `blog/views.py` (render form, save valid submissions, re-render with errors on duplicate username)
- [x] 1.3 Add `register/` route to `blog/urls.py`
- [x] 1.4 Create `blog/templates/blog/register.html` extending the base template

## 2. Login / Logout

- [x] 2.1 Add `login_view` in `blog/views.py` (or wire `django.contrib.auth.views.LoginView` with a custom template)
- [x] 2.2 Add `logout_view` in `blog/views.py` as a POST-only action
- [x] 2.3 Add `login/` and `logout/` routes to `blog/urls.py`
- [x] 2.4 Create `blog/templates/blog/login.html` extending the base template

## 3. Dynamic Header

- [x] 3.1 Create `blog/templates/blog/base.html` with a header block that checks `user.is_authenticated`
- [x] 3.2 Convert `home`, `article_list`, `article_detail` views to render templates extending `base.html` (preserve existing content)
- [x] 3.3 Verify header shows "ログイン / 新規登録" when logged out and "ようこそ、{{ user.username }} さん / ログアウト" when logged in, on every page

## 4. Verification

- [x] 4.1 Manually test registration with a new username (success) and a duplicate username (error shown)
- [x] 4.2 Manually test login with correct and incorrect credentials
- [x] 4.3 Manually test logout and confirm header reverts to anonymous state
- [x] 4.4 Run `pytest` and fix any regressions
