import unittest

from gitanalysis.domain.changelog import Changelog


class TestChangelog(unittest.TestCase):

    def test_fromGitlog_should_transform_git_log_into_changelog(self):
        # Assign
        gitlog = u"""--79e6be4--2019-02-14--Fabien Arcellier
2       2       .env.dist
1       1       VERSION.in
        """
        changelog_handler = Changelog()

        # Acts
        changelog = changelog_handler.fromGitlog(gitlog)

        changelog_lines = changelog.split('\n')
        self.assertEqual(4, len(changelog_lines))

    def test_fromGitlog_should_change_the_commit_date_into_a_format_compliant_with_excel(self):
        # Assign
        gitlog = u"""--79e6be4--2018-07-23--Fabien Arcellier
2       2       .env.dist
1       1       VERSION.in
        """
        changelog_handler = Changelog()

        # Acts
        changelog = changelog_handler.fromGitlog(gitlog)

        # Assert
        changelog_lines = changelog.split('\n')
        changelog_line_2 = changelog_lines[1].split(',')
        self.assertEqual(changelog_line_2[1], '2018-07-23')

    def test_date_format_should_change_the_output_date_format_into_the_changelog(self):
        # Assign
        gitlog = u"""--79e6be4--2018-07-23--Fabien Arcellier
2       2       .env.dist
1       1       VERSION.in
                """
        changelog_handler = Changelog(date_format="%d/%m/%Y %H:%M")

        # Acts
        changelog = changelog_handler.fromGitlog(gitlog)

        # Assert
        changelog_lines = changelog.split('\n')
        changelog_line_2 = changelog_lines[1].split(',')
        self.assertEqual(changelog_line_2[1], '23/07/2018 00:00')