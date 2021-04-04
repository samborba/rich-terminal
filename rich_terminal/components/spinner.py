from time import sleep

from rich.console import Console

from rich_terminal.components.table import make_table


def work():
    """Let's pretend that this is a long work."""
    sleep(5)


def make_spinner():
    """Make Spinner component with a mocked response table."""
    console = Console()
    response = make_table()

    with console.status('Getting data...'):
        work()

    console.rule("[bold red]API Response")
    console.print(response)


def make_eof_spinner():
    """Make Spinner component EOF exception."""
    console = Console()

    with console.status('Closing aplication...'):
        sleep(1)
