

class HelmDeployer():
    def __init__(self, configuration, shell):
        self.configuration = configuration
        self.shell = shell

    def deploy(self):
        for release in self.configuration["release"]:
            self.install_repository(release)

        self.update_repository()

        for release in self.configuration["release"]:
            self.deploy_release(release)

    def install_repository(self, release):
        name = release["chart"]["repository"]["name"]
        url = release["chart"]["repository"]["url"]

        print("\n Adding Helm Repository [{}]({})".format(name, url))
        command = ["helm", "repo", "add", name, url]

        self.shell.execute(command)


    def update_repository(self):
        command = ["helm", "repo", "update"]
        self.shell.execute(command)


    def deploy_release(self, release):
        chart_name = release["chart"]["name"]
        chart_version = release["version"]
        release_name = release["name"]
        release_namespace = release["namespace"]
        release_value = release["value"]

        command = ["helm", "upgrade", "--install",
                  release_name, chart_name,
                  "--namespace", release_namespace,
                  "--version", chart_version,
                  "--values", release_value]
        self.shell.execute(command)
