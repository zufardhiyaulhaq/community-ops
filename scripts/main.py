#!/usr/bin/env python

from parser.configuration import ConfigurationParser
from deployer.helm import HelmDeployer
from deployer.shell import ShellDeployer

DEFAULT_CLUSTER_CONFIG = "config.yaml"


def main():
    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    helm = HelmDeployer(configuration.get(), shell)
    helm.deploy()


if __name__ == '__main__':
    main()