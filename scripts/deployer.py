#!/usr/bin/env python

import click

from commands.version import version_commands
from commands.helm.helm_group import helm
from commands.kustomize.kustomize_group import kustomize
from commands.manifests.manifests_group import manifests
from commands.istio.istio_group import istio

@click.group()
def main():
    pass

# command
main.add_command(version_commands.version)

# group
main.add_command(istio)
main.add_command(helm)
main.add_command(kustomize)
main.add_command(manifests)

if __name__ == '__main__':
    main()
