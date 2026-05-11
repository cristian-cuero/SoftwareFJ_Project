from abc import ABC, abstractmethod
import logging


logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass


class ReservaSala(Servicio):
    def __init__(self, nombre, costo_base, capacidad=10): # Capacidad por defecto para evitar errores
        super().__init__(nombre, costo_base)
        self.__capacidad = capacidad # ENCAPSULAMIENTO

    @property
    def capacidad(self):
        return self.__capacidad

    def calcular_costo(self, horas, es_vip=False):
        # POLIMORFISMO Y SOBRECARGA REAL
        try:
            if horas <= 0:
                logging.info(f"La duración debe ser mayor a cero: {self.nombre} ")
                raise ValueError("La duración debe ser mayor a cero")
            
            total = self.costo_base * horas
            
            # Lógica de negocio (Recargo por capacidad)
            if self.capacidad > 20:
                total += 100 
            
            # Sobrecarga (Descuento VIP)
            if es_vip:
                total *= 0.85
                
            logging.info(f"Calculo exitoso para Sala: {self.nombre} | Total: {total} | Capacidad: {self.capacidad}")
            return total
        except ValueError as e:
            logging.error(f"Error en Sala '{self.nombre}': {str(e)}")
            raise e

    def obtener_detalles(self):
        return f"SALA: {self.nombre} | Capacidad: {self.capacidad} pers."


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, seguro=0):
        return (self.costo_base * dias) + seguro


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, impuesto=0):
        return (self.costo_base * sesiones) + impuesto