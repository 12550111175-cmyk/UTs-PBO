from abc import ABC, abstractmethod

class Laporan(ABC):
    @abstractmethod
    def generate(self):
        pass