class KustomizeDeployer():
    def __init__(self, shell):
        self.shell = shell

    def deploy(self):
        self.shell.execute(["kustomize", "build", "kustomize",
                           "--load_restrictor", "LoadRestrictionsNone", "-o", "rendered.yaml"])
        self.shell.execute(["kubectl", "apply", "-f", "rendered.yaml"])
