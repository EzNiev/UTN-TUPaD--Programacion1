"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

cantidad = 0
media, suma = 0, 0
while cantidad > 100 or cantidad <= 0:
    cantidad = int(
        input("Ingrese la cantidad de números que desee procesar (máximo 100): ")
    )

for i in range(cantidad):
    n = int(input(f"Ingrese el número {i+1} a procesar: "))
    suma += n

media = suma / cantidad

print(f"Media de la suma de los {cantidad} números ingresados: {media}")
