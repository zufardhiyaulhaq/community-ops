class IstioDeployer():
    def __init__(self, shell, config_file):
        self.shell = shell
        self.config_file = config_file

    # TODO add ability to dryrun the istioctl
    # https://github.com/istio/istio/pull/34634
    def deploy(self, dryrun=False):
        if dryrun == False:
            command = ["istioctl", "upgrade", "-f", self.config_file, "--force", "--skip-confirmation"]
            self.shell.execute(command)
        
    # TODO add ability to diff the manifest
    def diff(self):
        return
