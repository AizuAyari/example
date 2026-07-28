## Purpose

Core `Article` data model: fields, default ordering, and admin display.

## Requirements

### Requirement: Article Data Model
The system SHALL provide an `Article` model with the following fields: `title` (string, required), `content` (text, required), `author` (foreign key to `User`, `on_delete=CASCADE`, required), `created_at` (auto-set on creation, not editable), and `updated_at` (auto-updated on every save).

#### Scenario: created_at is set automatically on creation
- **WHEN** an authenticated user creates a new article
- **THEN** `created_at` is automatically set to the current timestamp

#### Scenario: updated_at changes on update, created_at does not
- **WHEN** an existing article's `title` or `content` is updated and saved
- **THEN** `updated_at` is set to the current timestamp while `created_at` remains unchanged

#### Scenario: Article requires an author
- **WHEN** an `Article` is saved without an `author`
- **THEN** the database constraint rejects the save and no article is created

### Requirement: Default Article Ordering
The article list SHALL be ordered newest-first by default.

#### Scenario: Default queryset ordering
- **WHEN** `Article.objects.all()` is queried without an explicit `order_by()`
- **THEN** results are returned in descending `created_at` order (most recent first)

### Requirement: Article Admin Display
The `Article` model SHALL have a human-readable string representation for the Django Admin.

#### Scenario: Article display in admin
- **WHEN** an administrator opens the article list in Django Admin
- **THEN** each article is identifiable by its title (`__str__()` returns the title)
