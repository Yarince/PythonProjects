from abc import ABCMeta, abstractmethod


class ICalculator:
    """Calculator interface"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, var): raise NotImplementedError

    @abstractmethod
    def multiply(self, var): raise NotImplementedError

    @abstractmethod
    def pow(self, var): raise NotImplementedError

