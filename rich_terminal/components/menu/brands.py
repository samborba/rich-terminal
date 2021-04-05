from time import sleep

from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import IntPrompt

MARKDOWN = Markdown("""
# Select the country:
1. Brazil
2. Germany
3. Belgium
4. United Kingdom
5. Netherlands
""")


def list_brazil_brands():
    """List Brazil brands."""
    console = Console()
    markdown = Markdown("""
- Liber
- Antarctica
- Cervejaria Wäls
- Aqua Fratelli Vita
- Cervejaria Colorado
    """)
    markdown = Markdown(markdown)
    console.print(markdown)


def list_germany_brands():
    """List Germany brands."""
    console = Console()
    markdown = Markdown("""
- Dimix
- Beck's
- Haake-Beck
- Gilde Ratskeller
- Franziskaner Weissbier
    """)
    console.print(markdown)


def list_belgium_brands():
    """List Belgium brands."""
    console = Console()
    markdown = Markdown("""
- Leffe
- Belle-Vue
- Hoegaarden
- Vieux Temps
- Bosteels Brewery
    """)
    console.print(markdown)


def list_uk_brands():
    """List United Kingdom brands."""
    console = Console()
    markdown = Markdown("""
- Bass
- Whitbread
- Boddingtons
- Camden Town Brewery
    """)
    console.print(markdown)


def list_netherlands_brands():
    """List Netherlands brands."""
    console = Console()
    markdown = Markdown("""
- Dommelsch
- Hertog Jan
- Oranjeboom
    """)

    console.print(markdown)


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
