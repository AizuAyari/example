## Why

The `Keyword` model was added in Exercise 6-7 as groundwork for tagging articles, but no feature ever used it — there is no way to attach a keyword to an article or see one. It sits in the schema and in Django Admin with zero user-facing behavior. This change wires it up with the smallest useful feature: enter keywords when creating an article, see them on the article's detail page.

## What Changes

- The article creation form gains an optional "keywords" text input (comma-separated).
- On successful creation, each non-empty comma-separated keyword is saved as a `Keyword` record linked to the new article (duplicates and blank entries are ignored).
- The article detail page displays the article's keywords as a list of tags.
- Keyword-based filtering/search and editing keywords after creation are explicitly out of scope for this change.

## Capabilities

### New Capabilities
(none)

### Modified Capabilities
- `article-creation`: creation form and view now accept and persist an optional comma-separated keywords field.
- `blog-keyword`: adds requirements for how keywords are created (via the article creation form) and displayed (on the article detail page), on top of the existing data-model requirements.

## Impact

- `blog/forms.py`: `ArticleForm` gains a `keywords` field (not a model field — handled manually in the view).
- `blog/views.py`: `article_create` parses the keywords input and creates `Keyword` records after saving the article.
- `blog/templates/blog/article_form.html`: no structural change needed (the new form field renders via the existing `{% for field in form %}` loop).
- `blog/templates/blog/article_detail.html`: adds a keyword tag list.
- `blog/tests.py`: new tests for keyword creation and display.
