from rich import print

from rich.prompt import Confirm

from rich_terminal.components.exit import make_exit_layout
from rich_terminal.components.logo import make_logo
from rich_terminal.components.spinner import make_eof_spinner

from rich_terminal.components.menu.initial import initial_menu
from rich_terminal.utils import clear_screen


def exit_application():
    """Exit the application."""
    exit_screen = make_exit_layout()

    print(exit_screen)
    exit()


def start():
    """Start the application"""
    logo = make_logo()
    clear_screen()
    print(logo)

    operation_has_finished = initial_menu()

    if operation_has_finished:
        should_continue = Confirm.ask("Do you want to continue using the POC?")

        if should_continue:
            start()

    exit_application()


if __name__ == "__main__":
    try:
        start()
    except (EOFError, KeyboardInterrupt):
        make_eof_spinner()
