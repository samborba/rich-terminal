from rich.prompt import Confirm, FloatPrompt, IntPrompt, Prompt


def beer_specification():
    """
    Prompts beer specification.

    Returns
    -------
    dict
        A dict with beer specifications.
    """
    name = Prompt.ask("Enter the beer name")
    quantity = IntPrompt.ask("Quantity")
    price = FloatPrompt.ask("Price (Float format)")
    is_alcoholic = Confirm.ask("Is alcoholic?")

    return {
        "name": name,
        "quantity": quantity,
        "price": price,
        "isAlcoholic": is_alcoholic
    }
