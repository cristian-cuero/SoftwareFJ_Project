from core.cliente import Cliente
from core.reserva import Reserva
from core.salas import ReservaSala
from core.equipos import AlquilerEquipo
from core.asesoarias import AsesoriaEspecializada
from utils.logger import registrar_log
from utils.excepciones import *


def ejecutar():

    clientes_creados = []

    try:
        # 🔷 LISTA DE CLIENTES (CON LAMBDAS)
        clientes = [
            lambda: Cliente(1, "Jessica", "123", "jessica@gmail.com"),
            lambda: Cliente(2, "", "456", "correo_invalido"),
            lambda: Cliente(3, "Carlos", "789", "carlos@gmail.com"),
            lambda: Cliente(4, "Ana", "", "ana@gmail.com"),
            lambda: Cliente(5, "Juan", "123", "juan@gmail.com"),
        ]

        # 🔷 CREACIÓN DE CLIENTES
        for i, crear_cliente in enumerate(clientes, start=1):
            try:
                cliente = crear_cliente()
                clientes_creados.append(cliente)
                registrar_log(f"Cliente {i} creado: {cliente.mostrar_info()}")
            except ClienteError as e:
                registrar_log(f"ERROR cliente {i}: {e}")

        # 🔷 CREACIÓN DE SERVICIOS
        try:
            sala = ReservaSala("Sala VIP", 100)
            equipo = AlquilerEquipo("Laptop", 50, "Tecnología")
            asesoria = AsesoriaEspecializada("Consultoría", 200)

            registrar_log("Servicios creados correctamente")

        except Exception as e:
            registrar_log(f"ERROR creando servicios: {e}")

        # 🔷 RESERVA VÁLIDA
        try:
            r1 = Reserva(clientes_creados[0], sala, 3)
            r1.confirmar()
            registrar_log("Reserva confirmada correctamente")

            total = r1.procesar_pago()
            registrar_log(f"Pago realizado: {total}")

        except Exception as e:
            registrar_log(f"ERROR en reserva válida: {e}")

        # 🔷 RESERVA INVÁLIDA (duración negativa)
        try:
            r2 = Reserva(clientes_creados[0], sala, -2)
        except ReservaError as e:
            registrar_log(f"ERROR reserva inválida: {e}")

        # 🔷 ERROR EN SERVICIO
        try:
            sala.calcular_costo(0)
        except Exception as e:
            registrar_log(f"ERROR cálculo servicio: {e}")

        # 🔷 USO DE OTROS SERVICIOS
        try:
            total_equipo = equipo.calcular_costo(2, seguro=20)
            registrar_log(f"Pago equipo: {total_equipo}")

            total_asesoria = asesoria.calcular_costo(2, impuesto=50)
            registrar_log(f"Pago asesoría: {total_asesoria}")

        except Exception as e:
            registrar_log(f"ERROR en otros servicios: {e}")

        # 🔷 CANCELACIÓN
        try:
            r1.cancelar()
            registrar_log("Reserva cancelada correctamente")
        except Exception as e:
            registrar_log(f"ERROR al cancelar: {e}")

    except Exception as e:
        registrar_log(f"ERROR crítico del sistema: {e}")

    finally:
        print("Sistema ejecutado sin detenerse ✔")


if __name__ == "__main__":
    ejecutar()