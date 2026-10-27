from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass
class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok
    def obwod(self):
        return 4 * self.bok
