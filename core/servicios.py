from core.base import EntidadBase

class Servicio(EntidadBase):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

class ReservaSala(Servicio): # Herencia
    def calcular_costo(self, horas, descuento=0):
        # Polimorfismo y Sobrecarga
        return (self.costo_base * horas) - descuento

    def obtener_detalles(self):
        return f"Servicio: {self.nombre}"
