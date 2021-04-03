from rich.table import Table


def make_table():
    """
    Make table component.

    Returns
    -------
    rich.table.Table
        The component.
    """
    table = Table(title="Beers")

    table.add_column("Title", style="magenta")
    table.add_column("Price", justify="right", style="green")
    table.add_column("Size", justify="right", style="cyan", no_wrap=True)

    table.add_row("Hoegaarden", "R$6,99", "330 ml")
    table.add_row("Colorado Indica", "R$15,99", "600 ml")
    table.add_row("Budweiser", "R$3,88", "330 ml")
    table.add_row("Franziskaner", "R$19,99", "500 ml")

    return table


def make_beer_table(beers: list):
    """
    Make beer table component.

    Parameters
    ----------
    beers : list

    Returns
    -------
    rich.table.Table
        The component.
    """
    table = Table(title="Beers")

    table.add_column("Name", style="magenta")
    table.add_column("Price", justify="right", style="green")
    table.add_column("Quantity", style="white")
    table.add_column("Alcoholic", justify="right", style="cyan", no_wrap=True)

    for beer in beers:
        table.add_row(
            beer["name"],
            str(beer["price"]),
            str(beer["quantity"]),
            str(beer["isAlcoholic"]),
        )

    return table
