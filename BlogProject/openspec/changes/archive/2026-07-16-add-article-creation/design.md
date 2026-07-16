## Context

`Article` already has `title`, `content`, `author` (FK to `User`), `created_at`/`updated_at` — no schema change needed. `article_detail` currently just echoes `article_id` without querying the database, so it needs updating in the same change to actually show a newly created article. `settings.py` has no `LOGIN_URL` configured, so Django's default `login_required` decorator would redirect anonymous users to `/accounts/login/`, which doesn't exist in this app (login lives at `/login/`).

## Goals / Non-Goals

**Goals:**
- Authenticated users can submit a title + content and create a real `Article` row, authored as themselves.
- Anonymous visitors are redirected to the existing login page, not a 404 or a Django default login URL.
- The new article is immediately visible at its detail page after creation.

**Non-Goals:**
- Editing or deleting existing articles — out of scope, only creation.
- Rich text / Markdown editing — plain `<textarea>` for content, consistent with the model's plain `TextField`.
- Draft/publish workflow or article visibility permissions — every created article is immediately public, matching current `article_list`/`article_detail` behavior (no draft state on the model).
- Keyword tagging via the `Keyword` model at creation time — deferred; `Keyword` stays unused by this change, same as before.

## Decisions

- **`login_required(login_url="login")` decorator** on `article_create`, rather than adding `LOGIN_URL = "login"` globally to `settings.py`. Rationale: scoping it to the one view that needs it avoids a project-wide settings change for a single call site, and keeps the decision visible right next to the view it affects.
- **`ArticleForm(forms.ModelForm)`** with `fields = ["title", "content"]` — `author` is never form-supplied; the view sets `form.instance.author = request.user` before saving, so a malicious/malformed POST can't set an arbitrary author.
- **Manual field-loop template** (same `{% for field in form %}` + explicit `<label for=...>` pattern as `register.html`/`login.html`), for markup/accessibility consistency with the rest of the site rather than `{{ form.as_p }}`.
- **`article_detail` now queries `get_object_or_404(Article, pk=article_id)`** instead of trusting the raw `article_id` — this is a necessary fix, not scope creep, since without it a newly created article's "detail page" would still just show a placeholder string.

## Risks / Trade-offs

- [Risk] Updating `article_detail` to render real data changes its template/behavior outside this change's "creation form" framing → Mitigation: it's a prerequisite for the create flow to be verifiable end-to-end (redirect target must actually show the article), and it doesn't change any existing passing test (previous tests never asserted on `article_detail` content).
- [Risk] No authorization check beyond "must be logged in" — any authenticated user can post, there's no role/permission distinction → Mitigation: matches the current scope of `user-auth` (a single `User` role, no staff/author distinction exists yet); out of scope to add roles here.
