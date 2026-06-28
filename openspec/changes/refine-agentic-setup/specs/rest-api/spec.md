## ADDED Requirements

### Requirement: Stable response shapes
API response shapes in `apps/api` SHALL remain stable across changes. Fields MUST NOT be renamed or removed without an explicit API versioning decision. Agents MUST NOT rename API fields unless explicitly instructed.

#### Scenario: Existing field preserved after change
- **WHEN** a serializer is modified to add a new field
- **THEN** all existing fields remain present with the same names and types in the response

#### Scenario: Field removal without versioning
- **WHEN** a developer attempts to remove a response field without a version increment
- **THEN** this is flagged as a breaking change in code review

### Requirement: DRF serializers for all API I/O
All input validation and output serialization in `apps/api` SHALL use Django REST Framework serializers. Raw `request.data` access for validation MUST NOT occur in views.

#### Scenario: Valid input via serializer
- **WHEN** a valid request payload is received
- **THEN** the serializer validates it and passes clean data to the service layer

#### Scenario: Invalid input via serializer
- **WHEN** an invalid request payload is received
- **THEN** the serializer returns a 400 Bad Request response with field-level error details

### Requirement: URL naming stability
URL names in `apps/api` SHALL remain stable. `reverse()` calls and `url_name` references MUST NOT break across changes unless a rename is explicitly requested.

#### Scenario: URL resolution by name
- **WHEN** application code calls `reverse('<url-name>')`
- **THEN** the correct endpoint URL is returned without errors

### Requirement: Authentication on protected endpoints
All non-public API endpoints SHALL require authentication. DRF permission classes MUST be set at the view or viewset level; default-allow MUST NOT be used for protected resources.

#### Scenario: Authenticated request to protected endpoint
- **WHEN** a request with valid authentication credentials reaches a protected endpoint
- **THEN** the system processes the request

#### Scenario: Unauthenticated request to protected endpoint
- **WHEN** a request without credentials reaches a protected endpoint
- **THEN** the system returns 401 Unauthorized
