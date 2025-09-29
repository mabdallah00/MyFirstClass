from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def printProperties(self):
        pass

