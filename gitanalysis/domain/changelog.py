# coding=utf-8
# pylint: disable=import-error

import sys
from io import StringIO
import re

import pandas as pd

pd.set_option('mode.chained_assignment', None)


class Changelog:
    """
    :var date_format: datetime format - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    :type date_format: str


    :see https://www.feststelltaste.de/reading-a-git-log-file-output-with-pandas/
    """

    def __init__(self, date_format=None):
        self.date_format = date_format

    def fromGitlog(self, gitlog):
        """
        :param gitlog: log reprentation from `git log --pretty=format:'-%h;%an;%ad' --numstat`
        :type gitlog: str

        :rtype: str|unicode
        :return: dateframe from git log injected information
        """
        commits = pd.read_csv(StringIO(gitlog), header=None, names=['raw'])

        commit_marker = commits[commits['raw'].str.startswith("-", na=False)]
        commit_info = commit_marker['raw'].str.extract(
            r"^--(?P<shorthash>.*?)--(?P<date>.*?)--(?P<author>.*?)$",
            expand=True
        )

        commit_info['date'] = pd.to_datetime(commit_info['date'])

        file_stats_marker = commits[~commits.index.isin(commit_info.index)]
        file_stats_marker["insertions"] = file_stats_marker['raw'].apply(insertions)
        file_stats_marker["deletions"] = file_stats_marker['raw'].apply(deletions)
        file_stats_marker["filename"] = file_stats_marker['raw'].apply(filename)
        file_stats = file_stats_marker[["insertions", "deletions", "filename"]]
        file_stats['insertions'] = pd.to_numeric(file_stats['insertions'], errors='coerce')
        file_stats['deletions'] = pd.to_numeric(file_stats['deletions'], errors='coerce')

        commit_data = commit_info.reindex(commits.index).fillna(method="ffill")
        commit_data = commit_data[~commit_data.index.isin(commit_info.index)]
        commit_data = commit_data.join(file_stats)
        commit_data.fillna(0)

        changelog = commit_data.to_csv(index=False, date_format=self.date_format)
        if sys.version_info < (3, 0):
            changelog = changelog.decode('utf-8')

        return changelog


def insertions(raw_line):
    return re.split(r"\s+", raw_line)[0]


def deletions(raw_line):
    return re.split(r"\s+", raw_line)[1]


def filename(raw_line):
    return " ".join(re.split(r"\s+", raw_line)[2:])
