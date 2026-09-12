import click

from .gateway.gateway_group import gateway
from .control_plane.control_plane_group import control_plane
from .version import version
from .revision import revision

@click.group()
def istio():
    pass

istio.add_command(gateway)
istio.add_command(control_plane)
istio.add_command(version)
istio.add_command(revision)

