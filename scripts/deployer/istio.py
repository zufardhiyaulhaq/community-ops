class IstioDeployer():
    def __init__(self, shell, config_file, cluster):
        self.shell = shell
        self.config_file = config_file
        self.cluster = cluster

    def deploy(self, dryrun=False):
        command = ["istioctl", "install", "-f", self.config_file, "--force", "--skip-confirmation", "--context", self.cluster]

        if dryrun:
            command.extend(["--dry-run"])

        output = self.shell.execute(command)
        print(output)
        
    def diff(self):
        generate_manifest_command = ["istioctl", "manifest", "generate", "-f", self.config_file]
        output = self.shell.execute(generate_manifest_command)

        text_file = open("output.yaml", "w")
        n = text_file.write(output)
        text_file.close()

        diff_command = ["kubectl", "diff", "-f", "output.yaml"]
        output = self.shell.execute(diff_command)
        print(output)

