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
def deploy(cluster_name, revision):
    os.chdir(DEFAULT_CLUSTERS_DIR + cluster_name)

    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    print_header(f'Deploying Istio Gateway with revision {revision}')
    istio_gateways = configuration.get_istio_gateway()
    for gateway in istio_gateways:
        istio = IstioDeployer(shell, gateway, cluster_name)
        istio.deploy(revision=revision)

