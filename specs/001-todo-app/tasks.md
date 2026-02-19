# Tasks: Console-Based In-Memory Todo Application

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/service_interface.md, quickstart.md

**Tests**: Tests are OPTIONAL for Phase I - not included per specification (manual validation against acceptance criteria).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow plan.md structure: `src/models/`, `src/services/`, `src/cli/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create src/ directory structure: models/, services/, cli/
- [x] T002 [P] Initialize Python project with pyproject.toml for UV package manager
- [x] T003 [P] Create empty __init__.py files in src/, src/models/, src/services/, src/cli/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Create Task entity in src/models/task.py with id, description, is_completed attributes
- [x] T005 [P] Create TodoService class in src/services/todo_service.py with internal _tasks dict and _next_id counter
- [x] T006 Implement main.py entry point with application bootstrap

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Task List (Priority: P1) 🎯 MVP

**Goal**: Display all tasks with ID, description, and status. Show "No tasks available" when empty.

**Independent Test**: Launch application, select "View Tasks" option, verify task list displays correctly (empty or populated).

### Implementation for User Story 1

- [x] T007 [P] [US1] Implement list_tasks() method in src/services/todo_service.py returning list[Task]
- [x] T008 [US1] Implement CLI view tasks function in src/cli/app.py: display_task_list(tasks: list[Task]) -> None
- [x] T009 [US1] Add "View Tasks" menu option (option 4) in src/cli/app.py main menu loop
- [x] T010 [US1] Handle empty state: display "No tasks available" when list_tasks() returns empty list

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Add Task (Priority: P2)

**Goal**: Allow users to add new tasks with description. Auto-assign sequential IDs starting from 1.

**Independent Test**: Add a task with description, verify it appears in task list with correct ID and "Incomplete" status.

### Implementation for User Story 2

- [x] T011 [P] [US2] Implement add_task(description: str) method in src/services/todo_service.py
- [x] T012 [US2] Add validation in add_task: reject empty/whitespace-only descriptions
- [x] T013 [US2] Implement CLI add task function in src/cli/app.py: prompt_add_task() -> None
- [x] T014 [US2] Add "Add Task" menu option (option 1) in src/cli/app.py main menu loop
- [x] T015 [US2] Display confirmation message: "Task added with ID {id}"

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task as Complete (Priority: P3)

**Goal**: Toggle task completion status by ID. Flip between Complete and Incomplete.

**Independent Test**: Add a task, mark it complete, verify status changes in task list.

### Implementation for User Story 3

- [x] T016 [P] [US3] Implement toggle_complete(task_id: int) method in src/services/todo_service.py
- [x] T017 [US3] Add validation in toggle_complete: return "Task not found" for non-existent ID
- [x] T018 [US3] Implement CLI toggle function in src/cli/app.py: prompt_toggle_complete() -> None
- [x] T019 [US3] Add "Mark Task Complete" menu option (option 5) in src/cli/app.py main menu loop
- [x] T020 [US3] Display status-specific message: "Task marked as complete" or "Task marked as incomplete"

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P4)

**Goal**: Allow users to update task description while preserving completion status.

**Independent Test**: Add a task, update its description, verify description changed but status unchanged.

### Implementation for User Story 4

- [x] T021 [P] [US4] Implement update_task(task_id: int, new_description: str) method in src/services/todo_service.py
- [x] T022 [US4] Add validation in update_task: reject empty descriptions, return "Task not found" for invalid ID
- [x] T023 [US4] Implement CLI update function in src/cli/app.py: prompt_update_task() -> None
- [x] T024 [US4] Add "Update Task" menu option (option 3) in src/cli/app.py main menu loop
- [x] T025 [US4] Preserve is_completed status during update (invariant check)

**Checkpoint**: At this point, User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Remove tasks by ID. Display error for non-existent IDs.

**Independent Test**: Add a task, delete it, verify it no longer appears in task list.

### Implementation for User Story 5

- [x] T026 [P] [US5] Implement delete_task(task_id: int) method in src/services/todo_service.py
- [x] T027 [US5] Add validation in delete_task: return "Task not found" for non-existent ID
- [x] T028 [US5] Implement CLI delete function in src/cli/app.py: prompt_delete_task() -> None
- [x] T029 [US5] Add "Delete Task" menu option (option 2) in src/cli/app.py main menu loop
- [x] T030 [US5] Display confirmation message: "Task deleted successfully"

**Checkpoint**: All 5 user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final validation

- [x] T031 [P] Implement "Exit" menu option (option 6) with clean exit message
- [x] T032 Add input validation in src/cli/app.py: validate_menu_choice(input_str: str) -> int | None
- [x] T033 Add error display handling: display_error(message: str) -> None in src/cli/app.py
- [x] T034 Handle invalid task ID input: display "Invalid task ID. Please enter a number."
- [x] T035 Handle invalid menu selections: re-display menu with "Invalid option. Please try again."
- [x] T036 [P] Add type hints to all public functions across all modules
- [x] T037 [P] Add docstrings to all public functions and classes
- [ ] T038 Run PEP8 compliance check (linting)
- [ ] T039 Remove any unused imports and code
- [ ] T040 Verify no circular dependencies between modules
- [ ] T041 Manual validation: Test all acceptance scenarios from spec.md
- [ ] T042 [P] Update quickstart.md with final implementation details if needed

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order: P1 → P2 → P3 → P4 → P5
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1 - View)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2 - Add)**: Can start after Foundational (Phase 2) - Independent of US1
- **User Story 3 (P3 - Mark Complete)**: Can start after Foundational (Phase 2) - Independent of US1/US2
- **User Story 4 (P4 - Update)**: Can start after Foundational (Phase 2) - Independent of US1/US2/US3
- **User Story 5 (P5 - Delete)**: Can start after Foundational (Phase 2) - Independent of US1/US2/US3/US4

### Within Each User Story

- Models before services (if applicable)
- Service methods before CLI integration
- Core implementation before error handling
- Story complete before moving to next priority

### Parallel Opportunities

- **Phase 1 (Setup)**: T002, T003 can run in parallel
- **Phase 2 (Foundational)**: T004, T005 can run in parallel
- **Phase 3-7 (User Stories)**: All user stories can run in parallel once Phase 2 completes
- **Within User Story 1**: T007 (service method) can run in parallel with T004 (Task model) if not already done
- **Within User Story 2**: T011 (service method) can run in parallel with other service methods
- **Phase 8 (Polish)**: T031, T032, T033, T034, T035, T036, T037, T038, T039, T040, T041, T042 can all run in parallel (different files)

---

## Parallel Example: Foundational Phase

```bash
# Launch T004 and T005 together:
Task: "Create Task entity in src/models/task.py"
Task: "Create TodoService class in src/services/todo_service.py"
```

## Parallel Example: User Story 2

```bash
# Launch T011 (service) in parallel with T004 (model) if model not yet complete:
Task: "Create Task entity in src/models/task.py"
Task: "Implement add_task method in src/services/todo_service.py"
```

## Parallel Example: Polish Phase

```bash
# Launch all polish tasks together:
Task: "Add type hints to all public functions"
Task: "Add docstrings to all public functions and classes"
Task: "Run PEP8 compliance check"
Task: "Remove unused imports and code"
Task: "Verify no circular dependencies"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T006)
3. Complete Phase 3: User Story 1 (T007-T010)
4. **STOP and VALIDATE**: Test View Tasks independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (View) → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 (Add) → Test independently → Deploy/Demo
4. Add User Story 3 (Mark Complete) → Test independently → Deploy/Demo
5. Add User Story 4 (Update) → Test independently → Deploy/Demo
6. Add User Story 5 (Delete) → Test independently → Deploy/Demo
7. Complete Polish phase → Final validation
8. Each story adds value without breaking previous stories

