from typer import Typer

from .hello import app as hello_app
from .tokens import app as token_app

app = Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.callback()
def callback():
    """
    Some CLI management commands
    """


app.add_typer(
    hello_app,
)
app.add_typer(token_app)
