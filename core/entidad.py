from abc import ABC, abstractmethod
from datetime import datetime


class EntidadBase(ABC):
    """
    Clase abstracta base para representar entidades generales del sistema.
    """

    def __init__(self, id):
        self._id = id
        self._fecha_creacion = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @abstractmethod
    def mostrar_info(self):
        """
        Método abstracto que debe implementarse en las clases hijas.
        """
        pass