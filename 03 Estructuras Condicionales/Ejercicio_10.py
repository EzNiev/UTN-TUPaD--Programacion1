"""
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano, según la siguiente tabla:
•	Desde el 21 de diciembre hasta el 20 de marzo: Invierno (N) / Verano (S)
•	Desde el 21 de marzo hasta el 20 de junio: Primavera (N) / Otoño (S)
•	Desde el 21 de junio hasta el 20 de septiembre: Verano (N) / Invierno (S)
•	Desde el 21 de septiembre hasta el 20 de diciembre: Otoño (N) / Primavera (S)

"""

hemisferio = input("¿En qué hemisferio esta? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día es?: "))


if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3 and dia <= 20):
    if hemisferio == "N":
        print("Te encuentras en Invierno.")
    elif hemisferio == "S":
        print("Te encuentras en Verano.")

elif (mes >= 3 and dia >= 21) or (mes >= 4 and mes <= 6 and dia <= 20):
    if hemisferio == "N":
        print("Te encuentras en Primavera.")
    elif hemisferio == "S":
        print("Te encuentras en Otoño.")

elif (mes >= 6 and dia >= 21) or (mes >= 7 and mes <= 9 and dia <= 20):
    if hemisferio == "N":
        print("Te encuentras en Verano.")
    elif hemisferio == "S":
        print("Te encuentras en Invierno.")

elif (mes >= 9 and dia >= 21) or (mes >= 10 and mes <= 12 and dia <= 20):
    if hemisferio == "N":
        print("Te encuentras en Otoño.")
    elif hemisferio == "S":
        print("Te encuentras en Primavera.")
else:
    print("La combinación de fecha no corresponde a una estación.")
