from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, horas, descuento=0):
        return (self.costo_base * horas) - descuento


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, seguro=0):
        return (self.costo_base * dias) + seguro


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, impuesto=0):
        return (self.costo_base * sesiones) + impuesto