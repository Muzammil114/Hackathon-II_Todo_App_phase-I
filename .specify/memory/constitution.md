<!--
SYNC IMPACT REPORT
==================
Version change: 0.0.0 → 1.0.0 (MAJOR - initial constitution)
Modified principles: N/A (initial creation)
Added sections:
  - Core Principles (5 principles)
  - Key Standards
  - Architecture Standards
  - Development Workflow
  - Governance
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ aligned (Constitution Check section present)
  - .specify/templates/spec-template.md ✅ aligned (requirements structure compatible)
  - .specify/templates/tasks-template.md ✅ aligned (phase-based structure compatible)
Follow-up TODOs: None
-->

# Phase I – Console-Based In-Memory Todo Application Constitution

## Core Principles

### I. Spec-First Development
Every feature MUST have a written specification before implementation begins.
No code is written without an approved spec document.
This ensures clarity, reduces rework, and enables spec-driven development workflow.
Rationale: Prevents ambiguous requirements and ensures all stakeholders align on behavior before coding.

### II. Deterministic Behavior
All application behavior MUST be predictable and explicit.
No hidden logic, no implicit side effects, no autonomous AI agents.
Every function produces the same output given the same input.
Rationale: Enables reliable testing, debugging, and user trust in the system.

### III. Clean Architecture
The codebase MUST enforce separation of concerns across three layers:
- CLI layer: handles input/output only
- Service layer: contains all business logic
- Models layer: defines data entities only
No business logic inside CLI layer. No circular dependencies between layers.
Rationale: Enables independent testing, maintainability, and clear responsibility boundaries.

### IV. Simplicity Over Abstraction
Avoid unnecessary patterns, overengineering, or premature abstraction.
Start with the simplest solution that works. Apply YAGNI (You Ain't Gonna Need It).
No repositories, factories, or complex patterns unless explicitly required by spec.
Rationale: Reduces cognitive load, accelerates development, and maintains readability.

### V. Testability
Business logic MUST be testable independently from CLI input/output.
All public functions and classes require explicit type hints and docstrings.
Single Responsibility Principle (SRP) enforced per module and class.
Rationale: Enables isolated unit testing and ensures code quality through verification.

## Key Standards

**Technology Stack**:
- Python 3.13+ required
- Dependency management via UV
- In-memory storage only (no files, no databases, no persistence)
- No external APIs, no frameworks beyond standard library

**Code Quality**:
- PEP8 compliance mandatory
- Explicit type hints on all functions
- Docstrings required for all public functions and classes
- Clear error handling with no silent failures

**Feature Scope**:
Exactly 5 core features to implement:
1. Add Task
2. Delete Task
3. Update Task
4. View Task List
5. Mark as Complete

**Development Workflow**:
- Follow spec → plan → tasks → implement workflow
- No manual coding during implementation phase
- All features must map directly to written functional requirements
- Deterministic task ID management

## Architecture Standards

**Directory Structure**:
```
src/
├── models/      # Task entity only
├── services/    # Todo service logic (business rules)
├── cli/         # Input/output handling only
└── main.py      # Entry point
```

**Module Responsibilities**:
- `models/`: Contains only the Task entity definition with attributes
- `services/`: Contains all business logic for task operations
- `cli/`: Handles user input parsing and output formatting only
- `main.py`: Application entry point, wires dependencies

**Constraints**:
- Storage exists only during runtime (memory-based list/dict)
- CLI-based interaction only
- No circular dependencies between modules
- No unused code in final implementation

## Development Workflow

**Phase 1 - Specification**:
- Write complete feature specification with user stories
- Define acceptance criteria for each story
- Document edge cases and error handling

**Phase 2 - Planning**:
- Create implementation plan aligned with constitution
- Define technical approach and project structure
- Perform constitution check before proceeding

**Phase 3 - Task Breakdown**:
- Break implementation into testable tasks
- Organize tasks by user story priority
- Identify parallel execution opportunities

**Phase 4 - Implementation**:
- Follow tasks in priority order
- Maintain separation of concerns
- Verify constitution compliance throughout

**Success Criteria**:
- All 5 features implemented exactly as defined in spec
- Clear separation between UI and business logic
- No circular dependencies
- No unused code
- Application runs without runtime errors
- All user actions produce deterministic and predictable output
- Codebase readable and maintainable
- Fully aligned with written specification

## Governance

**Amendment Procedure**:
Constitution amendments require:
1. Proposed change documented with rationale
2. Version bump according to semantic versioning
3. Sync impact report generated
4. Dependent templates updated if needed

**Versioning Policy**:
- MAJOR: Backward incompatible principle removals or redefinitions
- MINOR: New principle/section added or materially expanded guidance
- PATCH: Clarifications, wording improvements, typo fixes

**Compliance Review**:
- All PRs must verify constitution compliance
- Constitution Check performed during planning phase
- Complexity must be justified if violating simplicity principle
- Use checklist-template.md for runtime development guidance

**Version**: 1.0.0 | **Ratified**: 2026-02-19 | **Last Amended**: 2026-02-19
