import os
import click

from utils import *
from parser.configuration import ConfigurationParser


@click.command()
@click.option("--cluster-name",
              help="Cluster name to read the istio revision from",
              required=True)
def revision(cluster_name):
    os.chdir(DEFAULT_CLUSTERS_DIR + cluster_name)

    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    # Print only the raw value so CI can capture it: $(... istio revision ...)
    click.echo(configuration.get_istio_revision())
