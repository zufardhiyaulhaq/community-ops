#!/usr/bin/env python

import os
import sys
import yaml
import click
import subprocess

DEFAULT_CLUSTER_CONFIG="config.yaml"

def get_configuration(filename):
    with open(filename, 'r') as metadata:
        try:
            return yaml.safe_load(metadata)
        except yaml.YAMLError as exception:
            raise err

def execute_command(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while process.poll() is None:
            print(process.stdout.readline().strip().decode("utf-8"))
        print (process.stdout.read().strip().decode("utf-8"))
    except subprocess.CalledProcessError as exc:
        print("[ERROR] Command \"{}\" failed with exit code {}: {}".format(' '.join(command), exc.returncode, exc.output.strip().decode("utf-8")))
        sys.exit(1)
    except Exception as exc:
        print(exc.output)
        raise exc

def install_helm_repository(config):
    if "repository" not in config["chart"]:
        return

    name = config["chart"]["repository"]["name"]
    url = config["chart"]["repository"]["url"]

    print("\n Adding Helm Repository [{}]({})".format(name, url))
    command = ["helm", "repo", "add", name, url]

    execute_command(command)

def update_helm_repository():
    command = ["helm", "repo", "update"]
    execute_command(command)

def apply_helm_release(config):
    chart_name = config["chart"]["name"]
    chart_version = config["version"]
    release_name = config["name"]
    release_namespace = config["namespace"]
    release_value = config["value"]

    command = ["helm", "upgrade", "--install", 
               release_name, chart_name,
               "--namespace", release_namespace,
               "--version", chart_version,
               "--values", release_value]
    print(' '.join(command))
    execute_command(command)

def main():
    cluster_configuration = get_configuration(DEFAULT_CLUSTER_CONFIG)

    print("\nInstalling Helm repository")
    for release in cluster_configuration["release"]:
        install_helm_repository(release)

    print("\nUpdate Helm repository")
    update_helm_repository()

    print("\nApplying Helm release")
    for release in cluster_configuration["release"]:
        apply_helm_release(release)

if __name__ == '__main__':
    main()
