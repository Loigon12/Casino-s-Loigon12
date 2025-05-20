import random
import time

# Enumeración para representar los estados del juego
CONTINUA = 0
GANA = 1
PIERDE = 2

# Función para simular el lanzamiento de los dados
def lanzar_dados():
    """Simula el lanzamiento de dos dados con un breve tiempo de espera."""
    print("Lanzando los dados...")
    time.sleep(1)  # He reducido el tiempo de espera para una prueba más rápida

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print(f"El jugador obtiene {dado1} + {dado2} = {suma}")
    time.sleep(0.3) # Espera medio segundo después de mostrar la suma
    return suma

def mostrar_mensaje_aleatorio(saldo_banco):
    """Muestra mensajes aleatorios durante el juego con un breve tiempo de espera."""
    time.sleep(0.3)
    mensaje = random.randint(0, 4)

    if saldo_banco < 300:
        # Mensajes cuando el saldo es bajo
        mensajes_bajo = [
            "Mhm... parece que va a la quiebra.",
            "¿Seguro que quiere seguir apostando? No le queda mucho saldo...",
            "¡Es hora de un golpe de suerte o nunca!",
            "La fortuna favorece a los valientes, ¡pero también arruina a los imprudentes!",
            "¡Está caminando por la cuerda floja financiera!"
        ]
        print(mensajes_bajo[mensaje])
    else:
        # Mensajes generales
        mensajes_generales = [
            "¡Ande! ¡Atrévase!",
            "¡No tenga miedo, ahora es el momento de arriesgarse!",
            "¿Siente la adrenalina? ¡Este es el verdadero juego!",
            "Los dados son sus amigos... ¿o sus enemigos?",
            "¡La fortuna sonríe a los audaces!"
        ]
        print(mensajes_generales[mensaje])
    time.sleep(0.3)

# Funcion principal del juego de Craps
def jugar_craps():
    """Encapsula toda la lógica del juego de craps, incluyendo apuestas y bucle de juego."""
    saldo_banco = 1000   # Inicializar el saldo del banco en $1000
    random.seed(int(time.time()))   # Establecer la semilla para el generador de números aleatorios
    print("----¡Bienvenido al juego de Craps!----")
    print(f"Su saldo inicial es de ${saldo_banco}")
    time.sleep(0.3)

    while True:
        # Solicitar la apuesta al usuario
        while True:
            try:
                apuesta_str = input(f"\nIntroduzca su apuesta (debe ser menor o igual a ${saldo_banco}): ")
                apuesta = int(apuesta_str)
                if apuesta <= 0:
                    print("La apuesta debe ser mayor que cero. Intente de nuevo.")
                    time.sleep(0.1)
                elif apuesta > saldo_banco:
                    print("No tiene suficiente saldo para esa apuesta. Intente con una cantidad menor.")
                    time.sleep(0.1)
                else:
                    break
            except ValueError:
                print("Por favor, introduzca un número entero para la apuesta.")
                time.sleep(0.1)

        print(f"\n¡Comienza el juego con una apuesta de ${apuesta}!\n")
        time.sleep(0.3)

        # Mostrar mensaje de "conversación" aleatorio
        mostrar_mensaje_aleatorio(saldo_banco)

        # Lógica de una ronda de craps
        suma = lanzar_dados()
        estatus_juego = CONTINUA
        punto = 0

        # Determinar el estado del juego para el primer lanzamiento
        if suma == 7 or suma == 11:
            estatus_juego = GANA
        elif suma == 2 or suma == 3 or suma == 12:
            estatus_juego = PIERDE
        else:
            estatus_juego = CONTINUA
            punto = suma
            print(f"Su punto es: {punto}")
            time.sleep(0.5)

        # Posteriores lanzamientos
        while estatus_juego == CONTINUA:
            print("\nSiguiente lanzamiento...")
            time.sleep(0.4)
            suma = lanzar_dados()
            if suma == punto:
                estatus_juego = GANA
            elif suma == 7:
                estatus_juego = PIERDE

        # Actualizar el saldo según el resultado de la ronda
        if estatus_juego == GANA:
            print("El jugador gana")
            saldo_banco += apuesta
            print(f"\n¡Felicidades! Ha ganado ${apuesta}")
        else:
            print("El jugador pierde")
            saldo_banco -= apuesta
            print(f"\nHa perdido ${apuesta}")
        time.sleep(0.3)

        # Mostrar el saldo actualizado
        print(f"Su saldo actual es de ${saldo_banco}")
        time.sleep(0.3)

        # Verificar si se quedó sin saldo
        if saldo_banco == 0:
            print("\nLo siento. ¡Su saldo se agotó!\n")
            break

        # Preguntar si desea seguir jugando
        seguir_jugando = input("\n¿Desea seguir jugando? (s(si)/n(no)): ").lower()
        if seguir_jugando != 's':
            break
        time.sleep(0.1)

    print(f"\n¡Gracias por jugar! Su saldo final es de ${saldo_banco}")

# El main solo ejecuta la función jugar_craps
if __name__ == "__main__":
    jugar_craps()