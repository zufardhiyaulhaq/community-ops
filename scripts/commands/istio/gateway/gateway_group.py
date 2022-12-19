import click

from .deploy import deploy
from .diff import diff
from .dryrun import dryrun

@click.group()
def gateway():
    pass

gateway.add_command(deploy)
gateway.add_command(diff)
gateway.add_command(dryrun)
