## Purpose

User identity relies on Django's built-in `User` model, and articles are linked to their author with cascading delete behavior.

## Requirements

### Requirement: Built-in User Model
The system SHALL use Django's built-in `django.contrib.auth.models.User` model as the sole source of user identity and authentication data. A custom user model SHALL NOT be introduced.

#### Scenario: Username uniqueness
- **WHEN** a new user is created with a username that is already registered
- **THEN** Django's built-in uniqueness constraint rejects the save at the database level and no duplicate user is created

#### Scenario: Password is stored hashed
- **WHEN** a user sets a password while creating an account
- **THEN** the password is stored hashed using Django's standard hashing algorithm, never in plaintext

### Requirement: Article-Author Association
The `Article` model SHALL reference a `User` as its author. Deleting the author user SHALL cascade-delete that user's articles.

#### Scenario: Deleting a user cascades to their articles
- **WHEN** an author user is deleted from the database
- **THEN** all `Article` records authored by that user are also deleted
