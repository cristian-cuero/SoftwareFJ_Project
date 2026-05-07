from abc import ABC, abstractmethod

class EntidadBase(ABC):
    @abstractmethod
    def obtener_detalles(self):
        pass