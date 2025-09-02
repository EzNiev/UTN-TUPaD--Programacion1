import random

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

numero_random = random.randint(0, 9)
intentos = 0
n = -1
while numero_random != n:
    intentos += 1
    if intentos == 1:
        n = int(input("Intente adivinar el número entre 0 y 9: "))
    else:
        print(f"No es el número {n}!")
        n = int(input("Intente adivinar nuevamente el número entre 0 y 9: "))
print(f"Correcto! El número es {n}! \nTardó {intentos} intentos en adivinarlo.")
if intentos == 1:
    print("Con esa suerte me iría a la quiniela!")
