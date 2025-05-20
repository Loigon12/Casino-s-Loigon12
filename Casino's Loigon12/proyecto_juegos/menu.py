#menu.py
from Juegos.blackJack import juego_blackjack
from Juegos.craps     import jugar_craps
from Juegos.ruleta    import juego_ruleta

def main():
    while True:
        print("|---------------------------|")
        print("---Menu de Juegos de Azar---")
        print("|---------------------------|")
        print("1. BlackJack")
        print("2. Craps")
        print("3. Ruleta")
        print("4. Salir\n")
        opc = input("Opción: ").strip()
        if opc == "1":
            juego_blackjack()
        elif opc == "2":
            jugar_craps()
        elif opc == "3":
            juego_ruleta()
        elif opc =="4":
            print("¡Hasta luego!"); 
            break
        else:
            print("Invalido.\n")

if __name__ == "__main__":
    main()
        

