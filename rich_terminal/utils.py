from os import system, name


def clear_screen():
    """Clean the prompt."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
