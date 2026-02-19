"""TodoService - Business logic for task operations."""

from typing import Optional
from src.models.task import Task


class TodoService:
    """Business logic container for task operations.

    Manages an in-memory task collection with dictionary-based storage
    for O(1) lookup by task ID.

    Attributes:
        _tasks: Internal storage mapping task ID to Task object.
        _next_id: Counter for generating the next task ID.
    """

    def __init__(self) -> None:
        """Initialize the TodoService with empty task collection."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, description: str) -> tuple[bool, str, Optional[int]]:
        """Add a new task with the given description.

        Args:
            description: The task description, must be non-empty.

        Returns:
            A tuple of (success, message, task_id).
            On success: (True, "Task added with ID {id}", task_id)
            On failure: (False, "Task description cannot be empty", None)
        """
        # Validate description
        if not description or not description.strip():
            return (False, "Task description cannot be empty", None)

        # Create task with auto-increment ID
        task_id = self._next_id
        task = Task(id=task_id, description=description.strip(), is_completed=False)
        self._tasks[task_id] = task
        self._next_id += 1

        return (True, f"Task added with ID {task_id}", task_id)

    def delete_task(self, task_id: int) -> tuple[bool, str]:
        """Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete.

        Returns:
            A tuple of (success, message).
            On success: (True, "Task deleted successfully")
            On failure: (False, "Task not found")
        """
        if task_id not in self._tasks:
            return (False, "Task not found")

        del self._tasks[task_id]
        return (True, "Task deleted successfully")

    def update_task(self, task_id: int, new_description: str) -> tuple[bool, str]:
        """Update a task's description while preserving completion status.

        Args:
            task_id: The ID of the task to update.
            new_description: The new description text.

        Returns:
            A tuple of (success, message).
            On success: (True, "Task updated successfully")
            On failure: (False, "Task not found") or (False, "Task description cannot be empty")
        """
        if task_id not in self._tasks:
            return (False, "Task not found")

        if not new_description or not new_description.strip():
            return (False, "Task description cannot be empty")

        self._tasks[task_id].update_description(new_description.strip())
        return (True, "Task updated successfully")

    def toggle_complete(self, task_id: int) -> tuple[bool, str]:
        """Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle.

        Returns:
            A tuple of (success, message).
            On success: (True, "Task marked as complete" or "Task marked as incomplete")
            On failure: (False, "Task not found")
        """
        if task_id not in self._tasks:
            return (False, "Task not found")

        task = self._tasks[task_id]
        if task.is_completed:
            task.mark_incomplete()
            return (True, "Task marked as incomplete")
        else:
            task.mark_complete()
            return (True, "Task marked as complete")

    def list_tasks(self) -> list[Task]:
        """List all tasks in the collection.

        Returns:
            A list of all Task objects. Returns empty list if no tasks exist.
        """
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The Task object if found, None otherwise.
        """
        return self._tasks.get(task_id)
