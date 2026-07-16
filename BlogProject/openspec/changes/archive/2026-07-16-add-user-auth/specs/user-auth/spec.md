## ADDED Requirements

### Requirement: User Registration
The system SHALL allow an anonymous visitor to create an account with a unique username and a password, using Django's built-in `User` model with secure password hashing.

#### Scenario: Successful registration
- **WHEN** an anonymous visitor submits the registration form with a username that does not already exist and a valid password
- **THEN** the system creates a new `User` record with the hashed password and redirects the visitor to a logged-in state

#### Scenario: Duplicate username rejected
- **WHEN** an anonymous visitor submits the registration form with a username that already exists
- **THEN** the system does not create a new account and re-displays the form with a visible error indicating the username is already taken

### Requirement: Login
The system SHALL allow a registered user to start an authenticated session by submitting their username and password.

#### Scenario: Successful login
- **WHEN** a registered user submits the login form with their correct username and password
- **THEN** the system starts an authenticated session for that user and redirects them to the home page

#### Scenario: Invalid credentials rejected
- **WHEN** a visitor submits the login form with a username/password combination that does not match any account
- **THEN** the system does not start a session and re-displays the login form with an error message

### Requirement: Logout
The system SHALL allow an authenticated user to end their session.

#### Scenario: Successful logout
- **WHEN** an authenticated user submits the logout action
- **THEN** the system ends their session and the header reflects the anonymous (logged-out) state

### Requirement: Dynamic Header Based on Auth State
The system SHALL display different header content depending on whether the current visitor is authenticated, on every page.

#### Scenario: Header for anonymous visitor
- **WHEN** an anonymous visitor views any page
- **THEN** the header displays "ログイン" and "新規登録" links

#### Scenario: Header for authenticated user
- **WHEN** an authenticated user views any page
- **THEN** the header displays a welcome message containing their username and a logout control, and does not display the login/register links
