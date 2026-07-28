## ADDED Requirements

### Requirement: Keyword Display on Article Detail
The system SHALL display an article's linked keywords on that article's detail page.

#### Scenario: Article with keywords
- **WHEN** a visitor views the detail page of an article that has one or more linked `Keyword` records
- **THEN** the page displays each keyword's text as a tag

#### Scenario: Article with no keywords
- **WHEN** a visitor views the detail page of an article with no linked `Keyword` records
- **THEN** the page displays the article without a keyword tag list (no empty tag markup)
