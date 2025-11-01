"""
PROGRAMACIÓN 1 - Segundo Parcial
Alumno: Nieva Gabriel Ezequiel
DNI: 41153456
"""

import os


""" Funcion auxiliar para validar que un ingreso numerico sea un entero positivo, con un mensaje predeterminado """


def validar_entero_positivo(mensaje="Ingrese un valor entero positivo:\n> "):
    numero = input(mensaje)
    while not numero.isdigit() or int(numero) <= 0:
        print("Debe ingresar un número entero positivo.")
        numero = input(mensaje)
    return numero


""" Funcion auxiliar para extraer los libros del CSV y retornarlos en una lista para trabajar en memoria"""


def librosCSV_a_lista():
    # Funcion que extrae los libros del CSV y la guarda en una lista, sin printear nada
    libros = []

    with open("catalogo.csv", "r") as archivo:
        lineas = archivo.readlines()[1:]  # salto la cabecera
        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) >= 2:
                titulo = partes[0]
                cantidad = int(partes[1])
                libros.append({"titulo": titulo, "cantidad": cantidad})
    return libros


""" OPCION 1 - Ingresar multiples titulos """


def ingresar_titulos():

    cantidad_cargar = validar_entero_positivo(
        mensaje="Ingrese la cantidad de libros que desea cargar:\n> "
    )

    print(f"Se van a ingresar {cantidad_cargar} libros.")

    # Para evitar duplicados me di cuenta que debo verificar tanto en la lista en memoria como en el csv
    # Acá lo que hago es crear una lista con lo que ya esté en el archivo, si es que tiene algo
    titulos_existentes = []
    if os.path.exists("catalogo.csv"):
        with open("catalogo.csv", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) >= 1:
                    # Extraigo solo el titulo
                    titulo_existente = partes[0].lower()
                    titulos_existentes.append(titulo_existente)

    # Hasta acá tengo titulos_existentes con solo los titulos del archivo, si es que hay.

    # Acá empieza la carga, donde tambien valido lo que vaya cargando en memoria que no se repita con el archivo.
    libros_cargar = []
    for i in range(int(cantidad_cargar)):
        print("." * 66)

        # Como no se puede usar try except resolví con un while True
        while True:
            titulo = input(
                f"Ingrese el título del libro {i+1} (no se permiten campos vacíos ni repetidos):\n> "
            ).strip()

            # Valido que no sea un campo vacio ni espacio en blanco
            if titulo.strip() == "":
                print("ERROR: El título no puede estar vacío.")
                continue

            # Generar lista de títulos de la tanda actual
            # Es lo mismo que hice con el archivo pero con los datos en moemoria adentro de este ciclo while
            titulos_tanda = []
            for linea in libros_cargar:
                partes = linea.split(",")
                titulo_tanda = partes[0].lower()
                titulos_tanda.append(titulo_tanda)

            # Validar duplicados en memoria o en en CSV
            if titulo.lower() in titulos_tanda or titulo.lower() in titulos_existentes:
                print("ERROR: Ese título ya existe en el catálogo.")
                continue

            # Si pasó ambas validaciones, salir del while
            break

        cantidad = validar_entero_positivo(
            mensaje=f"Ingrese el stock del libro {i+1}:\n>"
        )

        libros_cargar.append(f"{titulo},{cantidad}\n")
    with open("catalogo.csv", "a") as catalogo:
        catalogo.writelines(libros_cargar)
    print("Libros correctamente cargados en el catálogo.")


""" OPCION 2 - Ingresar ejemplares """


