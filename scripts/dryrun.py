#!/usr/bin/env python

from parser.configuration import ConfigurationParser
from deployer.helm import HelmDeployer
from deployer.shell import ShellDeployer
from deployer.kustomize import KustomizeDeployer
from deployer.manifest import ManifestDeployer

DEFAULT_CLUSTER_CONFIG = "config.yaml"
DEFAULT_CLUSTER_MANIFEST_DIR = "manifests/"

def main():
    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    kustomize = KustomizeDeployer(shell)
    kustomize.deploy(dryrun=True)

    manifest = ManifestDeployer(shell, DEFAULT_CLUSTER_MANIFEST_DIR)
    manifest.deploy(dryrun=True)

    helm = HelmDeployer(shell)
    helm.deploy(dryrun=True)

if __name__ == '__main__':
    main()