### Sequential Single-Developer Strategy

With one developer, follow priority order:

1. T001 → T006: Setup + Foundational (complete first)
2. T007 → T010: User Story 1 (View) - MVP ready
3. T011 → T015: User Story 2 (Add)
4. T016 → T020: User Story 3 (Mark Complete)
5. T021 → T025: User Story 4 (Update)
6. T026 → T030: User Story 5 (Delete)
7. T031 → T042: Polish & Validation

---

## Task Summary

| Phase | Description | Task Count |
|-------|-------------|------------|
| Phase 1 | Setup | 3 |
| Phase 2 | Foundational | 3 |
| Phase 3 | User Story 1 (View - P1) | 4 |
| Phase 4 | User Story 2 (Add - P2) | 5 |
| Phase 5 | User Story 3 (Mark Complete - P3) | 5 |
| Phase 6 | User Story 4 (Update - P4) | 5 |
| Phase 7 | User Story 5 (Delete - P5) | 5 |
| Phase 8 | Polish & Cross-Cutting | 12 |
| **Total** | | **42** |

---

## Notes

- [P] tasks = different files, no dependencies, can run in parallel
- [Story] label maps task to specific user story for traceability (e.g., [US1], [US2])
- Each user story is independently completable and testable
- Commit after each task or logical group of tasks
- Stop at any checkpoint to validate story independently
- MVP scope: Phases 1-3 (T001-T010) = 10 tasks for View-only functionality
- Full implementation: All 8 phases (T001-T042) = 42 tasks
