import sys
import subprocess


class ShellDeployer():
    def __init__(self):
        pass

    def execute(self, command, check=True):
        # Capture combined stdout+stderr, wait for the process to finish, and
        # (when check=True) fail the whole run on a non-zero exit code. Without
        # this, helmfile/kubectl/istioctl failures were swallowed and CI stayed
        # green over broken deploys.
        #
        # Pass check=False for commands where a non-zero exit is expected and
        # not an error, e.g. `kubectl diff` returns 1 when differences exist,
        # and `mkdir <dir>` fails when the directory already exists.
        try:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = process.stdout.read().decode("utf-8").strip()
            returncode = process.wait()
        except Exception as exc:
            print("[ERROR] Command \"{}\" could not be executed: {}".format(
                ' '.join(command), exc))
            sys.exit(1)

        if check and returncode != 0:
            if output:
                print(output)
            print("[ERROR] Command \"{}\" failed with exit code {}".format(
                ' '.join(command), returncode))
            sys.exit(1)

        return output
