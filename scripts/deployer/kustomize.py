class KustomizeDeployer():
    def __init__(self, shell, cluster):
        self.shell = shell
        self.cluster = cluster

    def deploy(self, dryrun=False):
        render_command = ["kustomize", "build", "kustomize", "--load_restrictor", "LoadRestrictionsNone", "-o", "kustomized-rendered.yaml"]
        apply_command = ["kubectl", "apply", "-f", "kustomized-rendered.yaml", "--context", self.cluster]

        if dryrun:
            apply_command.extend(["--dry-run=server"])
            
        output = self.shell.execute(render_command)
        print(output)

        output = self.shell.execute(apply_command)
        print(output)

    def diff(self):
        render_command = ["kustomize", "build", "kustomize", "--load_restrictor", "LoadRestrictionsNone", "-o", "kustomized-rendered.yaml"]
        output = self.shell.execute(render_command)

        create_dir_command = ["mkdir", "kustomized-rendered-dir"]
        self.shell.execute(create_dir_command)

        split_manifest_command = ["kubectl-slice", "-f", "kustomized-rendered.yaml", "-o", "kustomized-rendered-dir"]
        self.shell.execute(split_manifest_command)

        diff_command = ["kubectl", "diff", "-f", "kustomized-rendered-dir", "--context", self.cluster]
        output = self.shell.execute(diff_command)
        print(output)

        return
