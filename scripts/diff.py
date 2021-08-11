#!/usr/bin/env python

from parser.configuration import ConfigurationParser
from deployer.helm import HelmDeployer
from deployer.shell import ShellDeployer
from deployer.kustomize import KustomizeDeployer
from deployer.manifest import ManifestDeployer
from deployer.istio import IstioDeployer
from utils import *

DEFAULT_CLUSTER_CONFIG = "config.yaml"
DEFAULT_CLUSTER_MANIFEST_DIR = "manifests/"

def main():
    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    print_header("Diff Kustomize")
    kustomize = KustomizeDeployer(shell)
    kustomize.diff()

    print_header("Diff Manifest")
    manifest = ManifestDeployer(shell, DEFAULT_CLUSTER_MANIFEST_DIR)
    manifest.diff()

    print_header("Diff Helm")
    helm = HelmDeployer(shell)
    helm.diff()

    print_header("Diff Istio")
    istio_config_file = configuration.get_istio()
    istio = IstioDeployer(shell, istio_config_file)
    istio.diff()

if __name__ == '__main__':
    main()
