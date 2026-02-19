"""Task entity representing a single todo item."""

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single todo item with three attributes.

    Attributes:
        id: Unique identifier, auto-generated sequential starting from 1.
        description: Task description text, must be non-empty.
        is_completed: Completion status, defaults to False.
    """

    id: int
    description: str
    is_completed: bool = field(default=False)

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.is_completed = True

    def mark_incomplete(self) -> None:
        """Mark this task as incomplete."""
        self.is_completed = False

    def update_description(self, new_description: str) -> None:
        """Update the task description.

        Args:
            new_description: The new description text.
        """
        self.description = new_description
