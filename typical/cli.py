# -*- coding: utf-8 -*-

"""Console script for typical."""

from __future__ import division, print_function, absolute_import

import click

@click.command()
def main(args=None):
    """Console script for typical."""
    click.echo("Replace this message by putting your code into "
               "typical.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
