class IstioDeployer():
    def __init__(self, shell, config_file, cluster):
        self.shell = shell
        self.config_file = config_file
        self.cluster = cluster

    def deploy(self, dryrun=False):
        if dryrun == False:
            command = ["istioctl", "install", "-f", self.config_file, "--force", "--skip-confirmation", "--context", self.cluster]
            self.shell.execute(command)
        else:
            command = ["istioctl", "install", "-f", self.config_file, "--force", "--dry-run", "--skip-confirmation", "--context", self.cluster]
            self.shell.execute(command)
        
    def diff(self):
        manifest_generate_command = ["istioctl", "manifest", "generate", "-f", self.config_file, ">", "output.yaml"]
        self.shell.execute(manifest_generate_command)

        diff_command = ["kubectl", "diff", "-f", "output.yaml"]
        self.shell.execute(diff_command)
