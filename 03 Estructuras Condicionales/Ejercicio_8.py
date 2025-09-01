"""
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas
"""

nombre = input("Ingresa tu nombre: ")
op = input(
    "Ingresa un número (1, 2 o 3) según la opción que desees:\n1. Mayúsculas\n2. Minúsculas\n3. Con la primera letra en mayúscula\nOpción: "
)


if op == "1":
    nom_final = nombre.upper()
    print(nom_final)
elif op == "2":
    nom_final = nombre.lower()
    print(nom_final)
elif op == "3":
    nom_final = nombre.title()
    print(nom_final)
else:
    print("Opción no válida. Por favor, ingresa 1, 2 o 3.")
