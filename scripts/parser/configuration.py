from typing import Any
import yaml


class ConfigurationParser:
    def __init__(self, configuration):
        with open(configuration, 'r') as metadata:
            self.configuration = yaml.safe_load(metadata)

    def validate(self):
        self.validate_helm()

    def validate_helm(self):
        if "release" not in self.configuration:
            raise ValueError("configuration missing release key")

        for release in self.configuration["release"]:
            if "name" not in release:
                raise ValueError("release missing name")
            if "namespace" not in release:
                raise ValueError(
                    "release {} missing namespace".format(release["name"]))
            if "version" not in release:
                raise ValueError(
                    "release {} missing version".format(release["name"]))
            if "value" not in release:
                raise ValueError(
                    "release {} missing value".format(release["name"]))
            if "chart" not in release:
                raise ValueError(
                    "release {} missing chart configuration".format(release["name"]))
            if "name" not in release["chart"]:
                raise ValueError(
                    "release {} missing chart name".format(release["name"]))
            if "repository" not in release["chart"]:
                raise ValueError(
                    "release {} missing chart repository configuration".format(release["name"]))
            if "name" not in release["chart"]["repository"]:
                raise ValueError(
                    "release {} missing chart repository name".format(release["name"]))
            if "url" not in release["chart"]["repository"]:
                raise ValueError(
                    "release {} missing chart repository url".format(release["name"]))

    def get(self):
        return self.configuration
