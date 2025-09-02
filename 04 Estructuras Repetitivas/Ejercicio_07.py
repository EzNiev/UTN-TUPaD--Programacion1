"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

n1 = 0
n2 = int(input("Ingrese un número entero positivo: "))
if n1 < n2:
    acumulador = 0
    for i in range(n1 + 1, n2):
        print(f"Sumando: {acumulador} + {i} = {acumulador + i}")
        acumulador += i
    print(
        f"Suma de todos los números enteros comprendidos entre {n1} y {n2} es igual a: {acumulador}"
    )
else:
    print("Ingreso valores inválidos.")
