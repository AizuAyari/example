## 1. Form

- [x] 1.1 Add an optional `keywords` `CharField` to `ArticleForm` (not a model field; help text explaining comma-separated input)

## 2. View

- [x] 2.1 In `article_create()`, after saving the article, parse `form.cleaned_data["keywords"]`: split on `,`, strip whitespace, drop blanks, dedupe, and create one `Keyword` per distinct entry linked to the new article

## 3. Templates

- [x] 3.1 Add a keyword tag list to `article_detail.html`, rendered from `article.keywords.all()`, only shown when non-empty

## 4. Tests

- [x] 4.1 Test that submitting comma-separated keywords on creation creates matching `Keyword` records linked to the article
- [x] 4.2 Test that a blank `keywords` field creates no `Keyword` records
- [x] 4.3 Test that blank entries (extra commas) and duplicate keyword text are not saved as separate/empty `Keyword` records
- [x] 4.4 Test that the article detail page displays each linked keyword's text
- [x] 4.5 Test that the article detail page does not render a keyword tag list when the article has no keywords
- [x] 4.6 Run `pytest` and confirm all tests (new and existing) pass