def ingresar_ejemplares():
    """Ingresar ejemplares: sumar una cantidad X a un título existente."""
    # Cargo en memoria en una lista los libros del archivo
    libros = listar_mostrar_libros()
    # Verifico que tenga algo cargado
    if not libros:
        return

    # Reutilizo funcion validar entero positivo para elegir un libro
    eleccion = validar_entero_positivo(mensaje="Seleccione un título por número:\n>")

    # Verifico que esté dentro del rango válido
    while int(eleccion) < 1 or int(eleccion) > len(libros):
        print("Número fuera de rango. Intente nuevamente.")
        eleccion = validar_entero_positivo(
            mensaje="Seleccione un título por número:\n> "
        )

    libro_seleccionado = libros[int(eleccion) - 1]

    # Pido cantidad a sumar y la valido
    cantidad_sumar = validar_entero_positivo(
        mensaje="Ingrese la cantidad que desea sumar al stock:\n> "
    )

    # Actualizo el stock en memoria
    libro_seleccionado["cantidad"] += int(cantidad_sumar)

    # Guardo todos los libros nuevamente en el CSV (sobrescribiendo directamente)
    with open("catalogo.csv", "w") as catalogo:
        # Escribo la cabecera de nuevo
        catalogo.write("TITULO,CANTIDAD\n")
        # Escrito las lineas de libros
        for libro in libros:
            catalogo.write(f"{libro['titulo']},{libro['cantidad']}\n")

    print(f"\nStock actualizado correctamente.")
    print(
        f"{libro_seleccionado['titulo']} - Nuevo stock: {libro_seleccionado['cantidad']}"
    )


""" OPCION 3 - Sirve como uncion auxiliar para listar todos los libros del archivo """


def listar_mostrar_libros():
    """Lee el archivo catalogo.csv con funcion auxiliar y despues muestra los libros con número."""
    libros = librosCSV_a_lista()

    if not libros:
        print("No hay libros cargados en el catálogo aún.")
        return []

    print("\n--- LISTA DE LIBROS ---")
    for i, libro in enumerate(libros, start=1):
        print(f"{i}. {libro['titulo']} (Stock: {libro['cantidad']})")

    return libros


""" OPCION 4 - Consultar disponibilidad de X libro """


