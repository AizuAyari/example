## ADDED Requirements

### Requirement: Article Creation Form
The system SHALL allow an authenticated user to create a new `Article` by submitting a title and content through a web form.

#### Scenario: Successful creation
- **WHEN** an authenticated user submits the article creation form with a non-empty title and content
- **THEN** the system creates a new `Article` record authored by that user and redirects to the new article's detail page

#### Scenario: Missing required field
- **WHEN** an authenticated user submits the article creation form with an empty title or content
- **THEN** the system does not create an article and re-displays the form with a visible validation error

### Requirement: Creation Requires Authentication
The system SHALL require a visitor to be logged in to access the article creation form.

#### Scenario: Anonymous visitor redirected to login
- **WHEN** an anonymous visitor requests the article creation page
- **THEN** the system redirects them to the login page instead of showing the form

### Requirement: Author Is Always the Submitting User
The system SHALL always set the created article's author to the currently authenticated user, regardless of form input.

#### Scenario: Author cannot be spoofed via form data
- **WHEN** an authenticated user submits the creation form
- **THEN** the created article's author is the logged-in user, not any value supplied in the request

### Requirement: New Post Link for Authenticated Users
The system SHALL display a link to the article creation page in the site navigation, visible only to authenticated users.

#### Scenario: Link visible when logged in
- **WHEN** an authenticated user views any page
- **THEN** the navigation includes a link to the article creation page

#### Scenario: Link hidden when logged out
- **WHEN** an anonymous visitor views any page
- **THEN** the navigation does not include a link to the article creation page

### Requirement: Article Detail Shows Real Article Data
The system SHALL render the article detail page from the actual `Article` database record matching the requested ID.

#### Scenario: Existing article is displayed
- **WHEN** a visitor requests the detail page for an existing article's ID
- **THEN** the page displays that article's title, content, author, and creation date

#### Scenario: Nonexistent article returns 404
- **WHEN** a visitor requests the detail page for an ID that does not match any article
- **THEN** the system returns a 404 response
