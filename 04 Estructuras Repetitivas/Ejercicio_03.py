"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

n1 = int(input("Ingrese el valor del extremo inferior: "))
n2 = int(input("Ingrese el valor del extremo superior: "))
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
