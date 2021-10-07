from abc import ABC, abstractmethod
from attributes import Attributes


class BaseStatus(ABC):
    NAME = NotImplemented

    def __init__(self):
        pass

    @abstractmethod
    def modify_attrs(self, attrs: Attributes):
        raise NotImplementedError
