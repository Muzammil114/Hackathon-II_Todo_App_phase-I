# Implementation Plan: Console-Based In-Memory Todo Application

**Branch**: `001-todo-app` | **Date**: 2026-02-19 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-todo-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a console-based in-memory todo application with 5 CRUD features (Add, Delete, Update, View, Mark Complete). Technical approach follows clean architecture with strict separation: models (data), services (business logic), and CLI (I/O). Uses Python 3.13+ with dictionary-based storage for O(1) task lookup and auto-increment IDs for deterministic behavior.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard library only (no external frameworks)
**Storage**: In-memory dictionary `{id: Task}` - runtime only
**Testing**: Manual validation against acceptance criteria (unit tests optional for Phase I)
**Target Platform**: Cross-platform CLI (Windows, macOS, Linux)
**Project Type**: Single project (CLI application)
**Performance Goals**: Application starts and responds within 2 seconds
**Constraints**: <100MB memory, no persistence, no external APIs
**Scale/Scope**: Single user, session-based (tasks cleared on exit)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Compliance | Notes |
|-----------|------------|-------|
| I. Spec-First Development | ✅ PASS | Specification complete before planning |
| II. Deterministic Behavior | ✅ PASS | Auto-increment IDs, predictable output |
| III. Clean Architecture | ✅ PASS | Three layers: models/, services/, cli/ |
| IV. Simplicity Over Abstraction | ✅ PASS | No patterns beyond basic OOP, standard library only |
| V. Testability | ✅ PASS | Business logic isolated from CLI, type hints, docstrings |

**Gate Result**: All principles pass. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-app/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (service interface contracts)
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Task entity with id, description, is_completed
├── services/
│   └── todo_service.py  # Business logic: add, delete, update, toggle, list
├── cli/
│   └── app.py           # Menu loop, input parsing, output formatting
└── main.py              # Entry point, wires CLI to service
```

**Structure Decision**: Single project structure per constitution standards. Three-layer architecture with clear separation:
- `models/`: Data structures only
- `services/`: Business logic only
- `cli/`: User interaction only
- `main.py`: Application bootstrap

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations. All principles followed with simplest approach.

---

## Phase 0: Research & Technical Decisions

### Decision 1: Storage Structure

**Decision**: Dictionary `{id: Task}`

**Rationale**: 
- O(1) lookup by ID for delete, update, toggle operations
- Natural mapping to task ID as key
- Prevents accidental duplicates

**Alternatives Considered**:
- List of Task objects: Simpler but O(n) lookup for every ID-based operation
- Set: Cannot have duplicate IDs but lacks ordering and ID-based access

### Decision 2: ID Generation

**Decision**: Auto-increment counter starting from 1

**Rationale**:
- Deterministic and predictable (constitution Principle II)
- Simple implementation (counter variable)
- User-friendly sequential IDs

**Alternatives Considered**:
- UUID: Unnecessary complexity for in-memory scope
- Timestamp-based: Not deterministic, harder to test

### Decision 3: Task Mutability

**Decision**: Mutable Task object

**Rationale**:
- Simpler for Phase I scope (constitution Principle IV)
- Direct attribute assignment for updates
- No overhead of object replacement

**Alternatives Considered**:
- Immutable + replace pattern: Cleaner but adds complexity without benefit for in-memory storage

### Decision 4: Error Handling Strategy

**Decision**: Return-based with error messages (no exceptions for business logic)

**Rationale**:
- Simpler flow for CLI application (constitution Principle IV)
- Service methods return tuple `(success: bool, message: str, data: optional)`
- CLI layer handles all error display

**Alternatives Considered**:
- Custom exceptions: Cleaner separation but overengineering for 5 simple operations

### Decision 5: CLI Design

**Decision**: Numbered menu loop

**Rationale**:
- Beginner-friendly and simple (constitution Principle IV)
- Clear options displayed each iteration
- Easy input validation (numeric choice)

**Alternatives Considered**:
- Command-based input: More flexible but unnecessary complexity for MVP

---

## Phase 1: Design & Data Model

### Data Model (data-model.md)

**Entity: Task**

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| id | int | Unique identifier | Auto-generated, sequential, starts at 1 |
| description | str | Task description | Non-empty, non-whitespace |
| is_completed | bool | Completion status | Default: False |

**Entity: TodoService**

| Method | Parameters | Returns | Behavior |
|--------|------------|---------|----------|
| add_task | description: str | (bool, str, optional int) | Creates task, returns (success, message, id) |
| delete_task | task_id: int | (bool, str) | Removes task if exists |
| update_task | task_id: int, new_description: str | (bool, str) | Updates description only |
| toggle_complete | task_id: int | (bool, str) | Toggles is_completed boolean |
| list_tasks | none | list[Task] | Returns all tasks |

### Service Interface Contracts (contracts/service_interface.md)

**Add Task Contract**:
- Input: Non-empty string description
- Output: Success tuple with task ID on success, error message on failure
- Validation: Description must be non-empty and non-whitespace
- Error: "Task description cannot be empty"

**Delete Task Contract**:
- Input: Integer task ID
- Output: Success tuple with confirmation message
- Validation: Task ID must exist in collection
- Error: "Task not found"

**Update Task Contract**:
- Input: Integer task ID, string new_description
- Output: Success tuple with confirmation message
- Validation: Task ID must exist, description non-empty
- Error: "Task not found" or "Task description cannot be empty"
- Invariant: is_completed must remain unchanged

**Toggle Complete Contract**:
- Input: Integer task ID
- Output: Success tuple with new status
- Validation: Task ID must exist
- Error: "Task not found"
- Behavior: Flips is_completed (True ↔ False)

**List Tasks Contract**:
- Input: None
- Output: List of all Task objects
- Behavior: Returns empty list if no tasks
- Display: "No tasks available" for empty list

### Quick Start Guide (quickstart.md)

```markdown
# Quick Start: Todo Application

