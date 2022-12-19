import os
import click

from utils import *
from parser.configuration import ConfigurationParser
from deployer.helm import HelmDeployer
from deployer.shell import ShellDeployer

@click.command()
@click.option("--cluster-name",
              help="Cluster name to where the runtime should be deployed to",
              required=True)
def deploy(cluster_name):
    os.chdir(DEFAULT_CLUSTERS_DIR + cluster_name)

    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    print_header("Deploying Helm")
    helm = HelmDeployer(shell, cluster_name)
    helm.deploy()
