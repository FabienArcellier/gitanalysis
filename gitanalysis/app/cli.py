#!/usr/bin/python
# coding=utf-8

import click

from gitanalysis.domain.changelog import Changelog
from gitanalysis.domain.effort_by_author import EffortByAuthor
from gitanalysis.infrastructure.git_shell import GitShell
from gitanalysis.infrastructure.stdin_click import StdinClick
from gitanalysis.infrastructure.stdout_click import StdoutClick


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
    stdout = StdoutClick()

    if use_git or not stdin.active():
        git_log_raw = git.log()
    else:
        stdin_content = stdin.read()
        git_log_raw = stdin_content

    if git_log_raw is not None:
        git_changelog = changelog_.fromGitlog(git_log_raw)
        stdout.write(git_changelog)


@click.command('effort_by_author', help='export a csv that list the number of days an author has commit code')
@click.option('--use-git', is_flag=True, flag_value=True, help='force the usage of git on the current directory')
def effort_by_author(use_git):
    git = GitShell()
    stdin = StdinClick()
    stdout = StdoutClick()
    changelog_ = Changelog()
    _effort_by_author = EffortByAuthor()

    if use_git or not stdin.active():
        git_log_raw = git.log()
    else:
        stdin_content = stdin.read()
        git_log_raw = stdin_content

    if git_log_raw is not None:
        git_changelog = changelog_.fromGitlog(git_log_raw)
        effort_log = _effort_by_author.fromChangelog(git_changelog)
        stdout.write(effort_log)


cli.add_command(changelog)
cli.add_command(effort_by_author)

if __name__ == '__main__':
    cli()
