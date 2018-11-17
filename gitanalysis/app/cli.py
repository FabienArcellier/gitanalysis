#!/usr/bin/python
# coding=utf-8
import sys
import click

from gitanalysis.domain.changelog import Changelog
from gitanalysis.infrastructure.git_shell import GitShell
from gitanalysis.infrastructure.stdin_click import StdinClick


@click.group()
def cli():
    pass


@click.command('changelog')
@click.option('--use-git', is_flag=True, flag_value=True, help='force the usage of git on the current directory')
def changelog(use_git):
    git = GitShell()
    stdin = StdinClick()
    changelog_ = Changelog()

    if use_git or not stdin.active():
        git_log_raw = git.log()
    else:
        stdin_content = stdin.read()
        git_log_raw = stdin_content

    if git_log_raw is not None:
        git_changelog = changelog_.fromGitlog(git_log_raw)
        sys.stdout.write(git_changelog)


cli.add_command(changelog)

if __name__ == '__main__':
    cli()
