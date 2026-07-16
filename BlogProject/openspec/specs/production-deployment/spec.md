## Purpose

Environment-based configuration, static file serving, and deployment artifacts needed to run the app safely outside local development.

## Requirements

### Requirement: Environment-Based Secret and Debug Configuration
The system SHALL read `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` from environment variables rather than hardcoding them in source control, and SHALL default `DEBUG` to `False` when unset.

#### Scenario: Missing SECRET_KEY fails fast
- **WHEN** the application starts without a `SECRET_KEY` environment variable set
- **THEN** the application raises a configuration error instead of starting with an insecure default

#### Scenario: DEBUG defaults to off
- **WHEN** the application starts without a `DEBUG` environment variable set
- **THEN** the application runs with `DEBUG = False`

#### Scenario: Local development enables DEBUG explicitly
- **WHEN** a developer sets `DEBUG=True` in their local `.env` file
- **THEN** the application runs in debug mode locally

### Requirement: Restricted Allowed Hosts
The system SHALL restrict `ALLOWED_HOSTS` to an explicit, environment-configured list rather than a wildcard.

#### Scenario: Allowed hosts configured via environment
- **WHEN** `ALLOWED_HOSTS` is set to a comma-separated list of domains in the environment
- **THEN** the application only accepts requests with a matching `Host` header

### Requirement: Production Static File Serving
The system SHALL serve static files correctly when `DEBUG = False`, without requiring a separate static file host.

#### Scenario: Static files served with DEBUG off
- **WHEN** `DEBUG = False` and `python manage.py collectstatic` has been run
- **THEN** requests to static asset URLs (e.g. the stylesheet) return the asset content successfully

### Requirement: WSGI Application Server
The system SHALL be servable via a production-grade WSGI application server.

#### Scenario: App starts under gunicorn
- **WHEN** the application is started with `gunicorn BlogProject.wsgi:application`
- **THEN** the application serves HTTP requests successfully

### Requirement: Deployable Dependency and Process Declaration
The system SHALL declare its Python dependencies and process start command in files a PaaS host can use to build and run it.

#### Scenario: Dependencies are pinned
- **WHEN** a deployment platform installs dependencies from `requirements.txt`
- **THEN** all packages required to run the application (including `gunicorn`, `whitenoise`, `django-environ`) are installed

#### Scenario: Process start command is declared
- **WHEN** a deployment platform reads the process declaration file
- **THEN** it finds a `web` process command that starts the application via gunicorn
