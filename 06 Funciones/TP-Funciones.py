"""
Este archivo es la resolución del trabajo práctico de funciones, unidad 6.
Decidí hacer todos los ejercicios en un único archivo a diferencia de las otras unidades.
Además de las funciones para cada ejercicio, codifique las funciones para manejar
tanto el print del menú, como la selección de opciones usando try;except para manejar
errores y un funcion main para ejecutar todas las anteriores,
aplicando los conceptos de modularidad, composicion de funciones, descomposicion
de problemas complejos en problemas simples, mejorando la robustez del programa
y facilitando al usuario tanto el ingreso de datos como la prueba de las funciones
dejando todas las funciones a mano para usarlas, bien comentadas y explicadas,
con los errores explicando cual fue el error de tipeo.
"""

# =================================================================
# DEFINICIÓN DE FUNCIONES
# =================================================================


# EJERCICIO 1
def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' en la consola."""
    print("Hola Mundo!")


# EJERCICIO 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# EJERCICIO 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# EJERCICIO 4
def calcular_area_circulo(radio):
    return 3.1415 * (radio**2)


def calcular_perimetro_circulo(radio):
    return 2 * 3.1415 * radio


# EJERCICIO 5
def segundos_a_horas(segundos):
    return segundos / 3600


# EJERCICIO 6
def tabla_multiplicar(numero):
    print(f"--- Tabla del {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


# EJERCICIO 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b != 0:
        division = round(a / b, 3)
    else:
        division = "Indefinido (división por cero)"

    return (suma, resta, multiplicacion, division)


# EJERCICIO 8
def calcular_imc(peso, altura):
    if altura <= 0:
        return 0
    return peso / ((altura / 100) ** 2)


# EJERCICIO 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# EJERCICIO 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# =================================================================
# MENÚ PRINCIPAL
# =================================================================


def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n" + "=" * 45)
    print("         MENÚ PRÁCTICO 2: FUNCIONES")
    print("=" * 45)
    print(" 1. Saludo básico")
    print(" 2. Saludo personalizado")
    print(" 3. Información personal")
    print(" 4. Círculo (Área y Perímetro)")
    print(" 5. Segundos a Horas")
    print(" 6. Tabla de Multiplicar")
    print(" 7. Operaciones Básicas (Tupla)")
    print(" 8. Cálculo de IMC")
    print(" 9. Celsius a Fahrenheit")
    print("10. Calcular Promedio de 3 números")
    print(" 0. Salir")
    print("=" * 45)


def ejecutar_opcion(opcion):
    """Ejecuta la función según la opción elegida."""
    """
    Uso el try para validar las entradas, mas que para validar lo uso para evitar que un error de ingreso
    rompa el programa y así derivo al usuario nuevamente al menú principal, mostrando un mensaje de error
    """
    try:
        match opcion:
            case "1":
                print("\n--- Ejecutando Ejercicio 1 ---")
                imprimir_hola_mundo()

            case "2":
                print("\n--- Ejecutando Ejercicio 2 ---")
                nombre = input("Ingresa tu nombre:\n> ")
                saludo = saludar_usuario(nombre)
                print(saludo)

            case "3":
                print("\n--- Ejecutando Ejercicio 3 ---")
                nombre = input("Ingresa tu nombre:\n> ")
                apellido = input("Ingresa tu apellido:\n> ")
                edad = int(input("Ingresa tu edad:\n> "))
                residencia = input("Ingresa tu residencia:\n> ")
                informacion_personal(nombre, apellido, edad, residencia)

            case "4":
                print("\n--- Ejecutando Ejercicio 4 ---")
                radio_ingresado = float(input("Ingresa el radio del círculo:\n> "))
                area = calcular_area_circulo(radio_ingresado)
                perimetro = calcular_perimetro_circulo(radio_ingresado)
                print(f"El Área del círculo es: {round(area, 2)}")
                print(f"El Perímetro del círculo es: {round(perimetro, 2)}")

            case "5":
                print("\n--- Ejecutando Ejercicio 5 ---")
                segundos_ingresados = float(input("Ingresa los segundos:\n> "))
                horas = segundos_a_horas(segundos_ingresados)
                print(
                    f"{segundos_ingresados} segundos equivalen a {round(horas, 4)} horas."
                )

            case "6":
                print("\n--- Ejecutando Ejercicio 6 ---")
                numero_base = int(input("Ingresa un número para su tabla:\n> "))
                tabla_multiplicar(numero_base)

            case "7":
                print("\n--- Ejecutando Ejercicio 7 ---")
                num1 = float(input("Ingresa el primer número (A):\n> "))
                num2 = float(input("Ingresa el segundo número (B):\n> "))
                suma_res, resta_res, mult_res, div_res = operaciones_basicas(
                    round(num1, 3), round(num2, 3)
                )
                print("\nResultados:")
                print(
                    f"Suma: {suma_res}, Resta: {resta_res}, Multiplicación: {mult_res}, División: {div_res}"
                )

            case "8":
                print("\n--- Ejecutando Ejercicio 8 ---")
                peso_kg = float(input("Ingresa tu peso en kg:\n> "))
                altura_cm = float(input("Ingresa tu altura en centimetros:\n> "))
                imc = calcular_imc(peso_kg, altura_cm)
                if imc > 0:
                    print(f"Tu IMC es:\n> {round(imc, 2)}")
                else:
                    print("Error: La altura debe ser positiva.")

            case "9":
                print("\n--- Ejecutando Ejercicio 9 ---")
                temp_celsius = float(input("Ingresa la temperatura en °C:\n> "))
                temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
                print(f"{temp_celsius}°C equivalen a {round(temp_fahrenheit, 2)}°F.")

            case "10":
                print("\n--- Ejecutando Ejercicio 10 ---")
                num_a = float(input("Ingresa el primer número:\n> "))
                num_b = float(input("Ingresa el segundo número:\n> "))
                num_c = float(input("Ingresa el tercer número:\n> "))
                promedio = calcular_promedio(num_a, num_b, num_c)
                print(f"El promedio es: {round(promedio, 2)}")

            case "0":
                print("\nEl programa ha finalizado.")
                return False

            case _:
                print(
                    "\nOpción no válida. Por favor, selecciona un número del 0 al 10."
                )

    # El value error es un error de valor ingresado, por ejemplo, el programa esperaba un int y se ingresa un str
    # Esto me ahorra muchas lineas validando ingresos en cada funcion, lo que las hace mas simples de entender y mantener
    except ValueError:
        print(
            "\nERROR DE ENTRADA: Asegúrate de ingresar solo números (enteros o decimales) donde se solicitan."
        )
        input("\nPresione ENTER para volver al menú...")
        print("\n" * 50)
        return True

    # Acá es un error de excepcion. Me sirve tanto a mi como al usuario, por ejemplo, me intercepta las divisiones por cero
    # sin frenar el programa, lo que me permite hacer correcciones. Aunque valide muchas cosas, por buenas practicas lo dejo.
    except Exception as e:
        print(f"\nERROR INESPERADO: {e}")
        input("\nPresione ENTER para volver al menú...")
        print("\n" * 50)
        return True
    input("\nPresione ENTER para continuar...")
    print("\n" * 50)
    return True


# --- Bucle Principal del Programa ---
# Acá uso una bandera para definir si el programa se sigue ejecutando...
# Será siempre true, hasta que se elija la opcion 0 que la retorna en False, finalizando el programa.
if __name__ == "__main__":
    continuar = True
    while continuar:
        mostrar_menu()
        opcion_elegida = input("Selecciona una opción:\n> ")
        continuar = ejecutar_opcion(opcion_elegida)
