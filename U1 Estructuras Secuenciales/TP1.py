print("Ejercicio 1")
print("*" * 50)
# 1Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo!")


print("\nEjercicio 2")
print("*" * 50)
# 2Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
# Ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir “Hola Marcos!”.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

print("\nEjercicio 3")
print("*" * 50)
# 3 Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
# Ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir: “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Usted es {nombre} {apellido}, tiene {edad} años, y es de {residencia}.")

print("\nEjercicio 4")
print("*" * 50)
# 4 Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14159 * radio**2
perimetro = 3.14159 * 2 * radio
print(f"El área del círculo es {area}, y el perímetro es {perimetro}.")


print("\nEjercicio 5")
print("*" * 50)
# 5 Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivale a {horas} horas.")

print("\nEjercicio 6")
print("*" * 50)
# 6 Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un número entero: "))
for i in range(1, 11):
    print(f"{numero} x {i}: {numero * i}")

print("\nEjercicio 7")
print("*" * 50)
# 7 Crear un programa que pida al usuario dos números enteros distintos de 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese un número entero distinto de cero: "))
num2 = int(input("Ingrese otro número entero distinto de cero: "))
print(
    f"Suma : {num1 + num2}\nDivisión: {num1 / num2}\nMultiplicacion: {num1 * num2}\nResta: {num1 - num2}"
)

print("\nEjercicio 8")
print("*" * 50)
# 8 Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal (IMC).
altura = (float(input("Ingrese su altura en centrimetros (ejemplo 175): "))) / 100
peso = float(input("Ingrese su peso en kilogramos (ejemplo 70): "))
imc = peso / altura**2
print(f"Su indice de masa corporal es: {imc}")

print("\nEjercicio 9")
print("*" * 50)
# 9 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Ingrese un valor de temperatura en grados Celsius: "))
print(
    f"{celsius} grados celsius equivalen a {(celsius * 9/5) + 32} grados en escala de Farenheit."
)

print("\nEjercicio 10")
print("*" * 50)
# 10 Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
n1 = float(input("Ingrese un número: "))
n2 = float(input("Ingrese otro número: "))
n3 = float(input("Ingrese un último número: "))
print(f"Promedio: {(n1 + n2 + n3) / 3}")
