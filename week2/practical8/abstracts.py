from abc import ABC, abstractmethod


class AbstractShape(ABC):

    @abstractmethod
    def __contains__(self):
        pass


class AbstractCircle(ABC):
    @abstractmethod
    def radius(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def __contains__(self):
        pass
