from abc import ABCMeta, abstractmethod

class Stdin(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def active(self):
        raise NotImplementedError