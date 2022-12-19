import click

from .deploy import deploy
from .diff import diff
from .dryrun import dryrun

@click.group()
def helm():
    pass

helm.add_command(deploy)
helm.add_command(diff)
helm.add_command(dryrun)

