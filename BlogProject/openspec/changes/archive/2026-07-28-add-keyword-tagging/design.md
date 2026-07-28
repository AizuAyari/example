## Context

`Keyword` (`keyword_text`, FK to `Article`) has existed since Exercise 6-7 but nothing creates or reads it outside of `blog/tests.py` and Django Admin. This is a small, single-app change confined to `blog/forms.py`, `blog/views.py`, and two templates — no new dependency, no migration needed (the model already exists).

## Goals / Non-Goals

**Goals:**
- Let a user attach keywords to an article at creation time.
- Show those keywords on the article detail page.

**Non-Goals:**
- Keyword-based filtering/search (the existing `q` search param stays text-only; wiring it to `Keyword` is a separate, larger change).
- Editing keywords on an existing article.
- Autocomplete, keyword deduplication across articles, or a dedicated `Keyword` admin UI beyond what already exists.

## Decisions

- **Plain `forms.CharField`, not a `ModelForm` field on `Keyword`**: `ArticleForm` stays a `ModelForm` for `Article` (`title`, `content`). Keywords are entered as one comma-separated `CharField` and parsed manually in `article_create()`, since a single `Article` maps to zero-or-many `Keyword` rows — there's no single model field to bind to.
- **Parsing happens in the view, not the model**: `article_create()` splits on `,`, strips whitespace, drops blanks, and dedupes (case-sensitive, matching `Keyword.keyword_text`'s plain `CharField`) before calling `Keyword.objects.create()` per entry. Keeping this in the view (rather than a model method) matches the existing convention — `blog/views.py` already holds all business logic, per `AGENTS.md`.
- **Display via `article.keywords.all()`**: the model already exposes `related_name="keywords"`, so the template needs no new view context — `article_detail()` already passes the full `article` object.

## Risks / Trade-offs

- [Comma-separated free text allows near-duplicate keywords (e.g. "Django" vs "django")] → Accepted for this change; exact-match dedup only. Normalizing case/whitespace further is a future refinement, not blocking this minimal version.
- [No way to remove a keyword once saved] → Acceptable per Non-Goals; editing is out of scope.
