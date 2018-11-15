import subprocess

import sys

from gitanalysis.domain.git import Git


class GitShell(Git):
    def log(self):
        if sys.version_info >= (3, 0):
            output = subprocess.check_output("git log --pretty=format:'-%h;%an;%ad' --numstat", shell=True,
                                             encoding='utf8')
        else:
            output = subprocess.check_output("git log --pretty=format:'-%h;%an;%ad' --numstat", shell=True)
            output = output.decode('utf-8')
        return output
