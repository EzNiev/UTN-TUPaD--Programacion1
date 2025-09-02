"""
Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar
"""

num = int(input("Ingrese un número par: "))
if num % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un número par.")
