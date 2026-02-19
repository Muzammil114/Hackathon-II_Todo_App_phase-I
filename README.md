# Console-Based In-Memory Todo Application

A simple, interactive command-line todo application built with Python, featuring full CRUD functionality for task management without any external dependencies.

## Features

- **Add Tasks**: Create new tasks with descriptions
- **View Tasks**: See all tasks with their ID and completion status
- **Update Tasks**: Modify existing task descriptions
- **Delete Tasks**: Remove tasks you no longer need
- **Mark Complete**: Toggle task completion status
- **In-Memory Storage**: Tasks are stored in memory during the session
- **Interactive Menu**: User-friendly command-line interface
- **Input Validation**: Validates user inputs and provides helpful error messages
- **Clean Architecture**: Separated concerns between CLI interface, business logic, and data models

## Requirements

- Python 3.13 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Muzammil114/Hackathon-II_Todo_App_phase-I.git
cd Hackathon-II_Todo_App_phase-I
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows: .venv\Scripts\activate
```

3. Run the application directly with Python:
```bash
python main.py
```

Alternative method using UV package manager:
```bash
uv run python main.py
```

## Usage

The application presents a menu-driven interface with the following options:

1. **Add Task**: Create a new task with a description
2. **Delete Task**: Remove a task by its ID
3. **Update Task**: Modify the description of an existing task
4. **View Tasks**: Display all current tasks with their status
5. **Mark Task Complete**: Toggle the completion status of a task
6. **Exit**: Close the application

### Menu Options

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

**Add Task (Option 1)**
- Enter task description when prompted
- System assigns a unique ID automatically (starting from 1)
- Task is created with "Incomplete" status by default

**Delete Task (Option 2)**
- Enter the task ID to delete
- System removes the task if it exists
- Error message if the task ID doesn't exist

**Update Task (Option 3)**
- Enter the task ID to update
- Enter the new description
- Task status (complete/incomplete) remains unchanged

**View Tasks (Option 4)**
- Displays all tasks with ID, description, and status
- Shows "No tasks available" if the list is empty

**Mark Task Complete (Option 5)**
- Enter the task ID to toggle
- System flips the status (complete ↔ incomplete)
- Displays confirmation message

**Exit (Option 6)**
- Closes the application cleanly
- Note: All tasks are stored in memory only and will be lost when the application exits

### Example Workflow

1. Run `python main.py`
2. Select option 1 to add tasks
3. Select option 4 to view all tasks
4. Select option 5 to mark a task as complete
5. Select option 6 to exit the application

## Project Structure

```
.
├── main.py                 # Main entry point
├── pyproject.toml          # Project metadata and dependencies
├── src/
│   ├── cli/
│   │   └── app.py          # Command-line interface logic
│   ├── models/
│   │   └── task.py         # Task data model
│   └── services/
│       └── todo_service.py # Business logic layer
└── specs/
    └── 001-todo-app/       # Project specifications
```

## Architecture

The application follows a clean architecture pattern:

- **CLI Layer** (`src/cli/app.py`): Handles user input/output and menu navigation
- **Service Layer** (`src/services/todo_service.py`): Contains business logic for task operations
- **Model Layer** (`src/models/task.py`): Defines the Task entity structure

## Task Model

Each task has three attributes:
- `id`: Unique integer identifier (auto-incremented starting from 1)
- `description`: Text description of the task
- `is_completed`: Boolean indicating completion status (defaults to False)

## Common Issues & Solutions

- **"Task not found"**: The task ID you entered doesn't exist. Use "View Tasks" (option 4) to see existing task IDs.
- **"Invalid task ID. Please enter a number."**: You entered non-numeric input for a task ID. Enter only numeric values.
- **"Task description cannot be empty"**: You entered an empty string or only whitespace. Enter at least one visible character.
- **"Invalid option. Please try again."**: You entered a number outside the valid menu range (1-6). Enter a number between 1 and 6.

## Development

This project was created as part of the GIAIC Q4 Hackathon II - Phase I.

### Key Features Implemented

- Full CRUD operations (Create, Read, Update, Delete)
- Input validation for task descriptions and IDs
- Error handling with appropriate user messages
- Sequential ID assignment starting from 1
- In-memory storage with persistence only during the session
- Clean separation of concerns between CLI interface and business logic
- Deterministic output - same input always yields same output

## License

This project is open source and available under the MIT License.