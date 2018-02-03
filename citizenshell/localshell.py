import os
import subprocess

from shellresult import ShellResult


class LocalShell:

    def __init__(self, shell="/bin/bash"):
        self._env = os.environ
        self._shell = shell

    def __call__(self, script):
        shell_process = subprocess.Popen(self._shell, shell=False, env=self._env,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
        (out, err) = shell_process.communicate(script)
        return ShellResult(out.strip(), err.strip(), shell_process.returncode)