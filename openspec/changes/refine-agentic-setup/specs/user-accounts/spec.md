## ADDED Requirements

### Requirement: Role-based access control
The system SHALL enforce role-based permissions on all protected resources. Each user MUST be assigned at least one role. Permission checks SHALL occur in both web views and API endpoints.

#### Scenario: Authorized access
- **WHEN** a user with the required role accesses a protected resource
- **THEN** the system allows the request to proceed

#### Scenario: Unauthorized access
- **WHEN** a user without the required role accesses a protected resource
- **THEN** the system returns a 403 Forbidden response (API) or redirects to an error page (web)

#### Scenario: Unauthenticated access to protected resource
- **WHEN** an unauthenticated request reaches a protected resource
- **THEN** the system returns a 401 Unauthorized response (API) or redirects to the login page (web)

### Requirement: Permission check consistency
Permission logic SHALL be defined in `apps/accounts` and reused by both `apps/api` and `apps/web`. Duplicate permission checks in views and serializers MUST NOT exist.

#### Scenario: Permission change propagates to both interfaces
- **WHEN** a permission rule is updated in `apps/accounts`
- **THEN** the change is automatically reflected in both API endpoints and web views without additional code changes

### Requirement: User account lifecycle
The system SHALL support creating, deactivating, and querying user accounts. Deactivated accounts MUST NOT be able to authenticate.

#### Scenario: Active user login
- **WHEN** an active user provides valid credentials
- **THEN** the system authenticates the user and starts a session or issues a token

#### Scenario: Deactivated user login attempt
- **WHEN** a deactivated user provides valid credentials
- **THEN** the system rejects authentication and returns an appropriate error
