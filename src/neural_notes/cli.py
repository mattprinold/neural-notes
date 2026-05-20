import typer

app = typer.Typer(help="Neural Notes CLI", no_args_is_help=True, invoke_without_command=True)

@app.callback()
def callback() -> None:
    """Neural Notes CLI."""


@app.command()
def health() -> None:
    """Check the CLI is working."""
    typer.echo("CLI is healthy!")

def main() -> None:
    app()