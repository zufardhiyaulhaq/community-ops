import click

from .deploy import deploy
from .diff import diff
from .dryrun import dryrun

@click.group()
def control_plane():
    pass

control_plane.add_command(deploy)
control_plane.add_command(diff)
control_plane.add_command(dryrun)
