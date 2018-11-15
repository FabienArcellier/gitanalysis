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
@click.option('--use-gitlog', is_flag=True, flag_value=True, help='force the usage of git log command')
def changelog(use_gitlog):
    git = GitShell()
    stdin = StdinClick()

    if use_gitlog or not stdin.active():
        git_log_raw = git.log()
    else:
        stdin_content = stdin.read()
        git_log_raw = stdin_content

    if git_log_raw is not None:
        changes = Changelog()
        changelog = changes.from_gitlog(git_log_raw)
        sys.stdout.write(changelog.to_csv(index=False))


cli.add_command(changelog)

if __name__ == '__main__':
    cli()
