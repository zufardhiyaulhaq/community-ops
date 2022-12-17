#!/usr/bin/env python

from parser.configuration import ConfigurationParser
from deployer.helm import HelmDeployer
from deployer.shell import ShellDeployer
from deployer.kustomize import KustomizeDeployer
from deployer.manifest import ManifestDeployer
from deployer.istio import IstioDeployer
from utils import *

import os
import click

DEFAULT_CLUSTER_CONFIG = "config.yaml"
DEFAULT_CLUSTER_MANIFEST_DIR = "manifests/"

@click.command()
@click.option("--cluster-name",
              help="Cluster name to where the runtime should be deployed to",
              required=True)

def main(cluster_name):
    os.chdir("clusters/" + cluster_name)

    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    # print_header("Diff Kustomize")
    # kustomize = KustomizeDeployer(shell, cluster_name)
    # kustomize.diff()

    # print_header("Diff Manifest")
    # manifest = ManifestDeployer(shell, DEFAULT_CLUSTER_MANIFEST_DIR, cluster_name)
    # manifest.diff()

    # print_header("Diff Helm")
    # helm = HelmDeployer(shell, cluster_name)
    # helm.diff()

    print_header("Diff Istio Control Plane")
    istio_control_plane = configuration.get_istio_control_plane()
    istio = IstioDeployer(shell, istio_control_plane, cluster_name)
    istio.diff()

    # print_header("Diff Istio Gateway")
    # istio_gateways = configuration.get_istio_gateway()
    # for gateway in istio_gateways:
    #     istio = IstioDeployer(shell, gateway, cluster_name)
    #     istio.diff()

if __name__ == '__main__':
    main()
