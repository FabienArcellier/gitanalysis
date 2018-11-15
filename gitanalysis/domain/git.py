from abc import ABCMeta, abstractmethod

class Git(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def log(self):
        raise NotImplementedError