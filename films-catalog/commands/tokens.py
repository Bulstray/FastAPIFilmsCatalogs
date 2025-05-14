from typing import Annotated

import typer
from rich import print
from rich.markdown import Markdown

from api.api_v1.auth.services import redis_tokens as tokens

app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
    name="token",
    help="Tokens managements",
)


@app.command()
def check(
    token: Annotated[
        str,
        typer.Argument(
            help="The token to check",
        ),
    ],
):
    print(
        f"Token [bold]{token}[/bold] [green]exists[/green]"
        if tokens.token_exist(token)
        else f"{token} [red]does not exist[/red]"
    )


@app.command(name="list")
def get_tokens():
    print(Markdown("# Available API Tokens"))
    print(Markdown("\n- ".join([""] + tokens.get_tokens())))
    print()


@app.command()
def create():
    new_token = tokens.generate_and_save_token()
    print(f"New token [bold]{new_token}[/bold] saved to db.")


@app.command()
def add(
    token: Annotated[
        str,
        typer.Argument(help="The token to add"),
    ],
):
    """
    Add the provided token to db.
    """
    tokens.add_token(
        token,
    )
    print(f"Token [bold]{token}[/bold] added to db.")


@app.command(name="rm")
def delete(
    token: Annotated[
        str,
        typer.Argument(
            help="The token to delete",
        ),
    ],
):
    """
    Delete the provide token from db.
    """

    if not tokens.token_exist(token):
        print(f"Token [bold]{token} [red]does not exist[/red][/bold].")
        return

    tokens.delete_token(token)
    print(f"Token [bold]{token}[/bold] removed from db.")
