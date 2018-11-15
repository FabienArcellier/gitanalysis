import subprocess

from gitanalysis.domain.git import Git


class GitShell(Git):
    def log(self):
        result = subprocess.check_output("git log --pretty=format:'-%h;%an;%ad' --numstat", shell=True)
        return result

