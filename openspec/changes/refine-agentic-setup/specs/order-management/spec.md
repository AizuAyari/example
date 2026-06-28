## ADDED Requirements

### Requirement: Order lifecycle status transitions
The system SHALL enforce valid order status transitions. An order MUST move through statuses in a defined sequence; invalid transitions SHALL be rejected.

Valid transitions:
- `pending` → `confirmed`
- `confirmed` → `processing`
- `processing` → `shipped`
- `shipped` → `delivered`
- Any status → `cancelled` (except `delivered`)

#### Scenario: Valid status transition
- **WHEN** a service function requests a valid status transition for an order
- **THEN** the order status is updated and the change is persisted

#### Scenario: Invalid status transition
- **WHEN** a service function requests an invalid status transition (e.g., `pending` → `shipped`)
- **THEN** the system raises a domain error and the order status remains unchanged

#### Scenario: Cancellation of a delivered order
- **WHEN** a service function attempts to cancel an order in `delivered` status
- **THEN** the system raises a domain error and rejects the cancellation

### Requirement: Business logic in services layer
Order workflow logic SHALL reside in `apps/orders/services.py`. Views and serializers MUST NOT contain order transition logic.

#### Scenario: Order confirmation via service
- **WHEN** `confirm_order(order_id)` is called in `services.py`
- **THEN** the order status changes from `pending` to `confirmed` and any confirmation side-effects (notifications, tasks) are triggered

#### Scenario: Direct status mutation outside services
- **WHEN** a view or serializer directly sets `order.status` without calling a service function
- **THEN** this is considered a violation of project conventions (enforced by code review, not runtime)

### Requirement: Order data integrity
Each order MUST reference a valid customer account. Deleting an account SHALL NOT cascade-delete its orders; instead the account reference SHALL be preserved or nullified per business rules.

#### Scenario: Order created with valid customer
- **WHEN** a new order is created with a valid customer account
- **THEN** the order is persisted with the customer reference

#### Scenario: Order queried after account deletion
- **WHEN** a customer account is deleted
- **THEN** existing orders remain in the database and their customer reference reflects the configured on-delete behavior
