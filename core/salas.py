from base_servicio import Servicio
from utils.excepciones import ServicioError


class ReservaSala(Servicio):

    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ServicioError("Horas inválidas")

        return (self.costo_base * horas) - descuento

    def mostrar_info(self):
        return f"Sala: {self.nombre}"