import sys
import subprocess


class ShellDeployer():
    def __init__(self, manifest_dir):
        self.manifest_dir = manifest_dir

    def deploy(self, dryrun=False):
        command = ["kubectl", "apply", "-f", self.manifest_dir, "-R"]

        if dryrun:
            command.extend(["--dry-run=server"])
        self.execute(command)

    def execute(self, command):
        try:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(process.stdout.read().strip().decode("utf-8"))
        except subprocess.CalledProcessError as exc:
            print("[ERROR] Command \"{}\" failed with exit code {}: {}".format(
                ' '.join(command), exc.returncode, exc.output.strip().decode("utf-8")))
            sys.exit(1)
        except Exception as exc:
            print(exc.output)
            raise exc

    def execute_shell(self, command):
        try:
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(process.stdout.read().strip().decode("utf-8"))
        except subprocess.CalledProcessError as exc:
            print("[ERROR] Command \"{}\" failed with exit code {}: {}".format(
                ' '.join(command), exc.returncode, exc.output.strip().decode("utf-8")))
            sys.exit(1)
        except Exception as exc:
            print(exc.output)
            raise exc
