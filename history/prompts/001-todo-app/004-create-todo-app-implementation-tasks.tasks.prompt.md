---
id: 004
title: Create Todo App Implementation Tasks
stage: tasks
date: 2026-02-19
surface: agent
model: qwen-3.5
feature: 001-todo-app
branch: 001-todo-app
user: sonny
command: /sp.tasks
labels: ["tasks", "implementation", "todo-app", "breakdown"]
links:
  spec: specs/001-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-todo-app/tasks.md
tests:
  - N/A (task breakdown document creation)
---

## Prompt

/sp.tasks

Create:
- Architecture sketch
- Module structure
- Development phases
- Decision log (with tradeoffs)
- Validation and testing strategy
- Requirement traceability mapping

Development approach:
- Spec-driven development (no implementation before approved specification)
- Plan-first modular breakdown
- Iterative validation after each feature
- Deterministic feature-by-feature completion
- Clean architecture enforcement at every phase

Organize by phases:

Phase 1: Foundation
- Define project directory structure
- Define Task entity model
- Define in-memory storage strategy
- Define ID generation mechanism
- Define CLI interaction flow
- Establish error handling conventions

Phase 2: Core Service Layer
- Implement TodoService class
- Add task logic
- Delete task logic
- Update task logic
- Mark complete logic
- Retrieval logic
- Ensure business logic independent of CLI

Phase 3: CLI Layer
- Menu design
- Input validation
- Output formatting
- Error display handling
- Mapping user commands to service layer

Phase 4: Integration
- Connect CLI to service layer
- Validate deterministic behavior
- Confirm separation of concerns
- Remove redundant code
- Final review against specification

Architecture Sketch:

Project Structure:
- models/
    - task.py
- services/
    - todo_service.py
- cli/
    - app.py
- main.py

Layer Responsibilities:
- models → Data structure definition only
- services → Business logic only
- cli → User interaction only
- main.py → Application entry point

No cross-layer logic leakage allowed.

Decisions Needing Documentation:

1. Storage Structure
   Option A: List of Task objects
   Option B: Dictionary {id: Task}
   Tradeoff:
   - List simpler but slower lookup
   - Dictionary enables O(1) lookup by ID
   Decision must be documented with justification

2. ID Generation
   Option A: Auto-increment counter
   Option B: UUID
   Tradeoff:
   - Auto-increment simpler and deterministic
   - UUID unnecessary complexity for in-memory scope

3. Task Mutability
   Option A: Mutable Task object
   Option B: Immutable + replace pattern
   Tradeoff:
   - Mutable simpler for Phase I
   - Immutable cleaner but adds overhead

4. Error Handling Strategy
   Option A: Return None + error message
   Option B: Raise custom exceptions
   Tradeoff:
   - Exceptions cleaner separation
   - Return-based approach simpler for CLI app

5. CLI Design
   Option A: Numbered menu loop
   Option B: Command-based input
   Tradeoff:
   - Menu simpler and beginner-friendly
   - Command-based more flexible but unnecessary for MVP

Testing Strategy:

Validation checks based on acceptance criteria:

For Add Task:
- Adding valid description creates new task
- Empty description rejected
- ID increments correctly

For Delete Task:
- Valid ID removes task
- Invalid ID triggers clear error
- No side effects on other tasks

For Update Task:
- Valid ID updates description only
- Status remains unchanged
- Invalid ID handled correctly

For Mark Complete:
- Toggles status correctly
- Multiple toggles behave predictably
- Invalid ID handled correctly

For View Task List:
- Displays all tasks with ID, description, status
- Empty state handled properly

Architecture Validation:
- CLI contains no business logic
- Service layer contains no input/output calls
- Model contains no logic unrelated to task state

Code Quality Validation:
- PEP8 compliance
- Type hints everywhere
- Docstrings present
- No unused imports
- No circular dependencies

Definition of Done:
- All 5 features implemented
- Each requirement traceable to specification
- All validation checks pass manually
- Clean project structure maintained
- Deterministic and reproducible behavior

## Response snapshot

Created tasks.md at `specs/001-todo-app/tasks.md` with 42 tasks organized into 8 phases:
- Phase 1: Setup (3 tasks) - project structure, Python/UV initialization
- Phase 2: Foundational (3 tasks) - Task entity, TodoService class, main.py entry point
- Phase 3: User Story 1 - View Task List (4 tasks) - list_tasks(), CLI display, menu option 4
- Phase 4: User Story 2 - Add Task (5 tasks) - add_task(), validation, CLI prompt, menu option 1
- Phase 5: User Story 3 - Mark Complete (5 tasks) - toggle_complete(), CLI, menu option 5
- Phase 6: User Story 4 - Update Task (5 tasks) - update_task(), validation, CLI, menu option 3
- Phase 7: User Story 5 - Delete Task (5 tasks) - delete_task(), validation, CLI, menu option 2
- Phase 8: Polish & Cross-Cutting (12 tasks) - Exit, input validation, error handling, type hints, docstrings, PEP8, validation

Task format follows template strictly:
- Checkbox: - [ ]
- Task ID: T001-T042
- [P] marker for parallelizable tasks
- [Story] label for user story phases (US1-US5)
- Exact file paths in descriptions

Parallel opportunities identified:
- Phase 1: T002, T003 can run in parallel
- Phase 2: T004, T005 can run in parallel
- Phases 3-7: All user stories can run in parallel after Phase 2
- Phase 8: All 12 polish tasks can run in parallel

MVP scope: Phases 1-3 (T001-T010) = 10 tasks for View-only functionality

## Outcome

- ✅ Impact: Complete task breakdown with 42 tasks across 8 phases, organized by user story priority
- 🧪 Tests: N/A (task document, tests optional per spec - manual validation approach)
- 📁 Files: Created specs/001-todo-app/tasks.md (1 file)
- 🔁 Next prompts: Run `/sp.implement` to start implementing tasks in priority order
- 🧠 Reflection: Tasks follow strict format with IDs, parallel markers, story labels, and exact file paths. Each task is specific enough for immediate execution without additional context.

## Evaluation notes (flywheel)

- Failure modes observed: None - all tasks follow required format
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment: N/A
