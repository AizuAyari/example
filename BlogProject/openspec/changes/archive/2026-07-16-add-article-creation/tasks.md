## 1. Form and View

- [x] 1.1 Add `ArticleForm(forms.ModelForm)` in `blog/forms.py` with `fields = ["title", "content"]`
- [x] 1.2 Add `article_create` view in `blog/views.py`, decorated with `@login_required(login_url="login")`, setting `form.instance.author = request.user` before save, redirecting to `article_detail` on success
- [x] 1.3 Update `article_detail` view to use `get_object_or_404(Article, pk=article_id)` and pass the real article to the template
- [x] 1.4 Add `articles/new/` route to `blog/urls.py` named `article_create`

## 2. Templates

- [x] 2.1 Create `blog/templates/blog/article_form.html` using the manual field-loop pattern (label/id association, field errors) consistent with `register.html`/`login.html`
- [x] 2.2 Update `article_detail.html` to render the real article's title, content, author, and created date
- [x] 2.3 Add a "新規投稿" nav link to `base.html`, shown only when `user.is_authenticated`

## 3. Verification

- [x] 3.1 Manually test: log in, create an article, confirm redirect to its detail page shows the new content
- [x] 3.2 Manually test: log out, confirm `articles/new/` redirects to login (`?next=` preserved)
- [x] 3.3 Manually test: submit the form with an empty title, confirm validation error is shown and no article is created — covered by pytest (`test_empty_title_shows_validation_error_and_creates_nothing`)
- [x] 3.4 Write pytest tests covering successful creation, author assignment, login-required redirect, validation error, and article_detail 404/real-data rendering
- [x] 3.5 Run `pytest` to confirm no regressions — 33/33 passed
