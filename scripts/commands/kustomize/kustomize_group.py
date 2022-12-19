import click

from .deploy import deploy
from .diff import diff
from .dryrun import dryrun

@click.group()
def kustomize():
    pass

kustomize.add_command(deploy)
kustomize.add_command(diff)
kustomize.add_command(dryrun)
