## ADDED Requirements

### Requirement: Article List Backed by Real Data
The system SHALL render the article list page from actual `Article` database records, ordered newest first, instead of a hardcoded placeholder list.

#### Scenario: Articles are loaded from the database
- **WHEN** a visitor loads the article list page with no filters applied
- **THEN** the page displays every `Article` record's title, ordered by `created_at` descending

### Requirement: Keyword Search
The system SHALL allow a visitor to filter the article list by a keyword that matches the article's title or content.

#### Scenario: Keyword matches title or content
- **WHEN** a visitor enters a keyword that is a substring of an article's title or content
- **THEN** the article list updates to show only articles whose title or content contains that keyword (case-insensitive)

#### Scenario: No matches
- **WHEN** a visitor enters a keyword that matches no article's title or content
- **THEN** the article list shows a "no results" message instead of an empty list

### Requirement: Author Filter
The system SHALL allow a visitor to filter the article list to articles written by a specific author.

#### Scenario: Filtering by author
- **WHEN** a visitor selects an author from the author filter
- **THEN** the article list updates to show only articles written by that author

### Requirement: Date Filter
The system SHALL allow a visitor to filter the article list to articles created on a specific date.

#### Scenario: Filtering by date
- **WHEN** a visitor selects a date in the date filter
- **THEN** the article list updates to show only articles whose `created_at` date matches the selected date

### Requirement: Combined Filters
The system SHALL apply keyword, author, and date filters together (AND semantics) when more than one is set.

#### Scenario: Keyword and author combined
- **WHEN** a visitor sets both a keyword and an author filter
- **THEN** the article list shows only articles that match the keyword AND were written by the selected author

### Requirement: Dynamic Update Without Page Reload
The system SHALL update the article list in place, without a full page reload, when the visitor types a keyword or changes a filter.

#### Scenario: Typing a keyword updates results without reload
- **WHEN** a visitor types into the keyword field
- **THEN** the article list region updates to reflect the current filters shortly after typing pauses, without the browser performing a full page navigation

#### Scenario: Changing a filter updates results without reload
- **WHEN** a visitor changes the author or date filter
- **THEN** the article list region updates to reflect the new filter value without a full page navigation
