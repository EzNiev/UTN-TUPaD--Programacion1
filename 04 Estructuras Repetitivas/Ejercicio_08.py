"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

cantidad = 0
par, impar, neg, pos, ceros = 0, 0, 0, 0, 0
while cantidad > 100 or cantidad <= 0:
    cantidad = int(
        input("Ingrese la cantidad de números que desee procesar (máximo 100): ")
    )

for i in range(cantidad):
    n = int(input(f"Ingrese el número {i+1} a procesar: "))
    if n % 2 == 0:
        par += 1
        print(f"Número par!         Contador de pares {par}")
    else:
        impar += 1
        print(f"Número impar!       Contador de impares {impar}")
    if n > 0:
        pos += 1
        print(f"Número positivo!    Contador de positivos {pos}")
    elif n == 0:
        ceros += 1
    else:
        neg += 1
        print(f"Número negativo!    Contador de negativo {neg}")
    print("=" * 40)

print(
    f"Resultados finales:\n"
    f"Positivos:    {pos}\n"
    f"Negativos:    {neg}\n"
    f"Pares:        {par}\n"
    f"Impares:      {impar}\n"
    f"Ceros:        {ceros}\n"
)
