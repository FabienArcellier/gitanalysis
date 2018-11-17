# coding=utf-8


import io
import os
import unittest

from click.testing import CliRunner
from gitanalysis.app.cli import cli, changelog
from gitanalysis_tests.acceptances.fixtures import clone_template


class CliTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_changelog_should_read_input_from_piped_file_by_default(self):
        # Assign
        with clone_template('git-log-extract-1') as git_log_extract_directory:
            with io.open(os.path.join(git_log_extract_directory, 'gitlog.txt')) as f:
                runner = CliRunner()

                # Acts
                result = runner.invoke(cli, ['changelog'], input=f.read())

                # Assert
                self.assertEqual(result.exit_code, 0, msg=result.exception)
                first_line = result.output.split('\n')[0]
                second_line = result.output.split('\n')[1]
                self.assertEqual('shorthash,author,date,insertions,deletions,filename', first_line)
                self.assertEqual('79e6be4,Fabien Arcellier,2018-07-23 11:37:45,2,2,.env.dist', second_line)

    def test_changelog_should_run_git_log_on_working_directory_when_no_pipe_as_input(self):
        # Assign
        runner = CliRunner()

        # Acts
        result = runner.invoke(cli, ['changelog', '--use-git'])

        # Assert
        self.assertEqual(result.exit_code, 0, msg=result.output)
        first_line = result.output.split('\n')[0]
        self.assertEqual('shorthash,author,date,insertions,deletions,filename', first_line)