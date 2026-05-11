from core.cliente import Cliente
from core.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from core.reserva import Reserva
from core.logger import registrar_log
from core.excepciones import ClienteError, ReservaError


def ejecutar_sistema():
    clientes = []
    reservas = []

    operaciones = [
        lambda: Cliente("Jessica", "123", "jessica@gmail.com"),
        lambda: Cliente("", "456", "correo_invalido"),
        lambda: Cliente("Carlos", "789", "carlos@gmail.com"),
        lambda: Cliente("Ana", "", "ana@gmail.com"),
        lambda: Cliente("Juan", "123", "Juan@gmail.com"),
    ]

    for i, operacion in enumerate(operaciones, start=1):
        try:
            cliente = operacion()
            clientes.append(cliente)
            print(f"Cliente registrado correctamente: {cliente.obtener_detalles()}")
            registrar_log(f"Operación {i}: Cliente registrado correctamente.")
        except ClienteError as e:
            print(f"Error en cliente: {e}")
            registrar_log(f"Operación {i}: Error en cliente - {e}")

    servicios = [
        ReservaSala("Sala Premium", 100, 25),
        AlquilerEquipo("Proyector", 50),
        AsesoriaEspecializada("Consultoría", 200),
        ReservaSala("Sala Basica", 50, 10)
    ]

    operaciones_reservas = [
        (clientes[0], servicios[0], 3),
        (clientes[0], servicios[3], 2),
        (clientes[1] if len(clientes) > 1 else clientes[0], servicios[1], -2),
        (clientes[0], servicios[2], 2),
        (clientes[0], servicios[0], 0),
        (clientes[0], servicios[1], 5),
        (clientes[0], servicios[2], 1),
    ]

    for j, (cliente, servicio, duracion) in enumerate(operaciones_reservas, start=1):
        try:
            reserva = Reserva(cliente, servicio, duracion)
            reserva.confirmar()
           
           # Verificamos si el servicio es tu clase para aplicar la sobrecarga (VIP)
            if isinstance(servicio, ReservaSala):
                # Aplicamos descuento VIP si el cliente es Juan (por ejemplo)
                soy_vip = "Juan" in cliente.obtener_detalles()
                costo = servicio.calcular_costo(duracion, es_vip=soy_vip)               
            else:

                costo = reserva.procesar_pago()

            print(f"Reserva confirmada para {cliente.obtener_detalles()}")
            print(f"Servicio: {servicio.nombre} | Costo: {costo}")
            reservas.append(reserva)

            registrar_log(f"Reserva {j}: Confirmada correctamente.")
        except ReservaError as e:
            print(f"Error en reserva: {e}")
            registrar_log(f"Reserva {j}: Error - {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            registrar_log(f"Reserva {j}: Error inesperado - {e}")
        finally:
            print("Operación procesada.\n")

    print("Sistema ejecutado correctamente sin detenerse.")


if __name__ == "__main__":
    try:
        ejecutar_sistema()
    except Exception as e:
        registrar_log(f"Error crítico del sistema: {e}")
        print("Se produjo un error crítico, pero fue registrado.")