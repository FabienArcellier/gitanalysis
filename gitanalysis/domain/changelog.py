from io import StringIO

import pandas as pd

class Changelog(object):
    """
    :see https://www.feststelltaste.de/reading-a-git-log-file-output-with-pandas/
    """

    def from_gitlog(self, gitlog):
        commits = pd.read_csv(StringIO(gitlog), header=None, names=['raw'])

        commit_marker = commits[commits['raw'].str.startswith("-", na=False)]
        commit_info = commit_marker['raw'].str.extract(r"^-(?P<shorthash>.*?);(?P<author>.*?);(?P<date>.*?)$", expand=True)
        commit_info['date'] = pd.to_datetime(commit_info['date'])

        file_stats_marker = commits[~commits.index.isin(commit_info.index)]
        file_stats = file_stats_marker['raw'].str.split("\s+", expand=True)
        file_stats = file_stats.rename(columns={0: "insertions", 1: "deletions", 2: "filename"})
        file_stats['insertions'] = pd.to_numeric(file_stats['insertions'], errors='coerce')
        file_stats['deletions'] = pd.to_numeric(file_stats['deletions'], errors='coerce')

        commit_data = commit_info.reindex(commits.index).fillna(method="ffill")
        commit_data = commit_data[~commit_data.index.isin(commit_info.index)]
        commit_data = commit_data.join(file_stats)
        commit_data.fillna(0)
        return commit_data