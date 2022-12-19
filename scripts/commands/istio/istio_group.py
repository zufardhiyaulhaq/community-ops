import click

from .gateway.gateway_group import gateway
from .control_plane.control_plane_group import control_plane

@click.group()
def istio():
    pass

istio.add_command(gateway)
istio.add_command(control_plane)

