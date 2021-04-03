from time import sleep

from rich.console import Console
from rich.progress import track

from rich_terminal.components.table import make_beer_table
from rich_terminal.prompts.utils import beer_specification


def make_progress_display(n: int):
    """
    Create Progress Display component.

    Parameters
    ----------
    n : int
        Number of interactions.
    """
    console = Console()
    beers = []

    for _ in range(n):
        beers.append(beer_specification())

    for n in track(range(n), description="Creating products..."):
        sleep(n + 3)

    console.rule("[bold red]Products Created")
    table = make_beer_table(beers)
    console.print(table)
