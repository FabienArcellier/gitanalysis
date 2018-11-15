#!/usr/bin/python
# coding=utf-8
import sys
import click

from gitanalysis.domain.changelog import Changelog
from gitanalysis.infrastructure.git_shell import GitShell

@click.group()
def cli():
    pass


@click.command('changelog')
def changelog():
    stdin = click.get_text_stream('stdin')
    git = GitShell()

    stdin_content = stdin.read()
    if stdin_content != '' and stdin_content is not None:
        git_log_raw = stdin_content
    else:
        git_log_raw = git.log()

    if git_log_raw is not None:
        changes = Changelog()
        changelog = changes.from_gitlog(git_log_raw)
        sys.stdout.write(changelog.to_csv(index=False))


cli.add_command(changelog)

if __name__ == '__main__':
    cli()
