# Quick Start: Todo Application

**Feature**: 001-todo-app
**Created**: 2026-02-19
**Version**: 1.0.0

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Installation

1. Navigate to project root directory
2. Run `uv sync` to install dependencies (standard library only)

## Usage

### Starting the Application

```bash
uv run python src/main.py
```

### Main Menu

Upon startup, you will see the main menu:

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Task Complete
6. Exit
Choose option:
```

### Feature Guide

#### 1. Add Task

**Purpose**: Create a new task with a description.

**Steps**:
1. Select option `1` from the menu
2. Enter task description when prompted
3. System assigns a unique ID automatically
4. Confirmation message displays the new task ID

**Example**:
```
Choose option: 1
Enter task description: Buy groceries
Task added with ID 1
```

**Validation**:
- Description cannot be empty
- Description cannot be whitespace only

---

#### 2. Delete Task

**Purpose**: Remove a task you no longer need.

**Steps**:
1. Select option `2` from the menu
2. Enter the task ID to delete
3. System removes the task if it exists

**Example**:
```
Choose option: 2
Enter task ID to delete: 1
Task deleted successfully
```

**Error Handling**:
- If task ID doesn't exist: "Task not found"

---

#### 3. Update Task

**Purpose**: Modify the description of an existing task.

**Steps**:
1. Select option `3` from the menu
2. Enter the task ID to update
3. Enter the new description
4. Task status (complete/incomplete) remains unchanged

**Example**:
```
Choose option: 3
Enter task ID to update: 1
Enter new description: Buy 2% milk
Task updated successfully
```

**Error Handling**:
- If task ID doesn't exist: "Task not found"
- If new description is empty: "Task description cannot be empty"

---

#### 4. View Tasks

**Purpose**: Display all tasks with their ID, description, and status.

**Steps**:
1. Select option `4` from the menu
2. System displays all tasks or "No tasks available"

**Example**:
```
Choose option: 4
=== Task List ===
[1] Buy groceries - Incomplete
[2] Call dentist - Complete
```

**Empty State**:
```
=== Task List ===
No tasks available
```

---

#### 5. Mark Task Complete

**Purpose**: Toggle a task's completion status.

**Steps**:
1. Select option `5` from the menu
2. Enter the task ID to toggle
3. System flips the status (complete ↔ incomplete)

**Example**:
```
Choose option: 5
Enter task ID to mark as complete: 1
Task marked as complete
```

**Toggle Behavior**:
- Incomplete → Complete: "Task marked as complete"
- Complete → Incomplete: "Task marked as incomplete"

**Error Handling**:
- If task ID doesn't exist: "Task not found"

---

#### 6. Exit

**Purpose**: Close the application.

**Steps**:
1. Select option `6` from the menu
2. Application exits cleanly

**Note**: All tasks are stored in memory only and will be lost when the application exits.

---

## Common Issues

### "Task not found"

**Cause**: The task ID you entered doesn't exist.

**Solution**: 
1. Use "View Tasks" (option 4) to see existing task IDs
2. Ensure you're entering a valid number

---

### "Invalid task ID. Please enter a number."

**Cause**: You entered non-numeric input for a task ID.

**Solution**: Enter only numeric values (e.g., `1`, `2`, `3`)

---

### "Task description cannot be empty"

**Cause**: You entered an empty string or only whitespace.

**Solution**: Enter at least one visible character in the description

---

### "Invalid option. Please try again."

**Cause**: You entered a number outside the valid menu range (1-6).

**Solution**: Enter a number between 1 and 6

---

## Example Session

Here's a complete example session:

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

Choose option: 1
Enter task description: Call dentist
Task added with ID 2

Choose option: 4
=== Task List ===
[1] Buy groceries - Incomplete
[2] Call dentist - Incomplete

Choose option: 5
Enter task ID to mark as complete: 1
Task marked as complete

Choose option: 4
=== Task List ===
[1] Buy groceries - Complete
[2] Call dentist - Incomplete

Choose option: 3
Enter task ID to update: 2
Enter new description: Call dentist office
Task updated successfully

Choose option: 4
=== Task List ===
[1] Buy groceries - Complete
[2] Call dentist office - Incomplete

Choose option: 2
Enter task ID to delete: 1
Task deleted successfully

Choose option: 4
=== Task List ===
[2] Call dentist office - Incomplete

Choose option: 6
Goodbye!
```

---

## Architecture Notes

**For Developers**: This application follows clean architecture:

- **CLI Layer** (`src/cli/`): Handles all user input and output
- **Service Layer** (`src/services/`): Contains all business logic
- **Model Layer** (`src/models/`): Defines the Task data structure

Business logic is fully separated from user interface, enabling independent testing and maintenance.

---

## Support

For issues or questions, refer to the full specification at `specs/001-todo-app/spec.md`
