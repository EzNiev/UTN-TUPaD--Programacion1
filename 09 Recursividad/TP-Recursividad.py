"""
Funcion auxiliar que uso en casi todas las otras. Para evitar tanto codigo repetido la hice separada
"""


def validar_entero_positivo(mensaje="Ingrese un valor entero positivo:\n> "):
    numero = input(mensaje)
    while not numero.isdigit() or int(numero) <= 0:
        print("Debe ingresar un número entero positivo.")
        numero = input(mensaje)
    return int(numero)


"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""


# Funcion que calcula UN factorial para UN numero
def calculo_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calculo_factorial(num - 1)


# Funcion que calcula varios factoriales utilizando la funcion calculo_factorial mediante un ciclo FOR
def factorial_hasta():
    num = validar_entero_positivo(
        "Ingrese hasta que número desea calcular los factoriales:\n> "
    )
    for i in range(num + 1):
        factorial = calculo_factorial(i)
        print(f"Factorial del número {i}: {factorial}")


"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
Para esto voy a necesitar:
    - Funcion que calcule fibonacci
    - Funcion que reciba un valor X y calcule esa posicion de fibonacci y luego muestre todos los anteriores
"""


def calcular_fibonacci(posicion):
    # Sucesion de fibonacci = 0,1,1,2,3,5,8,13,21...
    # Casos base
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1

    # Caso recursivo
    return calcular_fibonacci(posicion - 1) + calcular_fibonacci(posicion - 2)


def fibonacci_completo():
    num = validar_entero_positivo(
        "Ingrese la posición hasta la cual cual quiere calcular la sucesión de Fibonacci:\n> "
    )
    if num > 35:
        # La recursividad gasta muchos recursos!
        # Lo ideal seria hacer un algoritmo iterativo con un for por ejemplo
        print("Esto puede demorar...")

    print(
        f"En la sucesión de Fibonacci la posición número {num} es {calcular_fibonacci(num-1)}"
    )

    for i in range(num):
        print(f"Posición {i+1} = {calcular_fibonacci(i)}")


"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
algoritmo general.
"""


def potencia_recursiva(base, exponente):
    # en la formula n^m = n * n^(m−1) --> Base seria la n y el exponente seria la m
    # El caso base va a ser cuando m=0
    if exponente == 0:
        return 1
    # Mientras tanto tengo que aplicar la formula
    else:
        return base * potencia_recursiva(base, exponente - 1)
    """
    Si me pasan base = 5 y exponente igual a 3 quedaria
    base = 5 * 5 ** (2), es decir 5x25 lo que tiene sentido, por seria igual que 5 x 5 x 5
    """


def potencia_base_exponente():
    base = validar_entero_positivo("Ingrese un valor para la base:\n>")
    exponente = validar_entero_positivo("Ingrese un valor para el exponente:\n>")
    print(
        f"El resultado de {base} a la potencia de {exponente} es igual a {potencia_recursiva(base, exponente)}"
    )


"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2.
"""


def decimal_binario_recursivo(n):
    # Caso base
    if n == 0:
        return ""

    # Llamada recursiva
    return decimal_binario_recursivo(n // 2) + str(n % 2)


def decimal_a_binario():
    decimal = validar_entero_positivo(
        "Ingrese un número entero en base 10 para convertir a binario:\n>"
    )
    if decimal == 0:
        binario = "0"
    else:
        print("Calculando...")
        binario = decimal_binario_recursivo(decimal)

    print(f"El número {decimal} representado en base binaria es: {binario}")


"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""


def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True

    # Si la primera y última letra no coinciden, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False

    # Llamada recursiva eliminando la primera y última letra
    return es_palindromo(palabra[1:-1])


def verificar_palindromo():
    palabra = input(
        "Ingrese una palabra para verificar si es un palíndromo:\n>"
    ).strip()
    resultado = es_palindromo(palabra)
    if resultado:
        print(f"La palabra {palabra} es un palíndromo")
    else:
        print(f"La palabra {palabra} NO es un palíndromo")


"""

6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
"""


def suma_digitos_recursiva(num):
    if num < 10:
        # print(num)
        return num
    # Obtengo el ultimo digito
    digito = num % 10
    # Al numero le saco ese ultimo digito
    num = num // 10

    # print(digito)
    return digito + suma_digitos_recursiva(num)


def pedir_numero_suma_digitos():
    num = validar_entero_positivo(
        "Ingrese un número para calcular la suma de sus dígitos:\n> "
    )
    suma = suma_digitos_recursiva(num)
    print(f"La suma de los dígitos del número {num} = {suma}")


"""
7) Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
"""


def contar_bloques(base):
    # Caso base, que ingresen 0 o 1, o que las restas lleguen a 1
    if base <= 1:
        return base

    return base + contar_bloques(base - 1)


def solicitar_cantidad_bloques():
    bloques_base = validar_entero_positivo(
        "Ingrese la cantidad de bloques de la base de la pirámide:\n> "
    )
    bloques_piramide = contar_bloques(bloques_base)
    print(
        f"La cantidad de bloques para una pirámide de base {bloques_base} = {bloques_piramide}"
    )


"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
"""


def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito, seria la ultima comparacion

    if numero < 10:
        if digito == numero:
            return 1
        else:
            return 0

    # Obtengo el ultimo digito
    digito_num = numero % 10
    # Al numero le saco ese ultimo digito
    numero_nuevo = numero // 10

    if digito == digito_num:
        return 1 + contar_digito(numero_nuevo, digito)
    else:
        return 0 + contar_digito(numero_nuevo, digito)


