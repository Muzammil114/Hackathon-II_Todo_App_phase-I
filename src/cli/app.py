"""Command-line interface for the Todo Application.

Handles all user input and output, delegating business logic to TodoService.
"""

from src.services.todo_service import TodoService


def display_menu() -> None:
    """Display the main menu options."""
    print("\n=== Todo Application ===")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Mark Task Complete")
    print("6. Exit")


def display_task_list(tasks: list) -> None:
    """Display a list of tasks.

    Args:
        tasks: List of Task objects to display.
    """
    print("\n=== Task List ===")
    if not tasks:
        print("No tasks available")
        return

    for task in tasks:
        status = "Complete" if task.is_completed else "Incomplete"
        print(f"[{task.id}] {task.description} - {status}")


def display_error(message: str) -> None:
    """Display an error message.

    Args:
        message: The error message to display.
    """
    print(f"\nError: {message}")


def display_success(message: str) -> None:
    """Display a success message.

    Args:
        message: The success message to display.
    """
    print(f"\n{message}")


def validate_menu_choice(input_str: str) -> int | None:
    """Validate and parse menu choice input.

    Args:
        input_str: The user's input string.

    Returns:
        Integer choice if valid (1-6), None otherwise.
    """
    try:
        choice = int(input_str.strip())
        if 1 <= choice <= 6:
            return choice
        return None
    except ValueError:
        return None


def validate_task_id(input_str: str) -> int | None:
    """Validate and parse task ID input.

    Args:
        input_str: The user's input string.

    Returns:
        Positive integer if valid, None otherwise.
    """
    try:
        task_id = int(input_str.strip())
        if task_id > 0:
            return task_id
        return None
    except ValueError:
        return None


def prompt_add_task(service: TodoService) -> None:
    """Prompt user to add a new task.

    Args:
        service: The TodoService instance.
    """
    description = input("Enter task description: ")
    success, message, _ = service.add_task(description)
    if success:
        display_success(message)
    else:
        display_error(message)


def prompt_delete_task(service: TodoService) -> None:
    """Prompt user to delete a task.

    Args:
        service: The TodoService instance.
    """
    task_id_input = input("Enter task ID to delete: ")
    task_id = validate_task_id(task_id_input)
    if task_id is None:
        display_error("Invalid task ID. Please enter a number.")
        return

    success, message = service.delete_task(task_id)
    if success:
        display_success(message)
    else:
        display_error(message)


def prompt_update_task(service: TodoService) -> None:
    """Prompt user to update a task.

    Args:
        service: The TodoService instance.
    """
    task_id_input = input("Enter task ID to update: ")
    task_id = validate_task_id(task_id_input)
    if task_id is None:
        display_error("Invalid task ID. Please enter a number.")
        return

    new_description = input("Enter new description: ")
    success, message = service.update_task(task_id, new_description)
    if success:
        display_success(message)
    else:
        display_error(message)


def prompt_toggle_complete(service: TodoService) -> None:
    """Prompt user to toggle task completion status.

    Args:
        service: The TodoService instance.
    """
    task_id_input = input("Enter task ID to mark as complete: ")
    task_id = validate_task_id(task_id_input)
    if task_id is None:
        display_error("Invalid task ID. Please enter a number.")
        return

    success, message = service.toggle_complete(task_id)
    if success:
        display_success(message)
    else:
        display_error(message)


def handle_exit() -> None:
    """Handle application exit."""
    print("\nGoodbye!")


def run_app() -> None:
    """Run the main application loop."""
    service = TodoService()

    while True:
        display_menu()
        choice_input = input("Choose option: ")
        choice = validate_menu_choice(choice_input)

        if choice is None:
            display_error("Invalid option. Please try again.")
            continue

        if choice == 1:
            prompt_add_task(service)
        elif choice == 2:
            prompt_delete_task(service)
        elif choice == 3:
            prompt_update_task(service)
        elif choice == 4:
            tasks = service.list_tasks()
            display_task_list(tasks)
        elif choice == 5:
            prompt_toggle_complete(service)
        elif choice == 6:
            handle_exit()
            break
