# Service Interface Contracts

**Feature**: 001-todo-app
**Created**: 2026-02-19
**Status**: Approved

## Overview

This document defines the interface contracts for the TodoService layer. All contracts follow a consistent return pattern for error handling.

## Return Type Convention

All service methods return tuples for consistent error handling:

```python
# Success case
(success: bool = True, message: str, data: Any)

# Failure case
(success: bool = False, message: str, data: None)
```

**Rationale**: Return-based error handling (no exceptions) per Phase 0 Decision 4.

---

## Contract 1: Add Task

**Method**: `add_task(description: str) -> tuple[bool, str, int | None]`

### Inputs
| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| description | str | Yes | Non-empty, non-whitespace |

### Outputs
| Position | Type | Description |
|----------|------|-------------|
| 0 | bool | Success flag |
| 1 | str | Human-readable message |
| 2 | int \| None | Task ID on success, None on failure |

### Behavior
1. Validate description is non-empty and non-whitespace
2. Create new Task with auto-increment ID starting from 1
3. Set is_completed to False (default)
4. Store task in internal dictionary
5. Increment next_id counter
6. Return success tuple with task ID

### Success Response
```python
(True, "Task added with ID 1", 1)
```

### Failure Response
```python
(False, "Task description cannot be empty", None)
```

### Edge Cases
| Input | Behavior |
|-------|----------|
| `""` (empty string) | Return failure |
| `"   "` (whitespace only) | Return failure |
| `"Buy milk"` (valid) | Create task, return success |
| `"Buy 2% milk"` (special chars) | Create task, accept all printable chars |

---

## Contract 2: Delete Task

**Method**: `delete_task(task_id: int) -> tuple[bool, str]`

### Inputs
| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| task_id | int | Yes | Must be positive integer (>= 1) |

### Outputs
| Position | Type | Description |
|----------|------|-------------|
| 0 | bool | Success flag |
| 1 | str | Human-readable message |

### Behavior
1. Check if task_id exists in internal dictionary
2. If exists: remove task, return success
3. If not exists: return failure (no modification)

### Success Response
```python
(True, "Task deleted successfully")
```

### Failure Response
```python
(False, "Task not found")
```

### Edge Cases
| Input | Behavior |
|-------|----------|
| `1` (existing ID) | Delete task, return success |
| `999` (non-existent ID) | Return failure, no side effects |
| `-1` (negative ID) | Return failure (no negative IDs exist) |
| `0` (zero ID) | Return failure (IDs start at 1) |

---

## Contract 3: Update Task

**Method**: `update_task(task_id: int, new_description: str) -> tuple[bool, str]`

### Inputs
| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| task_id | int | Yes | Must exist in collection |
| new_description | str | Yes | Non-empty, non-whitespace |

### Outputs
| Position | Type | Description |
|----------|------|-------------|
| 0 | bool | Success flag |
| 1 | str | Human-readable message |

### Behavior
1. Check if task_id exists in internal dictionary
2. If not exists: return failure immediately
3. If exists: validate new_description
4. Update task.description (preserve is_completed)
5. Return success

### Invariants
- **CRITICAL**: is_completed MUST remain unchanged
- Task ID MUST remain unchanged

### Success Response
```python
(True, "Task updated successfully")
```

### Failure Response
```python
(False, "Task not found")
# or
(False, "Task description cannot be empty")
```

### Edge Cases
| Input | Behavior |
|-------|----------|
| Valid ID, empty description | Return failure, description unchanged |
| Valid ID, valid description | Update description, status unchanged |
| Non-existent ID | Return failure, no side effects |

---

## Contract 4: Toggle Complete

**Method**: `toggle_complete(task_id: int) -> tuple[bool, str]`

### Inputs
| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| task_id | int | Yes | Must exist in collection |

### Outputs
| Position | Type | Description |
|----------|------|-------------|
| 0 | bool | Success flag |
| 1 | str | Human-readable message with new status |

### Behavior
1. Check if task_id exists in internal dictionary
2. If not exists: return failure immediately
3. If exists: flip is_completed boolean
4. Return success with new status

### Success Response (completed)
```python
(True, "Task marked as complete")
```

### Success Response (incomplete)
```python
(True, "Task marked as incomplete")
```

### Failure Response
```python
(False, "Task not found")
```

### Edge Cases
| Input | Behavior |
|-------|----------|
| Incomplete task | Toggle to complete |
| Complete task | Toggle to incomplete |
| Non-existent ID | Return failure, no side effects |
| Multiple toggles | Each toggle flips status predictably |

---

## Contract 5: List Tasks

**Method**: `list_tasks() -> list[Task]`

### Inputs
None

### Outputs
| Type | Description |
|------|-------------|
| list[Task] | List of all Task objects (may be empty) |

### Behavior
1. Return all tasks from internal dictionary
2. Return empty list if no tasks exist
3. Order: Insertion order (Python 3.7+ dict preserves order)

### Success Response (with tasks)
```python
[
    Task(id=1, description="Buy groceries", is_completed=False),
    Task(id=2, description="Call dentist", is_completed=True),
]
```

### Success Response (empty)
```python
[]
```

### Display Format (CLI Layer Responsibility)
```
=== Task List ===
[1] Buy groceries - Incomplete
[2] Call dentist - Complete
```

Or if empty:
```
No tasks available
```

---

## Contract 6: Get Task (Internal)

**Method**: `get_task(task_id: int) -> Task | None`

### Inputs
| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| task_id | int | Yes | Positive integer |

### Outputs
| Type | Description |
|------|-------------|
| Task \| None | Task object if found, None otherwise |

### Behavior
1. Look up task_id in internal dictionary
2. Return Task object if found
3. Return None if not found

### Usage
Internal helper method for other service methods. Not exposed to CLI layer directly.

---

## Summary Table

| Method | Input | Success Output | Failure Output |
|--------|-------|----------------|----------------|
| add_task | description: str | (True, msg, id) | (False, msg, None) |
| delete_task | task_id: int | (True, msg) | (False, "Task not found") |
| update_task | task_id, description | (True, msg) | (False, "Task not found" or "Empty description") |
| toggle_complete | task_id: int | (True, msg) | (False, "Task not found") |
| list_tasks | none | list[Task] | N/A (always succeeds) |
| get_task | task_id: int | Task | None |

---

## Traceability to Specification

| Contract | Functional Requirements |
|----------|------------------------|
| add_task | FR-001, FR-002, FR-003, FR-011, FR-012 |
| delete_task | FR-007, FR-008, FR-012 |
| update_task | FR-009, FR-011, FR-012 |
| toggle_complete | FR-010, FR-012 |
| list_tasks | FR-005, FR-006 |

| Contract | User Stories |
|----------|--------------|
| add_task | User Story 2 (Add Task) |
| delete_task | User Story 5 (Delete Task) |
| update_task | User Story 4 (Update Task) |
| toggle_complete | User Story 3 (Mark Task as Complete) |
| list_tasks | User Story 1 (View Task List) |
