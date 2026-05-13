from core.entidad import EntidadBase
from utils.excepciones import ClienteError


class Cliente(EntidadBase):

    def __init__(self, id, nombre, documento, correo):
        super().__init__(id)

        if not nombre:
            raise ClienteError("Nombre inválido")

        if not documento:
            raise ClienteError("Documento inválido")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}"