def solicitar_numero_y_digito():
    digito = 11
    num = validar_entero_positivo("Ingrese un numero:\n> ")
    while digito >= 10:
        digito = validar_entero_positivo("Ingrese un digito:\n> ")
    cantidad_apariciones = contar_digito(num, digito)
    print(
        f"En el número {num} el dígito {digito} aparece {cantidad_apariciones} veces."
    )


"""
Opcion 9 - una funcion que explica mejor que hace cada una de las otras.
"""


def detalle_de_funciones():
    print(
        """
    DETALLE DE FUNCIONES RECURSIVAS

    1) Calcular factorial hasta 'X' número.
    Calcula el factorial de un número usando recursión.
    Caso base: 0! = 1
    Caso recursivo: n! = n * (n - 1)!

    factorial_hasta():
    Pide un número al usuario y muestra el factorial de todos los números desde 0 hasta ese número.

    2) Sucesión de Fibonacci hasta 'X' número
    Devuelve el valor de la sucesión de Fibonacci en la posición indicada.
    Casos base:
        F(0) = 0
        F(1) = 1
    Caso recursivo:
        F(n) = F(n - 1) + F(n - 2)

    fibonacci_completo():
    Pide un número al usuario y muestra toda la sucesión hasta esa posición.

    3) Potencia por recursividad
    Calcula base^exp usando la fórmula recursiva:
        n^m = n * n^(m - 1)
    Caso base:
        todo número elevado a 0 da 1.

    potencia_base_exponente():
    Pide base y exponente al usuario y muestra el resultado.

    4) Pasar número decimal a binario
    Convierte un número decimal a binario sin usar funciones internas.
    Caso base:
        Si n = 0, devuelve "".
    Caso recursivo:
        binario(n) = binario(n // 2) + (n % 2)

    decimal_a_binario():
    Pide un número y muestra su representación binaria.

    5) Verificar palíndromo
    Verifica si una palabra es palíndroma.
    Casos base:
        0 o 1 caracteres → es palíndromo.
    Caso recursivo:
        Compara primer y último caracter y llama recursivamente al centro.

    verificar_palindromo():
    Pide una palabra y muestra si es un palíndromo.

    6) Suma de dígitos de un número
    Suma los dígitos de un número sin convertirlo a string.
    Caso base:
        Si num < 10 → devuelve ese dígito.
    Caso recursivo:
        último = num % 10
        resto = num // 10
        suma = último + suma_dígitos_recursiva(resto)

    pedir_número_suma_digitos():
    Pide un número y muestra la suma de sus dígitos.

    7) Calcular bloques de una piramide según bloques
    Calcula cuántos bloques requiere una pirámide con base n.
    Caso base:
        n <= 1 → devuelve n
    Caso recursivo:
        total = n + contar_bloques(n - 1)

    solicitar_cantidad_bloques():
    Pide la base y calcula el total de bloques.

    8) Contar dígitos
    Cuenta cuántas veces aparece un dígito dentro de un número.
    Caso base:
        Si número < 10 → compara directamente.
    Caso recursivo:
        último = numero % 10
        resto = numero // 10
        suma = (1 si último == dígito else 0) + contar_digito(resto, dígito)

    solicitar_numero_y_digito():
    Pide un número y un dígito, y muestra cuántas veces aparece.

    9) Detalle de cada funcion
    Explica como usar y como funciona cada una de las otras opciones.
    Y como estamos en recursividad también se explica a sí misma.

    0) Salir
    Sale del programa finalizando el bucle.
    """
    )

    pass


def main():
    while True:
        print("\n--- MENÚ DE FUNCIONES RECURSIVAS ---")
        print("1 - Calcular factorial hasta 'X' número.")
        print("2 - Sucesión de Fibonacci hasta 'X' posición.")
        print("3 - Potencia por recursividad.")
        print("4 - Pasar número decimal a binario.")
        print("5 - Verificar palíndromo.")
        print("6 - Suma de dígitos de un número.")
        print("7 - Calcular bloques de una piramide según bloques.")
        print("8 - Contar dígitos.")
        print("9 - Manual de funciones.")
        print("0 - Salir.")
        opcion = input("Seleccione una opción:\n> ")

        try:
            match opcion:
                case "1":
                    factorial_hasta()
                case "2":
                    fibonacci_completo()
                case "3":
                    potencia_base_exponente()
                case "4":
                    decimal_a_binario()
                case "5":
                    verificar_palindromo()
                case "6":
                    pedir_numero_suma_digitos()
                case "7":
                    solicitar_cantidad_bloques()
                case "8":
                    solicitar_numero_y_digito()
                case "9":
                    detalle_de_funciones()
                case "0":
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción inválida, intente otra vez.")

        # El value error es un error de valor ingresado, por ejemplo, el programa esperaba un int y se ingresa un str
        # Esto me ahorra muchas lineas validando ingresos en cada funcion, lo que las hace mas simples de entender y mantener
        except ValueError:
            print(
                "\nERROR DE ENTRADA: Asegúrate de ingresar solo números (enteros o decimales) donde se solicitan."
            )
            input("\nPresione ENTER para volver al menú...")
            print("\n" * 50)
            continue

        except Exception as e:
            print(f"\nERROR INESPERADO: {e}")
            input("\nPresione ENTER para volver al menú...")
            print("\n" * 50)
            continue
        input("\nPresione ENTER para continuar...")
        print("\n" * 50)


if __name__ == "__main__":
    main()
