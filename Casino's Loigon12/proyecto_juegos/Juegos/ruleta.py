# Daniel Esteban Guzman Rodriguez 2220241024
# Sebastian Londoño Medina 2220241005
# Armando Antonio Lopez Cuellar 2220241015

import random
import time

def crear_ruleta(numeros_rojos, numeros_negros):
    """Crea la ruleta con números rojos y negros."""
    ruleta_local = [('verde', 0)]  # Inicializa la ruleta con el número 0 y color verde.
    for numero in numeros_rojos:
        ruleta_local.append(('rojo', numero))  # Agrega cada número rojo a la ruleta como una tupla ('rojo', numero).
    for numero in numeros_negros:
        ruleta_local.append(('negro', numero)) # Agrega cada número negro a la ruleta como una tupla ('negro', numero).
    return ruleta_local

def simular_giro(ruleta_local):
    """Simula el giro de la ruleta."""

    print("\nLa ruleta está girando...\n")
    for _ in range(15):  # Simula la desaceleración de la ruleta imprimiendo '🔴⚫🟢' varias veces.
        print("🔴⚫🟢", end="", flush=True)
        time.sleep(0.2)    # Reduce un poco la pausa para un giro más fluido.
    print("\n")
    resultado_indice = random.randint(0, len(ruleta_local) - 1)
    return ruleta_local[resultado_indice]


def determinar_ganador(resultado, apuesta_numero, apuesta_color):
    """Determina si la apuesta del usuario gana."""
    color_resultado, numero_resultado = resultado
    gano_numero = (apuesta_numero is not None and apuesta_numero == numero_resultado)
    gano_color = (apuesta_color is not None and apuesta_color.lower() == color_resultado)
    return gano_numero, gano_color

# Variables globales para la ruleta (se inicializarán dentro de juego_ruleta)
numeros_rojos_global = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
numeros_negros_global = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def juego_ruleta():
    """Permite al usuario jugar rondas de la ruleta hasta que se quede sin saldo o decida parar."""
    global saldo_global, ruleta_global
    saldo_global = 100
    ruleta_global = crear_ruleta(numeros_rojos_global, numeros_negros_global)

    print("-----¡Bienvenido a la Ruleta de Casino!-----\n")

    while saldo_global > 0:  # Bucle principal del juego que continúa mientras el jugador tenga saldo.
        print(f"\nSu saldo actual es: ${saldo_global}")
        while True:  # Bucle para obtener una apuesta válida.
            try:
                apuesta_cantidad = float(input("Ingrese su apuesta: $"))
                if apuesta_cantidad <= 0 or apuesta_cantidad > saldo_global:
                    print("\nApuesta inválida. Debe ser mayor que 0 y no exceder su saldo.")
                else:
                    break  # Sale del bucle si la apuesta es válida.
            except ValueError:
                print("\nPor favor, ingrese un número válido para la apuesta.")

        apuesta_numero = None  # Inicializa la apuesta al número como None.
        apuesta_color = None   # Inicializa la apuesta al color como None.

        while True:  # Bucle para obtener el tipo de apuesta (número o color).
            tipo_apuesta = input("\n¿Apostará a un número (n), a un color (c) o a ambos (a)? (dejar en blanco para no apostar): ").lower()
            if tipo_apuesta == 'n':
                try:
                    numero = int(input("\nIngrese el número al que desea apostar (0-36): "))
                    if 0 <= numero <= 36:
                        apuesta_numero = numero  # Guarda el número apostado.
                        break  # Sale del bucle si el número es válido.
                    else:
                        print("\nNúmero inválido. Debe estar entre 0 y 36.")
                except ValueError:
                    print("\nPor favor, ingrese un número entero.")
            elif tipo_apuesta == 'c':
                color = input("\nIngrese el color al que desea apostar (rojo o negro): ").lower()
                if color in ['rojo', 'negro']:
                    apuesta_color = color  # Guarda el color apostado.
                    break  # Sale del bucle si el color es válido.
                else:
                    print("Color inválido. Debe ser rojo o negro.")
            elif tipo_apuesta == 'a':
                try:
                    numero = int(input("\nIngrese el número al que desea apostar (0-36): "))
                    if 0 <= numero <= 36:
                        apuesta_numero = numero  # Guarda el número apostado.
                    else:
                        print("\nNúmero inválido. Debe estar entre 0 y 36.")
                        continue
                    color = input("\nIngrese el color al que desea apostar (rojo o negro): ").lower()
                    if color in ['rojo', 'negro']:
                        apuesta_color = color  # Guarda el color apostado.
                        break # Sale del bucle si ambos son válidos
                    else:
                        print("Color inválido. Debe ser rojo o negro.")
                except ValueError:
                    print("\nPor favor, ingrese un número entero.")
            elif tipo_apuesta == '':
                break  # Sale del bucle si el usuario no quiere apostar a un número o color.
            else:
                print("Opción inválida. Por favor, ingrese 'n', 'c', 'a' o deje en blanco.")

        resultado = simular_giro(ruleta_global)  # Simula el giro de la ruleta.
        print(f"La ruleta se detiene en: {resultado}")

        gano_numero, gano_color = determinar_ganador(resultado, apuesta_numero, apuesta_color)  # Determina si la apuesta ganó.
        ganancia = 0  # Inicializa la ganancia en 0.

        if gano_numero:
            if apuesta_numero == 0:
                ganancia += apuesta_cantidad * 35    # Pago típico para acertar el 0 es de 35 a 1.
            else:
                ganancia += apuesta_cantidad * 35    # Pago típico para acertar un número es de 35 a 1.

        if gano_color:
            ganancia += apuesta_cantidad * 1     # Pago típico para acertar el color es de 1 a 1.

        if ganancia > 0:
            print(f"¡Felicidades! Ha ganado ${ganancia}")
            saldo_global += ganancia # Actualiza el saldo si ganó.
        else:
            print("Lo siento, ha perdido su apuesta.")
            saldo_global -= apuesta_cantidad  # Resta la apuesta del saldo si perdió.

        if saldo_global <= 0:
            print("¡Se ha quedado sin fondos!\n")
            break  # Sale del bucle si el saldo llega a 0 o menos.

        jugar_otra = input("¿Desea jugar otra ronda? (s/n): ").lower()  # Pregunta si el jugador quiere jugar otra ronda.
        if jugar_otra != 's':
            break  # Sale del bucle si el jugador no quiere jugar otra ronda.

    print("Gracias por jugar.")  # Mensaje de despedida al final del juego.

if __name__ == "__main__":
    juego_ruleta()