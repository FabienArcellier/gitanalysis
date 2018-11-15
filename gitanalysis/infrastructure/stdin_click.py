import click

from gitanalysis.domain.stdin import Stdin


class StdinClick(Stdin):
    def active(self):
        stdin = click.get_text_stream('stdin')
        active = not stdin.isatty()
        return active

    def read(self):
        stdin = click.get_text_stream('stdin')
        if not stdin.isatty():
            stdin_content = stdin.read()
        else:
            stdin_content = None

        return stdin_content
