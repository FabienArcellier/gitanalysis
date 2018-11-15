from abc import ABCMeta, abstractmethod

class Git:
    __metaclass__ = ABCMeta

    @abstractmethod
    def log(self):
        raise NotImplementedError
