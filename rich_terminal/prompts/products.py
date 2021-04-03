from rich.prompt import IntPrompt

from rich_terminal.components.progress_display import make_progress_display


def beer_creation():
    """
    Create beer.

    Returns
    -------
    list
        A list with all beers.
    """
    quantity = IntPrompt.ask("How many products do you want to create?")
    make_progress_display(quantity)
