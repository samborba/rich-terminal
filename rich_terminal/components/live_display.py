from time import sleep

from rich.live import Live
from rich.table import Table


def make_live_table_display():
    """Make the Live Display component."""
    table = Table(title="Beers")

    table.add_column("Title", style="magenta")
    table.add_column("Price", justify="right", style="green")
    table.add_column("Size", justify="right", style="cyan", no_wrap=True)

    beers = [
        {
            "name": "Budweiser",
            "price": "R$3,88",
            "size": "330 ml"
        },
        {
            "name": "Hoegaarden",
            "price": "R$6,99",
            "size": "330 ml"
        },
        {
            "name": "Franziskaner",
            "price": "R$19,99",
            "size": "500 ml"
        },
        {
            "name": "Colorado Indica",
            "price": "R$15,99",
            "size": "600 ml"
        },
    ]

    with Live(table, refresh_per_second=4):
        for beer in beers:
            sleep(1)

            table.add_row(
                beer["name"],
                beer["price"],
                beer["size"],
            )
