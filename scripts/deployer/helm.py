class HelmDeployer():
    def __init__(self, shell, cluster):
        self.shell = shell
        self.cluster = cluster


    # TODO add ability to dryrun the helm release
    def deploy(self, dryrun=False):
        if dryrun == False:
            command = ["helmfile", "--kube-context", self.cluster, "sync"]
            output = self.shell.execute(command)
            print(output)

    def diff(self):
        command = ["helmfile", "--kube-context", self.cluster, "diff", "--suppress-secrets"]
        output = self.shell.execute(command)
        print(output)
