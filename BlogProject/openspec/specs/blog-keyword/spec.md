## Purpose

`Keyword` tagging model for articles: data model, creation via the article creation form, and display on the article detail page.

## Requirements

### Requirement: Keyword Data Model
The system SHALL provide a `Keyword` model for tagging articles, with `keyword_text` (required) and `article` (foreign key to `Article`, required).

#### Scenario: Adding a keyword to an article
- **WHEN** a `Keyword` record is created with a `keyword_text` for an existing article
- **THEN** the `Keyword` record is saved and linked to that article

#### Scenario: Deleting an article cascades to its keywords
- **WHEN** an `Article` is deleted from the database
- **THEN** all `Keyword` records linked to that article are also deleted

### Requirement: Keyword Admin Display
The `Keyword` model SHALL have a human-readable string representation for the Django Admin.

#### Scenario: Keyword display in admin
- **WHEN** an administrator opens the keyword list in Django Admin
- **THEN** each keyword is identifiable by its keyword text (`__str__()` returns `keyword_text`)

### Requirement: Keyword Display on Article Detail
The system SHALL display an article's linked keywords on that article's detail page.

#### Scenario: Article with keywords
- **WHEN** a visitor views the detail page of an article that has one or more linked `Keyword` records
- **THEN** the page displays each keyword's text as a tag

#### Scenario: Article with no keywords
- **WHEN** a visitor views the detail page of an article with no linked `Keyword` records
- **THEN** the page displays the article without a keyword tag list (no empty tag markup)
