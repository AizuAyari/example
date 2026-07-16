## Purpose

Presentation-layer requirements for the blog app's templates: semantic HTML structure, a consistent hand-authored CSS stylesheet, responsive layout, and baseline accessibility (universal design) across all pages.

## Requirements

### Requirement: Semantic HTML Structure
The system SHALL render every page using semantic HTML5 landmark elements (`header`, `nav`, `main`, `footer` as applicable) and a logical heading hierarchy, instead of generic `div`/`p`-only markup.

#### Scenario: Landmarks present on every page
- **WHEN** any page (home, article list, article detail, register, login) is rendered
- **THEN** the page includes a `header` containing `nav`, a `main` element wrapping the page's primary content, and exactly one top-level heading (`h1`) describing the page

#### Scenario: Form fields are properly labelled
- **WHEN** the registration or login page is rendered
- **THEN** every form input has an associated `<label for="...">` referencing the input's `id`, so the field's purpose is programmatically determinable

### Requirement: Consistent Visual Styling
The system SHALL apply a single, consistent CSS stylesheet across all pages covering typography, color, spacing, navigation, buttons, and forms.

#### Scenario: Stylesheet loaded on every page
- **WHEN** any page is rendered
- **THEN** the page links the shared stylesheet (`blog/static/blog/css/style.css`) via `base.html`, and navigation, buttons, and form elements share consistent visual treatment across pages

### Requirement: Responsive Layout
The system SHALL render usable, non-overlapping layouts across viewport widths from mobile (~320px) through desktop.

#### Scenario: No horizontal scroll on narrow viewports
- **WHEN** any page is viewed at a 375px-wide viewport
- **THEN** all content fits within the viewport width with no horizontal scrollbar and no overlapping elements

#### Scenario: Content constrained on wide viewports
- **WHEN** any page is viewed at a desktop-width viewport (1280px or wider)
- **THEN** page content is constrained to a readable maximum width rather than stretching edge-to-edge

### Requirement: Accessible Interaction States
The system SHALL provide visible keyboard-focus indicators and sufficient color contrast for interactive elements and body text.

#### Scenario: Focus is visible while tabbing
- **WHEN** a user navigates the page using the Tab key
- **THEN** the currently focused link, button, or form field shows a clearly visible focus outline

#### Scenario: Text meets contrast requirements
- **WHEN** body text or interactive element labels are rendered against their background
- **THEN** the color contrast ratio meets or exceeds WCAG AA (4.5:1 for normal text)
