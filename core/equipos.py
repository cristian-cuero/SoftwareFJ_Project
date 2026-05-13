from core.base_servicio import Servicio
from utils.excepciones import ServicioError


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, tipo):
        super().__init__(nombre, costo_base)
        self.__tipo = tipo

    def calcular_costo(self, dias, seguro=0):
        if dias <= 0:
            raise ServicioError("Días inválidos")

        return (self.costo_base * dias) + seguro

    def mostrar_info(self):
        return f"Equipo: {self.nombre}"