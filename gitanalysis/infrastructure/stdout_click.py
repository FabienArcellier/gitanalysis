from __future__ import unicode_literals

import codecs
import sys

from gitanalysis.domain.stdout import Stdout


class StdoutClick(Stdout):
    def write(self, content):
        if sys.version_info < (3, 0):
            std_out = codecs.getwriter('utf8')(sys.stdout)
        else:
            std_out = sys.stdout

        std_out.write(content)
