# Daniel Esteban Guzman Rodriguez 2220241024
# Sebastian Londoño Medina 2220241005
# Armando Antonio Lopez Cuellar 2220241015

import random
import time

# Tiempo de espera para las acciones (en segundos)
TIEMPO_ESPERA = 1

# Función para generar una carta aleatoria (1-13)
def generar_carta():
    time.sleep(TIEMPO_ESPERA * 0.3)  # Pequeña pausa antes de generar
    return random.randint(1, 13)

# Función para calcular el valor de una mano, teniendo en cuenta los ases
def calcular_valor_mano(cartas):
    # Se inicializan en 0 para no tener inconvenientes
    
    total = 0
    ases = 0 
    
    # Primero sumamos todos los valores, contando los ases
    for carta in cartas:
        if carta == 1:   # Es un As
            ases += 1
            total += 11   # Inicialmente consideramos el As como 11
        elif carta >= 11 and carta <= 13:   # J, Q, K
            total += 10
        else:   # Cartas numéricas
            total += carta

    # Si nos pasamos de 21 y tenemos ases, convertimos los ases de 11 a 1 hasta que el total sea <= 21
    while total > 21 and ases > 0:
        total -= 10   # Convertir un As de 11 a 1 (restando 10)
        ases -= 1

    return total

# Función para mostrar el nombre de la carta
def mostrar_carta(carta):
    if carta == 1:
        print("As", end="")
    elif carta == 11:
        print("J", end="")
    elif carta == 12:
        print("Q", end="")
    elif carta == 13:
        print("K", end="")
    else:
        print(carta, end="")
    time.sleep(TIEMPO_ESPERA * 0.5)  # Pausa de 0.5 después de mostrar la carta

# Función para obtener la apuesta del jugador
def obtener_apuesta(saldo):
    while True:
        print(f"\nTu saldo actual es: {saldo}")
        try:
            apuesta = int(input("Ingresa tu apuesta (Apuesta minima de 5): "))
            if apuesta >= 5 and apuesta <= saldo:
                return apuesta
            else:
                print("Apuesta invalida. Ingrese otro monto")
                time.sleep(TIEMPO_ESPERA * 0.3)
        except ValueError:
            print("Por favor, ingresa un número válido")
            time.sleep(TIEMPO_ESPERA * 0.3)

# Función para el turno del jugador con la opción de doble apuesta
def turno_jugador(apuesta, saldo):
    cartas = []

    # Repartir cartas iniciales
    carta1 = generar_carta()
    carta2 = generar_carta()
    cartas.extend([carta1, carta2]) # Para que ambas cartas se guarden en la lista

    # Calcular total inicial
    total = calcular_valor_mano(cartas)

    # Mostrar cartas iniciales
    print("\n--- TURNO DEL JUGADOR ---")
    print("Cartas iniciales: ", end="")
    mostrar_carta(carta1)
    print(" y ", end="")
    mostrar_carta(carta2)
    print(f"\nTotal: {total}")
    time.sleep(TIEMPO_ESPERA * 0.7) #Tiempo de espera de 0.7 despues de mostrar cartas iniciales

    # Opción de doblar apuesta
    if saldo >= (apuesta * 2):
        print("\nDeseas doblar tu apuesta? (Double Down)")
        print("Si eliges doblar, duplicarás tu apuesta actual y recibirás una sola carta adicional")
        print("1. Si, doblar")
        print("0. No, continuar normalmente")
        try:
            opcion_doble = int(input("Elección: "))
            if opcion_doble == 1:
                # Duplicar apuesta
                apuesta *= 2
                print(f"\nApuesta duplicada a {apuesta}")
                time.sleep(TIEMPO_ESPERA * 0.5) #Tiempo de espera despues de aceptar duplicar la apuesta

                # Dar carta
                nueva_carta = generar_carta()
                cartas.append(nueva_carta) #Agregamos un elemento final a la lista [carta1, carta2, nueva_carta]
                print("Carta adicional: ", end="")
                mostrar_carta(nueva_carta)
                print()
                time.sleep(TIEMPO_ESPERA * 0.7) #Tiempo de espera de 0.7 despues de mostrar la nueva carta

                total = calcular_valor_mano(cartas)
                print(f"Total final: {total}")
                time.sleep(TIEMPO_ESPERA * 0.7)

                # No se permiten más cartas después de doblar
                return total, apuesta
        except ValueError:
            print("Entrada inválida, continuando normalmente") #Por si ingresa otro número o letra diferente
            time.sleep(TIEMPO_ESPERA * 0.3)

    # Preguntar si quiere más cartas o se planta
    while total < 21:
        try:
            decision = int(input("\n¿Desea otra carta? (1[Si]/0[No]): "))
            time.sleep(TIEMPO_ESPERA * 0.3)
            if decision == 1:
                nueva_carta = generar_carta()
                cartas.append(nueva_carta)
                print("Nueva carta: ", end="")
                mostrar_carta(nueva_carta)
                print()
                time.sleep(TIEMPO_ESPERA * 0.7)

                total = calcular_valor_mano(cartas)
                print(f"Total actualizado: {total}")
                time.sleep(TIEMPO_ESPERA * 0.7)
            else:
                break   # El jugador se planta
        except ValueError:
            print("Por favor, ingresa 1 para Si o 0 para No")
            time.sleep(TIEMPO_ESPERA * 0.3)

    return total, apuesta

