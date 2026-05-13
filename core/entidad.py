from abc import ABC, abstractmethod
from datetime import datetime


class EntidadBase(ABC):

    def __init__(self, id):
        self._id = id
        self._fecha_creacion = datetime.now()

    @property
    def id(self):
        return self._id

    @abstractmethod
    def mostrar_info(self):
        pass