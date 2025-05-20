## Sala de Juegos en Python
- Este proyecto implementa una sala de juegos interactiva en consola que incluye cuatro juegos clásicos de casino y azar.

## Juegos disponibles

2. Blackjack: El clásico juego de cartas donde debes acercarte lo más posible a 21 sin pasarte.
3. Craps: Juego de dados donde se apuesta al resultado de los lanzamientos.
4. Ruleta: Versión simplificada de la ruleta de casino con varias opciones de apuesta.

## Requisitos
- Python 3.8+

## Estructura
proyecto_juegos/
├── Juegos/
│   ├── adivina.py
│   ├── blackjack.py
│   ├── craps.py
│   └── ruleta.py
├── menu.py
└── README.md

## Cómo jugar
- Ejecuta el archivo principal:

python menu.py

- Sigue las instrucciones en pantalla para navegar por el menú y seleccionar el juego que deseas jugar.

## Reglas de los juegos

# Blackjack

- Tu objetivo es conseguir una mano con un valor más cercano a 21 que la del dealer, sin pasarte.
Las cartas numéricas valen su valor nominal, las figuras (J, Q, K) valen 10.
Puedes pedir cartas adicionales o plantarte en cualquier momento.
También tienes la opción de doblar tu apuesta.

# Craps

- En el primer lanzamiento, ganas si obtienes 7 u 11, y pierdes si obtienes 2, 3 o 12.
Si obtienes cualquier otro número, ese se convierte en tu "punto".
Debes seguir lanzando hasta obtener tu punto (ganas) o un 7 (pierdes).

# Ruleta

- Puedes realizar diferentes tipos de apuestas:

1. Pleno: Apostar a un solo número (paga 36 a 1)
2. Color: Rojo o negro (paga 1 a 1)
3. Par/Impar: Números pares o impares (paga 1 a 1)
4. 1-18/19-36: Primera o segunda mitad (paga 1 a 1)
5. Docena: Grupos de doce números (paga 2 a 1)