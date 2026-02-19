# Data Model: Todo Application

**Feature**: 001-todo-app
**Created**: 2026-02-19
**Status**: Approved

## Core Entities

### Task

Represents a single todo item with three attributes.

| Field | Type | Description | Constraints | Validation |
|-------|------|-------------|-------------|------------|
| id | int | Unique identifier | Auto-generated, sequential, starts at 1 | Must be positive integer |
| description | str | Task description text | Non-empty, non-whitespace | `len(description.strip()) > 0` |
| is_completed | bool | Completion status | Default: False | Boolean only |

**Invariants**:
- ID is immutable after creation
- Description can be updated but never empty
- Status toggles only via explicit method call

**State Transitions**:
```
Created (is_completed=False) → Toggle Complete → Completed (is_completed=True)
Completed (is_completed=True) → Toggle Complete → Created (is_completed=False)
```

### TodoService

Business logic container for task operations. Manages in-memory task collection.

| Attribute | Type | Description |
|-----------|------|-------------|
| _tasks | dict[int, Task] | Internal storage: {id: Task} |
| _next_id | int | Counter for next task ID (starts at 1) |

**Methods**:

| Method | Signature | Returns | Description |
|--------|-----------|---------|-------------|
| add_task | `add_task(description: str) -> tuple[bool, str, int | None]` | (success, message, task_id) | Creates new task with auto-increment ID |
| delete_task | `delete_task(task_id: int) -> tuple[bool, str]` | (success, message) | Removes task by ID if exists |
| update_task | `update_task(task_id: int, new_description: str) -> tuple[bool, str]` | (success, message) | Updates description, preserves status |
| toggle_complete | `toggle_complete(task_id: int) -> tuple[bool, str]` | (success, message) | Flips is_completed boolean |
| list_tasks | `list_tasks() -> list[Task]` | list[Task] | Returns all tasks (empty list if none) |
| get_task | `get_task(task_id: int) -> Task | None` | Task or None | Returns task by ID or None |

## Storage Strategy

**Type**: In-memory dictionary
**Lifetime**: Runtime only (cleared on application exit)
**Access Pattern**: O(1) lookup by ID

```python
# Internal structure
{
    1: Task(id=1, description="Buy groceries", is_completed=False),
    2: Task(id=2, description="Call dentist", is_completed=True),
}
```

**Rationale**:
- O(1) lookup for all ID-based operations
- Natural mapping: task ID → Task object
- Prevents duplicate IDs
- Simpler than list for delete/update operations

## ID Generation Strategy

**Mechanism**: Auto-increment counter
**Starting Value**: 1
**Update**: Incremented after each successful add_task call

```python
# Pseudocode
_next_id = 1
def add_task(description):
    task = Task(id=_next_id, description=description, is_completed=False)
    _next_id += 1
    return task
```

**Properties**:
- Deterministic: Same sequence of adds produces same IDs
- Sequential: Easy to understand and predict
- Unique: No collisions possible (single-threaded, in-memory)

## Validation Rules

### Task Description
- MUST be non-empty string
- MUST contain at least one non-whitespace character
- MAY contain any printable characters
- Maximum length: System memory (no artificial limit)

### Task ID
- MUST be positive integer (>= 1)
- MUST exist in collection for update/delete/toggle operations
- CANNOT be modified after creation

### Task Status
- MUST be boolean (True/False)
- Changes only via toggle_complete method
- Default: False (incomplete)

## Error Conditions

| Condition | Error Message | Handled By |
|-----------|---------------|------------|
| Empty description | "Task description cannot be empty" | add_task, update_task |
| Non-existent ID | "Task not found" | delete_task, update_task, toggle_complete |
| Invalid ID type | "Invalid task ID. Please enter a number." | CLI layer validation |

## Dependencies

- **None**: Task entity has no external dependencies
- **Standard Library Only**: No external packages required

## Traceability

| Data Element | Spec Requirement |
|--------------|------------------|
| Task.id | FR-002 (unique sequential IDs) |
| Task.description | FR-011 (non-empty validation) |
| Task.is_completed | FR-010 (toggle behavior) |
| TodoService.add_task | FR-001, FR-002, FR-003, FR-012 |
| TodoService.delete_task | FR-007, FR-008, FR-012 |
| TodoService.update_task | FR-009, FR-011, FR-012 |
| TodoService.toggle_complete | FR-010, FR-012 |
| TodoService.list_tasks | FR-005, FR-006 |
