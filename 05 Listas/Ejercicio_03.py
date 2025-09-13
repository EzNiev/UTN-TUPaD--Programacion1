"""
3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista
"""

import random

lista, pares, impares = [], [], []

for i in range(15):
    lista.append(random.randint(1, 100))

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print("Lista de números pares:")
for i in range(len(pares)):
    print(f"- {pares[i]}")
print(f"Total pares: {len(pares)}")

print("Lista de números impares:")
for i in range(len(impares)):
    print(f"- {impares[i]}")
print(f"Total impares: {len(impares)}")
