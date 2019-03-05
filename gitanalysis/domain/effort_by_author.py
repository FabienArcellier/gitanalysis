from io import StringIO

import pandas as pd

pd.set_option('mode.chained_assignment', None)


class EffortByAuthor():

    def __init__(self):
        pass

    def fromChangelog(self, changelog):
        commits = pd.read_csv(StringIO(gitlog), header=None, names=['raw'])
        return "author,effort(days)\ntt"
