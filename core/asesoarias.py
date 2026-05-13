from base_servicio import Servicio
from utils.excepciones import ServicioError


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, sesiones, impuesto=0):
        if sesiones <= 0:
            raise ServicioError("Sesiones inválidas")

        return (self.costo_base * sesiones) + impuesto

    def mostrar_info(self):
        return f"Asesoría: {self.nombre}"