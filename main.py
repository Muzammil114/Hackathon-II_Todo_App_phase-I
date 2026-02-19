"""Todo Application - Console-based in-memory task management.

Main entry point for the todo application.
"""

from src.cli.app import run_app


def main() -> None:
    """Run the todo application."""
    run_app()


if __name__ == "__main__":
    main()