## Prerequisites
- Python 3.13+
- UV package manager

## Installation
1. Clone repository
2. Run `uv sync` to install dependencies

## Usage
1. Run `uv run python src/main.py`
2. Select from menu:
   - 1: Add Task
   - 2: Delete Task
   - 3: Update Task
   - 4: View Tasks
   - 5: Mark Task Complete
   - 6: Exit

## Example Session
```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Task Complete
6. Exit
Choose option: 1
Enter task description: Buy groceries
Task added with ID 1

Choose option: 4
=== Task List ===
[1] Buy groceries - Incomplete
```

## Troubleshooting
- "Task not found": Ensure ID exists (use View Tasks to check)
- "Invalid task ID": Enter numeric values only
- "Task description cannot be empty": Provide non-empty text
```

---

## Constitution Check (Post-Design)

*Re-evaluation after Phase 1 design complete*

| Principle | Status | Verification |
|-----------|--------|--------------|
| Spec-First | ✅ | All decisions trace to spec requirements |
| Deterministic | ✅ | Auto-increment IDs, predictable menu flow |
| Clean Architecture | ✅ | Strict layer separation in design |
| Simplicity | ✅ | Dictionary storage, mutable objects, no exceptions |
| Testability | ✅ | Service layer independent, type hints planned |

**Gate Result**: All principles maintained. Ready for task breakdown.

## Dependencies & Risks

**Dependencies**:
- Python 3.13+ availability
- UV package manager

**Risks**:
- None identified for Phase I scope (in-memory, no persistence, no external APIs)

## Validation Strategy

**Manual Testing** (per spec acceptance criteria):
1. Execute each user story's acceptance scenarios
2. Verify error messages for all edge cases
3. Confirm deterministic output (same input → same output)
4. Validate architecture separation (no business logic in CLI)

**Code Quality Checks**:
- PEP8 compliance via linter
- Type hints present on all public functions
- Docstrings on all classes and public methods
- No circular imports
- No unused code

---

**Plan Status**: Ready for `/sp.tasks` command
