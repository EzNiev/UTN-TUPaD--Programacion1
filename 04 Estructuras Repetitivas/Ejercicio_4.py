"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

n = int(input("Ingrese un número: "))
acumulador = 0
while n != 0:
    print(f"Sumando {acumulador} + {n} = {acumulador + n}.")
    acumulador += n
    print("-" * 20)
    n = int(input("Ingrese otro número (0 para salir): "))
print("Resultado final: ", acumulador)
