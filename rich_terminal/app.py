from rich import print
from rich.console import Console
from rich.prompt import IntPrompt, Confirm

from rich_terminal.components.logo import make_logo
from rich_terminal.components.exit import make_exit_layout
from rich_terminal.components.spinner import make_spinner
from rich_terminal.prompts.products import beer_creation

from rich_terminal.utils import clear_screen

_markdown = """
Select the feature to be shown:
1. List Products — (Spinner and Table)
2. Create Products — (Progress Display)
3. Table
4. Logging
5. Live Display
6. Prompt
7. Exit POC
"""


def exit_application():
    """Exit the application."""
    exit_screen = make_exit_layout()

    print(exit_screen)
    exit()


def options(option: int):
    """
    Make some action.

    Parameters
    ----------
    option : int
        The selected option
    """
    {
        1: make_spinner,
        2: beer_creation,
        3: print(),
        4: print(),
        5: print(),
        6: print(),
    }[option]()


def initial_menu():
    """
    Shows the initial menu.

    Returns
    -------
    bool
        If `True`, means that all operations has finished,
        else (`False`) user want to exit.
    """
    console = Console()
    console.print(_markdown)

    option = IntPrompt.ask("Enter your choice",
                           choices=['1', '2', '3', '4', '5', '6', '7'],
                           show_choices=False)

    if option != 7:
        options(option)
        return True

    return False


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
    start()
