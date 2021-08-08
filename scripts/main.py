#!/usr/bin/env python

from parser.configuration import ConfigurationParser
from deployer.helm import HelmDeployer
from deployer.shell import ShellDeployer
from deployer.kustomize import KustomizeDeployer

DEFAULT_CLUSTER_CONFIG = "config.yaml"


def main():
    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()
    kustomize = KustomizeDeployer(shell)
    kustomize.deploy()

    shell.execute(["kubectl", "apply", "-f", "manual_manifest/", "-R"])

    helm = HelmDeployer(configuration.get(), shell)
    helm.deploy()


if __name__ == '__main__':
    main()
