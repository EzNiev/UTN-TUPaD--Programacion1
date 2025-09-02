"""
2 Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

n = int(input("Ingrese un número entero: "))
digitos = 1
while n > 10:
    n /= 10
    digitos += 1

print(f"Digitos contados: {digitos}")
