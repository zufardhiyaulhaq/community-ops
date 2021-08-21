class HelmDeployer():
    def __init__(self, shell, cluster):
        self.shell = shell
        self.cluster = cluster


    # TODO add ability to dryrun the helm release
    def deploy(self, dryrun=False):
        if dryrun == False:
            command = ["helmfile", "--kube-context", self.cluster, "sync"]
            self.shell.execute(command)

    def diff(self):
        command = ["helmfile", "--kube-context", self.cluster, "diff", "--suppress-secrets"]
        self.shell.execute(command)
