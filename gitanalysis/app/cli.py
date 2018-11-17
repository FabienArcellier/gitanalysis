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


@click.command('changelog', help='export a csv changelog from git log')
@click.option('--use-git', is_flag=True, flag_value=True, help='force the usage of git on the current directory')
@click.option('--date_format',
              default=None,
              help='date format - ref : https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior')
def changelog(use_git, date_format):
    git = GitShell()
    stdin = StdinClick()
    changelog_ = Changelog(date_format=date_format)

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
