from rich.tree import Tree
from rich import print


def make_tree():
    """Make the Tree component."""
    tree = Tree("Products by Brand")

    skol_tree = tree.add("[white]Skol")
    brahma_tree = tree.add("[red]Brahma")
    colorado_tree = tree.add("[yellow]Colorado")

    skol_tree.add("[blue]Skol Beats")
    skol_tree.add("[purple]Skol Beats Zodiac")
    skol_tree.add("[yellow]Skol Puro Malte")

    brahma_tree.add("[red]Brahma Duplo Malte")
    brahma_tree.add("[green]Brahma Malzbier")

    colorado_tree.add("[green]Colorado Indica")
    colorado_tree.add("[blue]Colorado Ribeirão")
    colorado_tree.add("[yellow]Colorado Murica")

    print(tree)
