from typing import Any
import yaml


class ConfigurationParser:
    def __init__(self, configuration):
        with open(configuration, 'r') as metadata:
            self.configuration = yaml.safe_load(metadata)

    def validate(self):
        self.validate_istio()
        return

    def validate_istio(self):
        return

    def get(self):
        return self.configuration

    def get_istio_control_plane(self):
        return self.configuration["istio"]["control_plane"]

    def get_istio_gateway(self):
        return self.configuration["istio"]["gateway"]
