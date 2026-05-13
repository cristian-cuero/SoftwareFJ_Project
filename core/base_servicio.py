from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, costo_base):
        self._nombre = nombre
        self._costo_base = costo_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass