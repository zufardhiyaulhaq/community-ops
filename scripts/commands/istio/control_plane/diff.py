import os
import click

from utils import *
from parser.configuration import ConfigurationParser
from deployer.istio import IstioDeployer
from deployer.shell import ShellDeployer

@click.command()
@click.option("--cluster-name",
              help="Cluster name to where the runtime should be deployed to",
              required=True)
@click.option("--revision",
              help="Deploy control plane with revision",
              required=False)
def diff(cluster_name, revision):
    os.chdir(DEFAULT_CLUSTERS_DIR + cluster_name)

    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    print_header(f'Diff Istio Control Plane with revision {revision}')
    istio_control_plane = configuration.get_istio_control_plane()
    istio = IstioDeployer(shell, istio_control_plane, cluster_name)
    istio.diff(revision=revision)
