# pylint: disable=import-error

from io import StringIO
import re

import pandas as pd
pd.set_option('mode.chained_assignment', None)


class Changelog:
    """
    :see https://www.feststelltaste.de/reading-a-git-log-file-output-with-pandas/
    """

    def fromGitlog(self, gitlog):
        commits = pd.read_csv(StringIO(gitlog), header=None, names=['raw'])

        commit_marker = commits[commits['raw'].str.startswith("-", na=False)]
        commit_info = commit_marker['raw'].str.extract(
            r"^-(?P<shorthash>.*?);(?P<author>.*?);(?P<date>.*?)$",
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
        return commit_data

def insertions(raw_line):
    return re.split(r"\s+", raw_line)[0]

def deletions(raw_line):
    return re.split(r"\s+", raw_line)[1]

def filename(raw_line):
    return " ".join(re.split(r"\s+", raw_line)[2:])
