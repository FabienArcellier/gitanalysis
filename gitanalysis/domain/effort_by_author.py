# coding=utf-8

import sys
from io import StringIO

import pandas as pd

pd.set_option('mode.chained_assignment', None)


class EffortByAuthor():

    def __init__(self):
        pass

    def fromChangelog(self, changelog):
        """

        :param changelog:
        :type changelog: str|unicode
        :return:
        :rtype str|unicode
        """
        commits = pd.read_csv(StringIO(changelog))
        commits_by_date_and_author = commits.groupby(['date', 'author']) \
            .agg(len) \
            .reset_index()

        efforts_by_authors = commits_by_date_and_author.groupby(['author']) \
            .agg({'date': len}) \
            .reset_index() \
            .rename(columns={'date': 'effort(days)'})

        efforts_by_authors_csv = efforts_by_authors.to_csv(index=False)
        if sys.version_info < (3, 0):
            efforts_by_authors_csv = efforts_by_authors_csv.decode('utf-8')

        return efforts_by_authors_csv
