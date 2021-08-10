from typing import Any
import yaml


class ConfigurationParser:
    def __init__(self, configuration):
        with open(configuration, 'r') as metadata:
            self.configuration = yaml.safe_load(metadata)

    def validate(self):
        return

    def get(self):
        return self.configuration
