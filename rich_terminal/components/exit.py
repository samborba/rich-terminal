from rich import box
from rich.align import Align
from rich.console import RenderGroup
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


def make_message():
    message = Table.grid(padding=1)
    message.add_column(style="green", justify="right")
    message.add_column(no_wrap=True)

    intro_message = Text.from_markup(
        """Thanks for trying out!"""
    )
    message.add_row(
        "Check the Repository on GitHub",
        ("[u blue link=https://github.com/samborba]"
         "https://github.com/samborba/rich-terminal")
    )

    message_panel = Panel(
        Align.center(
            RenderGroup(intro_message, "\n", Align.center(message)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        title="[b white]RICH TERMINAL",
        border_style="bright_blue",
    )

    return message_panel


def make_exit_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")
    message = make_message()

    layout.split(
        Layout(
            name="body",
        )
    )

    layout["body"].update(message)

    return layout
