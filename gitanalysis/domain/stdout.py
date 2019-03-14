from abc import ABCMeta, abstractmethod


class Stdout:
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, content):
        pass
