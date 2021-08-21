#!/usr/bin/env python

from parser.configuration import ConfigurationParser
from deployer.helm import HelmDeployer
from deployer.shell import ShellDeployer
from deployer.kustomize import KustomizeDeployer
from deployer.manifest import ManifestDeployer
from deployer.istio import IstioDeployer
from utils import *

import click

DEFAULT_CLUSTER_CONFIG = "config.yaml"
DEFAULT_CLUSTER_MANIFEST_DIR = "manifests/"

@click.command()
@click.option("--cluster-name",
              help="Cluster name to where the runtime should be deployed to",
              required=True)

def main(cluster_name):
    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    print_header("Deploying Kustomize")
    kustomize = KustomizeDeployer(shell, cluster_name)
    kustomize.deploy()

    print_header("Deploying Manifest")
    manifest = ManifestDeployer(shell, DEFAULT_CLUSTER_MANIFEST_DIR, cluster_name)
    manifest.deploy()

    print_header("Deploying Helm")
    helm = HelmDeployer(shell, cluster_name)
    helm.deploy()

    print_header("Deploying Istio")
    istio_config_file = configuration.get_istio()
    istio = IstioDeployer(shell, istio_config_file, cluster_name)
    istio.deploy()

if __name__ == '__main__':
    main()
