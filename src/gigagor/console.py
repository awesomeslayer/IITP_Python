import textwrap
from typing import Any

import click
import requests

from . import __version__

API_URL: str = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """The hypermodern Python project."""
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data: Any = response.json()

    title: str = data["title"]
    extract: str = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
