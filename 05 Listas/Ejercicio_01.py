import random

"""
1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
"""

# Genero una lista con 10 numeros enteros, rango de 1 a 10 incluidos los extremos
notas = []
mas_alta, mas_baja = 0, 10
for i in range(10):
    notas.append(random.randint(1, 10))

# Muestro la lista mientras proceso cual es mas alta y mas baja:
for i in range(len(notas)):
    print(f"Nota {i+1}: {notas[i]}")
    if notas[i] < mas_baja:
        mas_baja = notas[i]
    if notas[i] > mas_alta:
        mas_alta = notas[i]

# imprimo la mas alta y la mas baja
print(f"Nota más alta: {mas_alta} \n"
      f"Nota más baja: {mas_baja}\n")