def consultar_disponibilidad():
    """Consultar disponibilidad: buscar un TITULO y mostrar cuántos ejemplares hay
    disponibles."""
    while True:
        titulo_buscar = (
            input(f"'Ingrese el título que desea verificar la disponibilidad:\n>' ")
            .strip()
            .lower()
        )

        # Valido que no sea un campo vacio ni espacio en blanco
        if titulo_buscar.strip() == "":
            print("ERROR: El título no puede estar vacío.")
            continue
        # Si pasa la validacion salgo del bucle
        break

    # Reutilizo codigo de funcion 1 para listar los libros
    libros = []

    with open("catalogo.csv", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            # Para no procesar la linea de cabecera
            if "TITULO" not in linea:
                partes = linea.strip().split(",")
                if len(partes) >= 2:
                    titulo = partes[0]
                    cantidad = int(partes[1])
                    libros.append({"titulo": titulo, "cantidad": cantidad})

    # Ahora tengo el titulo a buscar y una lista con los libros en memoria
    # Puedo trabajar en memoria
    encontrado = False
    for libro in libros:
        if libro["titulo"].lower() == titulo_buscar and int(libro["cantidad"]) > 0:
            print(
                f"El libro {libro['titulo']} tiene un stock disponible de {libro['cantidad']}"
            )
            encontrado = True
        elif libro["titulo"].lower() == titulo_buscar and int(libro["cantidad"]) == 0:
            print(
                f"El libro {libro['titulo']} no tiene disponibilidad ya que tiene un stock disponible de {libro['cantidad']} unidades."
            )
            encontrado = True

    if not encontrado:
        print(f"No se encontró ningún libro con el titulo: '{titulo_buscar}'.")


""" OPCION 5 - LISTAR AGOTADOS """


def listar_agotados():
    # Listar agotados: mostrar solo los títulos con CANTIDAD == 0.
    libros = librosCSV_a_lista()
    # Luego en esta funcion trabajo con una lista en memoria a la que
    # Recorro con un for y muestro solo los que tengan cantidad = 0

    # Reutilizo el código de funcion 3 pero le agrego la condicion de que cantidad == 0
    if not libros:
        print("No hay libros cargados en el catálogo aún.")
        return []

    print("\n--- LISTA DE LIBROS AGOTADOS ---")
    hay_agotados = False
    for i, libro in enumerate(libros):
        if i > 0 and libro["cantidad"] == 0:
            hay_agotados = True
            print(f"{i}. {libro['titulo']} (Stock: {libro['cantidad']})")
    if not hay_agotados:
        print("No hay libros agotados.")


""" OPCION 6 - Agregar titulo """


def agregar_titulo():
    """Agregar título: alta de un libro individual (validar duplicados) con su cantidad inicial."""
    # Para evitar duplicados me di cuenta que debo verificar tanto en la lista en memoria como en el csv
    # Acá lo que hago es crear una lista con lo que ya esté en el archivo, si es que tiene algo
    titulos_existentes = []
    if os.path.exists("catalogo.csv"):
        with open("catalogo.csv", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) >= 1:
                    # Extraigo solo el titulo
                    titulo_existente = partes[0].lower()
                    titulos_existentes.append(titulo_existente)
    while True:
        titulo = input(
            f"Ingrese el título del nuevo libro (no se permiten campos vacíos ni repetidos):\n> "
        ).strip()

        # Valido que no sea un campo vacio ni espacio en blanco
        if titulo.strip() == "":
            print("ERROR: El título no puede estar vacío.")
            continue

        # Validar duplicados en CSV
        if titulo.lower() in titulos_existentes:
            print("ERROR: Ese título ya existe en el catálogo.")
            continue

        # Si pasó validaciones, salir del while
        break

    cantidad = validar_entero_positivo(
        mensaje=f"Ingrese el stock del nuevo libro '{titulo}':\n>"
    )

    with open("catalogo.csv", "a") as catalogo:
        catalogo.writelines(f"{titulo},{cantidad}\n")

    # Poner mensaje de OK ACA

    print(
        f"El libro '{titulo}' con stock de {cantidad} unidades se agregó correctamente al catálogo."
    )
    input(
        "Puede consultarlo con la opción 3 del menú principal\nPresione ENTER para continuar."
    )


""" OPCION 7 - Actualizar ejemplares, simular prestamos y devoluciones """


def actualizar_ejemplares():
    """Actualizar ejemplares (préstamo/devolución):
    ○ Préstamo: restar 1 solo si CANTIDAD > 0.
    ○ Devolución: sumar 1."""

    """
    para actualizar los ejemplares deberia cargar el archivo en una lista
    hacer busqueda, mostrando al usuario los libros y dejarle elegir por ID
    Todo esto ya lo hace la funcion  2 que a su vez usa la funcion 3
    """

    # Cargo en memoria en una lista los libros del archivo
    libros = listar_mostrar_libros()
    # Verifico que tenga algo cargado
    if not libros:
        # No imprimo mensaje porque ya esta en la funcion de listar libros
        return

    # Reutilizo funcion validar entero positivo para elegir un libro
    eleccion = validar_entero_positivo(mensaje="Seleccione un título por número:\n>")

    # Verifico que esté dentro del rango válido
    while int(eleccion) < 1 or int(eleccion) > len(libros):
        print("Número fuera de rango. Intente nuevamente.")
        eleccion = validar_entero_positivo(
            mensaje="Seleccione un título por número:\n> "
        )
    # En este punto lo unico que tengo es la eleccion CORRECTA y Validada del usuario
    libro_seleccionado = libros[int(eleccion) - 1]
    print(f"Libro seleccionado: {libro_seleccionado['titulo']}")

    # una vez seleccionado preguntar si solicita cargar un prestamo o una devolucion
    opcion = 3
    prestamo_devolucion = (
        "\nAhora por favor elija si desea cargar un préstamo o una devolución"
        "\n1- Préstamo"
        "\n2- Devolución\n>"
    )
    opcion = int(validar_entero_positivo(mensaje=prestamo_devolucion))
    while opcion not in [1, 2]:
        opcion = int(validar_entero_positivo(mensaje=prestamo_devolucion))

    # Ahora tengo el ID del libro y si es prestamo o devolucion, validados

    if opcion == 1:
        # PRESTAMO restar 1 si el titulo tiene cantidad >= 1
        if libro_seleccionado["cantidad"] > 0:
            libro_seleccionado["cantidad"] -= 1
            print("Prestamo registrado correctamente.")
        if libro_seleccionado["cantidad"] <= 0:
            print("No se puede hacer un prestamo de este libro ya que no hay stock.")

    elif opcion == 2:
        # DEVOLUCION
        # una devolucion seria como una carga de ejemplares con cantidad = 1
        libro_seleccionado["cantidad"] += 1
        print("Devolución registrada correctamente.")

    # Guardo todos los libros nuevamente en el CSV (sobrescribiendo directamente)
    with open("catalogo.csv", "w") as catalogo:
        # Escribo la cabecera de nuevo
        catalogo.write("TITULO,CANTIDAD\n")
        # Escrito las lineas de libros
        for libro in libros:
            catalogo.write(f"{libro['titulo']},{libro['cantidad']}\n")

    print(f"\nStock actualizado correctamente.")
    print(
        f"{libro_seleccionado['titulo']} - Nuevo stock: {libro_seleccionado['cantidad']}"
    )


def main():
    separador = "=" * 66
    # Si el catálogo no existe, se crea vacío, solo con las cabeceras
    # Si el archivo ya existe se ignora y deja el existente como está
    if not os.path.exists("catalogo.csv"):
        with open("catalogo.csv", "w") as archivo:
            archivo.write("TITULO,CANTIDAD\n")
        print("Archivo 'catalogo.csv' inicializado correctamente.")

    while True:

        print(f"\n{separador}")
        print("========== SISTEMA DE STOCK DE LIBROS DE LA BIBILIOTECA ==========")
        print(f"{separador}")
        print("1 - Ingresar multiples títulos.")
        print("2 - Ingresar ejemplares")
        print("3 - Mostrar catálogo")
        print("4 - Consultar disponibilidad")
        print("5 - Listar agotados")
        print("6 - Agregar título")
        print("7 - Actualizar ejemplares (préstamo/devolución)")
        print("8 - Salir del programa")
        opcion = input("Seleccione una opción:\n> ")

        match opcion:
            case "1":
                print(f"\n{separador}" f"\nINGRESAR MULTIPLES TITULOS" f"\n{separador}")
                ingresar_titulos()
            case "2":
                print(f"\n{separador}" f"\nINGRESAR EJEMPLARES" f"\n{separador}")
                ingresar_ejemplares()
            case "3":
                print(f"\n{separador}" f"\nMOSTRAR CATÁLOGO" f"\n{separador}")
                listar_mostrar_libros()
                input("Presione ENTER para continuar al menú.")
            case "4":
                print(f"\n{separador}" f"\nCONSULTAR DISPONIBILIDAD" f"\n{separador}")
                consultar_disponibilidad()
                input("Presione ENTER para continuar al menú.")
            case "5":
                print(f"\n{separador}" f"\nLISTAR AGOTADOS" f"\n{separador}")
                listar_agotados()
            case "6":
                print(f"\n{separador}" f"\nAGREGAR TITULO" f"\n{separador}")
                agregar_titulo()
            case "7":
                print(f"\n{separador}" f"\nACTUALIZAR EJEMPLARES" f"\n{separador}")
                actualizar_ejemplares()
                input("Presione ENTER para continuar al menú.")
            case "8":
                print("Saliendo del programa...")
                break
            case _:
                # Con esta linea se validan cualquier ingreso erroneo del menú, ya sea fuera de rango o vacio
                print("Opción inválida, intente otra vez.")


if __name__ == "__main__":
    main()