# Función para el turno del dealer
def turno_dealer():
    cartas = []

    # Repartir cartas iniciales
    carta1 = generar_carta()
    carta2 = generar_carta()
    cartas.extend([carta1, carta2])

    # Calcular total inicial
    total = calcular_valor_mano(cartas)

    # Mostrar cartas iniciales
    print("\n--- TURNO DEL DEALER ---")
    print("Cartas iniciales: ", end="")
    mostrar_carta(carta1)
    print(" y ", end="")
    mostrar_carta(carta2)
    print(f"\nTotal: {total}")
    time.sleep(TIEMPO_ESPERA * 0.7)

    # El dealer toma cartas hasta llegar a 17 o más
    while total < 17:
        nueva_carta = generar_carta()
        cartas.append(nueva_carta) #para agregar una nueva carta al final de la lista [carta1, carta2, nueva_carta]
        print("El dealer toma una carta: ", end="")
        mostrar_carta(nueva_carta)
        print()
        time.sleep(TIEMPO_ESPERA * 0.7) #tiempo de espera de 0.7 despues de mostrar las cartas del dealer
        total = calcular_valor_mano(cartas)
        print(f"Total del dealer: {total}")
        time.sleep(TIEMPO_ESPERA * 0.7)

    return total

# Función para actualizar el saldo según el resultado
def actualizar_saldo(saldo, apuesta, resultado):
    if resultado == 1:   # Jugador gana
        return saldo + apuesta
    elif resultado == 2:   # Dealer gana
        return saldo - apuesta
    else:   # Empate
        return saldo

# Función para mostrar el resultado de una ronda
def mostrar_resultado(total_jugador, total_dealer, saldo, apuesta):
    resultado = 0   # 0 = empate, 1 = jugador gana, 2 = dealer gana

    # Mostrar resultado final
    print("\n--- RESULTADO FINAL ---")
    print(f"Total del jugador: {total_jugador}")
    print(f"Total del dealer: {total_dealer}")
    time.sleep(TIEMPO_ESPERA * 0.7)

    # Determinar ganador
    if total_jugador > 21:
        print("\nTe has pasado de 21! El dealer gana")
        resultado = 2
    elif total_dealer > 21:
        print("\nEl dealer se ha pasado de 21! Has ganado!")
        resultado = 1
    elif total_jugador > total_dealer:
        print("\nFelicidades! Has ganado")
        resultado = 1
    elif total_jugador < total_dealer:
        print("\nEl dealer gana")
        resultado = 2
    else:
        print("\nEmpate")
        resultado = 0
    time.sleep(TIEMPO_ESPERA * 0.7)

    # Actualizar saldo
    nuevo_saldo = actualizar_saldo(saldo, apuesta, resultado)

    # Mostrar saldo actualizado
    if resultado == 1:
        print(f"Ganaste {apuesta} unidades")
    elif resultado == 2:
        print(f"Perdiste {apuesta} unidades")
    time.sleep(TIEMPO_ESPERA * 0.5)
    print(f"Tu nuevo saldo es: {nuevo_saldo}")
    time.sleep(TIEMPO_ESPERA * 0.7)
    return nuevo_saldo

# Función principal
def juego_blackjack():
    saldo = 1000   # Saldo inicial
    continuar_jugando = 1

    # Inicializar generador de números aleatorios
    random.seed(time.time()) #Para que genere numeros pseudoaleatorios proporcionando la semilla.

    print("Bienvenido al juego de Blackjack (21)")
    print("-------------------------------------")
    print(f"Comienzas con un saldo de {saldo} unidades")
    time.sleep(TIEMPO_ESPERA * 0.7)

    # Bucle principal del juego (múltiples rondas)
    while continuar_jugando and saldo > 0:
        # Obtener apuesta
        apuesta = obtener_apuesta(saldo)
        time.sleep(TIEMPO_ESPERA * 0.5)

        # Turno del jugador
        total_jugador, apuesta = turno_jugador(apuesta, saldo)

        # Verificar si el jugador se pasó
        if total_jugador > 21:
            print("\nTe has pasado de 21! Dealer gana")
            saldo -= apuesta
            print(f"Perdiste {apuesta} unidades")
            print(f"Tu nuevo saldo es: {saldo}")
            time.sleep(TIEMPO_ESPERA * 0.7)
        else:
            # Turno del dealer
            total_dealer = turno_dealer()

            # Mostrar resultado y actualizar saldo
            saldo = mostrar_resultado(total_jugador, total_dealer, saldo, apuesta)

        # Verificar si el jugador puede seguir jugando
        if saldo <= 0:
            print("\nTe has quedado sin saldo! Fin del juego")
            break

        # Preguntar si desea continuar jugando
        try:
            continuar_jugando = int(input("\nDeseas jugar otra ronda? (1[Si]/0[No]): "))
            time.sleep(TIEMPO_ESPERA * 0.3)
        except ValueError:
            print("Entrada inválida, finalizando el juego")
            continuar_jugando = 0
            time.sleep(TIEMPO_ESPERA * 0.3)

    print(f"\nGracias por jugar. Tu saldo final es: {saldo}")
    time.sleep(TIEMPO_ESPERA * 0.5)

if __name__ == "__main__":
    juego_blackjack()