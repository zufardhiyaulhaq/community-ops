class HelmDeployer():
    def __init__(self, shell):
        self.shell = shell

    # TODO add ability to dryrun the helm release
    def deploy(self, dryrun=False):
        if dryrun == False:
            command = ["helmfile", "sync"]
            self.shell.execute(command)

    def diff(self):
        command = ["helmfile", "diff", "--suppress-secrets"]
        self.shell.execute(command)
