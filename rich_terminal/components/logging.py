import logging
from time import sleep

from rich.logging import RichHandler


def make_logging():
    """Make Logging Component."""
    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(
                show_time=True,
                show_level=True,
                rich_tracebacks=True,
            )
        ]
    )

    log = logging.getLogger("rich")

    log.info('Parsing API response...')

    sleep(3)

    log.warning('Parsing process is taking longer than expected')

    sleep(3)

    log.error(
        (
            "[bold red blink]"
            "An error was encountered while parsing objects."
        ),
        extra={"markup": True}
    )

    sleep(3)

    # example for real exception
    try:
        print(1 / 0)
    except Exception:
        log.exception("Unable to parse!")
