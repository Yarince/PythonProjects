from abc import ABCMeta, abstractmethod


class ICalculator:
    """Calculator interface"""
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def add(var): raise NotImplementedError

    @staticmethod
    @abstractmethod
    def multiply(var): raise NotImplementedError

    @staticmethod
    @abstractmethod
    def pow(var): raise NotImplementedError
