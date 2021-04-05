from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import IntPrompt

from rich_terminal.components.live_display import make_live_table_display
from rich_terminal.components.logging import make_logging
from rich_terminal.components.spinner import make_spinner
from rich_terminal.components.tree import make_tree
from rich_terminal.components.menu.brands import list_countries
from rich_terminal.prompts.products import beer_creation

MARKDOWN = Markdown("""
Select the feature to be shown:
1. List Products — (Spinner and Table)
2. Create Products — (Progress Display and Prompt)
3. Logging Handler — (Logging)
4. Products by Brand — (Tree)
5. List Products on Real Time — (Live Display)
6. Brand by County — (Markdown)
7. Exit POC
""")


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
        3: make_logging,
        4: make_tree,
        5: make_live_table_display,
        6: list_countries,
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
    console.print(MARKDOWN)

    # all component actions except `Exit POC`
    actions = ['1', '2', '3', '4', '5', '6']

    option = IntPrompt.ask("Enter your choice",
                           choices=actions.extend(['7']),
                           show_choices=False)

    if option not in actions:
        options(option)
        return True

    return False
