from time import sleep

from rich import print
from rich.console import Console
from rich.prompt import IntPrompt

MARKDOWN = """
Select the country:
1. Brazil
2. Germany
3. Belgium
4. United Kingdom
5. Netherlands
"""


def list_brazil_brands():
    """List Brazil brands."""
    markdown = """
- Liber
- Antarctica
- Cervejaria Wäls
- Aqua Fratelli Vita
- Cervejaria Colorado
    """
    print(markdown)


def list_germany_brands():
    """List Germany brands."""
    markdown = """
- Dimix
- Beck's
- Haake-Beck
- Gilde Ratskeller
- Franziskaner Weissbier
    """
    print(markdown)


def list_belgium_brands():
    """List Belgium brands."""
    markdown = """
- Leffe
- Belle-Vue
- Hoegaarden
- Vieux Temps
- Bosteels Brewery
    """
    print(markdown)


def list_uk_brands():
    """List United Kingdom brands."""
    markdown = """
- Bass
- Whitbread
- Boddingtons
- Camden Town Brewery
    """
    print(markdown)


def list_netherlands_brands():
    """List Netherlands brands."""
    markdown = """
- Dommelsch
- Hertog Jan
- Oranjeboom
    """
    print(markdown)


def options(option: int):
    """
    Make some action.

    Parameters
    ----------
    option : int
        The selected option
    """
    {
        1: list_brazil_brands,
        2: list_germany_brands,
        3: list_belgium_brands,
        4: list_uk_brands,
        5: list_netherlands_brands,
    }[option]()


def list_countries():
    """Country list menu."""
    console = Console()
    console.print(MARKDOWN)

    mapper = {
        1: "Brazil",
        2: "Germany",
        3: "Belgium",
        4: "United Kingdom",
        5: "Netherlands",
    }

    option = IntPrompt.ask("Enter your choice",
                           choices=["1", "2", "3", "4", "5"],
                           show_choices=False)

    with console.status(f"Getting {mapper[option]} brands..."):
        sleep(2)

        console.rule(f"{mapper[option]} Brands")
        options(option)
