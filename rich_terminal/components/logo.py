from rich.panel import Panel
from rich.style import Style


def make_logo():
    """Make logo component."""
    logo = Panel(
        "\t \n \t :honeybee: RICH TERMINAL \n \t A proof of concept",
        width=42,
        height=6,
        style=Style(
            color='yellow',
            bgcolor='black',
        ),
        border_style='white'
    )

    return logo
