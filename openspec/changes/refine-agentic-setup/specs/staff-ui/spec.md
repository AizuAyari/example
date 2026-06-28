## ADDED Requirements

### Requirement: Server-rendered staff views
The staff-facing UI in `apps/web` SHALL be server-rendered using Django templates. Client-side JavaScript SHALL be limited to progressive enhancement; core workflows MUST function without JS enabled.

#### Scenario: Core workflow without JavaScript
- **WHEN** a staff user accesses an order management page with JavaScript disabled
- **THEN** the page renders correctly and form submissions work via standard HTTP POST

#### Scenario: Enhanced interaction with JavaScript
- **WHEN** a staff user accesses the same page with JavaScript enabled
- **THEN** any JS enhancements activate without breaking the base HTML functionality

### Requirement: Authentication required for all staff views
All views in `apps/web` SHALL require authentication. Unauthenticated requests MUST redirect to the login page.

#### Scenario: Authenticated staff member accesses a view
- **WHEN** a logged-in staff member navigates to a protected staff page
- **THEN** the page renders with the user's data and role-appropriate controls

#### Scenario: Unauthenticated access attempt
- **WHEN** an unauthenticated request is made to any staff view
- **THEN** the system redirects to the login page with the original URL preserved as `next`

### Requirement: Role-gated UI controls
Staff views SHALL hide or disable controls that the current user's role does not permit. Hiding a control does NOT replace server-side permission enforcement — both MUST be applied.

#### Scenario: Admin sees all controls
- **WHEN** a staff user with admin role views an order detail page
- **THEN** all action controls (edit, cancel, confirm) are visible and functional

#### Scenario: Read-only staff sees restricted controls
- **WHEN** a staff user with read-only role views the same page
- **THEN** action controls are hidden or disabled, and any direct POST attempt is rejected server-side
