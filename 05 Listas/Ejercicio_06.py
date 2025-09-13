"""
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero)
"""

import random

lista = []
for i in range(7):
    lista.append(random.randint(0, 100))
print(lista)

# Ya generada la lista procedo a intercambiar los elementos una posicion a la derecha
auxiliar = []
for i in range(len(lista)):
    auxiliar.append(lista[i - 1])
lista = auxiliar
print(lista)
