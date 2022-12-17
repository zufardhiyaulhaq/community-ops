class KustomizeDeployer():
    def __init__(self, shell, cluster):
        self.shell = shell
        self.cluster = cluster

    def deploy(self, dryrun=False):
        render_command = ["kustomize", "build", "kustomize", "--load_restrictor", "LoadRestrictionsNone", "-o", "rendered.yaml"]
        apply_command = ["kubectl", "apply", "-f", "rendered.yaml", "--context", self.cluster]

        if dryrun:
            apply_command.extend(["--dry-run=server"])
            
        output = self.shell.execute(render_command)
        print(output)

        output = self.shell.execute(apply_command)
        print(output)

    # TODO add ability to diff the manifest
    def diff(self):
        return
