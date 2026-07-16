## Why

The `Article` model and article list/search UI exist, but there is no way for a logged-in user to actually write and publish an article through the app — the only articles in the database come from the `seed_articles` management command or the Django admin. A creation form is the missing piece to make this a real, usable blog rather than a read-only demo.

## What Changes

- Add an `ArticleForm` (`ModelForm` for `title`/`content`) in `blog/forms.py`.
- Add an `article_create` view: only accessible to authenticated users (anonymous visitors are redirected to login), sets `author` to `request.user`, and redirects to the new article's detail page on success.
- Add a `blog/templates/blog/article_form.html` template following the same manual field-loop + label pattern used by `register.html`/`login.html`.
- Add an `articles/new/` route.
- Add a "新規投稿" (new post) link in the header/nav, visible only when authenticated (alongside the existing "ようこそ" / logout controls).
- Update `article_detail` to render the real `Article` record (title, content, author, date) instead of just echoing the raw `article_id` — needed so a newly created article is visible after redirect.

## Capabilities

### New Capabilities
- `article-creation`: Authenticated users can create new articles through a web form.

### Modified Capabilities
- `interface-design`: the header/nav requirement gains a new authenticated-only link; still server-rendered, semantic markup, same styling system — no change to existing header requirements' pass/fail behavior, so no delta spec needed there beyond the new nav link, which is covered under `article-creation`'s own requirements instead of touching `interface-design`.

## Impact

- Affected files: `blog/forms.py` (new `ArticleForm`), `blog/views.py` (`article_create`, updated `article_detail`), `blog/urls.py` (new route), `blog/templates/blog/article_form.html` (new), `blog/templates/blog/base.html` (nav link), `blog/templates/blog/article_detail.html` (render real article).
- No model changes — `Article` already has all needed fields.
- Anonymous users attempting to reach `articles/new/` are redirected to `login/` (reusing existing auth from `user-auth`).
