"""
Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""

frase = input("Ingrese una frase: ")
vocales = ["a", "e", "i", "o", "u"]
ultima_letra = frase[len(frase) - 1].lower()
if ultima_letra in vocales:
    frase += "!"
    print(frase)
else:
    print(frase)
