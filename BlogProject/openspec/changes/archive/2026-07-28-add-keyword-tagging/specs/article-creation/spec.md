## ADDED Requirements

### Requirement: Keyword Input on Creation
The system SHALL allow an authenticated user creating an article to optionally enter a comma-separated list of keywords, which are saved as `Keyword` records linked to the new article.

#### Scenario: Keywords saved with the new article
- **WHEN** an authenticated user submits the article creation form with a title, content, and a comma-separated `keywords` value
- **THEN** the system creates the article and a `Keyword` record for each non-blank, distinct keyword in the list, linked to that article

#### Scenario: Blank keywords field creates no keywords
- **WHEN** an authenticated user submits the article creation form with the `keywords` field left empty
- **THEN** the system creates the article with no linked `Keyword` records

#### Scenario: Blank and duplicate entries are ignored
- **WHEN** the submitted `keywords` value contains empty entries (e.g. from extra commas) or the same keyword text repeated
- **THEN** the system creates only one `Keyword` record per distinct, non-blank keyword text
