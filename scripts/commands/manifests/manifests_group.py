import click

from .deploy import deploy
from .diff import diff
from .dryrun import dryrun

@click.group()
def manifests():
    pass

manifests.add_command(deploy)
manifests.add_command(diff)
manifests.add_command(dryrun)
