#!/usr/bin/env python

import click
from dblib.querydb import querydb

#build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL from eth trading database to search the latest transactions information"""

# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM eth LIMIT 15",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query from eth trading database to search the latest transactions information"""
    querydb(query)


  
  #run the CLI
if __name__ == "__main__":
    cli()
