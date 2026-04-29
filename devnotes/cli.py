import click
from devnotes.storage import add_note, list_notes, search_notes, delete_note

@click.group()
def cli():
    """DevNotes CLI - Developer note manager"""
    pass

@cli.command()
@click.argument("text")
@click.option("--tag", "-t", multiple=True, help="Add tags")
def add(text, tag):
    add_note(text, list(tag) or ["general"])
    click.echo("✅ Note added")

@cli.command()
def list():
    notes = list_notes()
    if not notes:
        click.echo("No notes found.")
        return

    for i, n in enumerate(notes):
        tags = ", ".join(n["tags"])
        click.echo(f"{i}. [{tags}] {n['text']}")

@cli.command()
@click.argument("keyword")
def search(keyword):
    results = search_notes(keyword)

    if not results:
        click.echo("No matches found.")
        return

    for n in results:
        tags = ", ".join(n["tags"])
        click.echo(f"[{tags}] {n['text']}")

@cli.command()
@click.argument("index", type=int)
def delete(index):
    result = delete_note(index)

    if result:
        click.echo("🗑️ Note deleted")
    else:
        click.echo("Invalid index")
        
if __name__ == "__main__":
    cli()