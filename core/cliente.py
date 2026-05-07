from core.base import EntidadBase
from core.excepciones import ClienteError

class Cliente(EntidadBase):
    def __init__(self, nombre, documento, correo):
        if not nombre:
            raise ClienteError("Nombre inválido")
        if not documento:
            raise ClienteError("Documento inválido")
        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    def obtener_detalles(self):
        return f"Cliente: {self.__nombre}, Documento: {self.__documento}, Correo: {self.__correo}"