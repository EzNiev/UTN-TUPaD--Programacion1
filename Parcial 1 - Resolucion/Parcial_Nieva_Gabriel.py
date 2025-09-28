"""
PROGRAMACIÓN 1 - Primer Parcial
Alumno: Nieva Gabriel Ezequiel
DNI: 41153456
"""

# Inicialización de variables
# Me gustaría mencionar que yo usaria una estructura de listas anidadas para hacer este ejercicio
# titulos = [["nombre", cantidad],["nombre", cantidad],["nombre", cantidad],["nombre", cantidad]]
# Por cuestiones de interpretación de la consigna me limito a usar dos listas sincronizadas

titulos = []
ejemplares = []

# Esto lo iba a borrar, son las listas que hardcodee para hacer las pruebas sin tener que cargar siempre a mano los datos
# Decidí dejarlas porque son la evidencia de que hice pruebas y si tengo algún error que puede estar relacionado a que las
# listas estan mal cargadas me gustaría saberlo, espero no sea problema ya uqe no está en la consigna.
"""
titulos = [
    "El Señor de los Anillos",
    "Orgullo y Prejuicio",
    "Matar un Ruiseñor",
    "Cien Años de Soledad",
    "1984",
    "Don Quijote de la Mancha",
    "Crónica de una Muerte Anunciada",
    "Fahrenheit 451",
    "La Odisea",
    "Harry Potter y la Piedra Filosofal",
    "Los Juegos del Hambre",
    "Drácula",
    "It",
    "El Hobbit",
    "La Metamorfosis",
    "El Principito",
    "El Nombre del Viento",
    "Rayuela",
    "El Código Da Vinci",
    "El Alquimista"
]

ejemplares = [
    5,   # El Señor de los Anillos
    0,   # Orgullo y Prejuicio
    0,   # Matar un Ruiseñor
    3,   # Cien Años de Soledad
    10,  # 1984
    0,   # Don Quijote
    2,   # Crónica de una Muerte Anunciada
    7,   # Fahrenheit 451
    0,   # La Odisea
    12,  # Harry Potter
    1,   # Los Juegos del Hambre
    0,   # Drácula
    4,   # It
    0,   # El Hobbit
    8,   # La Metamorfosis
    0,   # El Principito
    6,   # El Nombre del Viento
    0,   # Rayuela
    9,   # El Código Da Vinci
    0    # El Alquimista
]

"""

op = ""
separador = "=" * 65

# Ejecución principal, si se pudieran usar funciones esta sería la funcion main.
# Cuando la opcion sea cualquier cosa menos el 8, se ejecuta, luego se valida que sea una opcion del menú.
while op != "8":

    # Se muestra el menú en cada ejecución del ciclo para que el usuario pueda leer las opciones cada vez que se ejecuta
    print(f'\n{separador}'
        f'\n==================== MENÚ PRINCIPAL ============================='
        f'\n================================================================='
        f'\n1- Ingresar títulos'
        f'\n2- Ingresar ejemplares'
        f'\n3- Mostrar catálogo'
        f'\n4- Consultar disponibilidad'
        f'\n5- Listar agotados'
        f'\n6- Agregar título'
        f'\n7- Actualizar ejemplares'
        f'\n8- Salir'
          )

    # Se solicita al usuario que elija una opcion del menu, lo proceso como string para validarlo mas fácil en los case
    # Le pongo el strip por si el usuario ingresa sin querer un espacio antes o despues de la opcion
    op = input("Seleccione una opción del menu (1-8):").strip()
    match op:
        case "1": # Ingresar titulos
            print(f'\n{separador}')
            print("INGRESAR TITULOS")

            # Acá hago una validación de la cantidad de titulo ingresada por le usuario para que tenga sentido y no rompa el programa
            num_a_cargar = 0
            while num_a_cargar <= 0:
                cantidad_titulos = input("Ingrese la cantidad de títulos que desea cargar: ")
                if cantidad_titulos.isdigit():
                    num_a_cargar = int(cantidad_titulos)
                else:
                    print("Tiene que ingresar un número entero positivo.")


            for i in range(num_a_cargar):
                titulo = input(f'Ingrese el nombre del libro #{i+1}: ')
                if titulo != "":
                    if titulo not in titulos:
                        # Cada vez que ingrese un titulo cargo el nombre al final de la lista, luego de validar que no esté ya cargado
                        titulos.append(titulo)
                        # Cargo una cantidad de copias en 0, para que ambas listas desde ya tengan la misma cantidad de indices
                        # Entonces si alguien carga solo títulos y luego quiere ver el catálogo, lo verá con stock 0 en todos los titulos
                        ejemplares.append(0)
                    else:
                        print(f'El título "{titulo}" ya existe en el catálogo.')
                else:
                    print(f'\nERROR. No debe ingresar un nombre vacío.'
                          f'\nSi lo que desea es eliminar un libro o disminuir la cantidad de copias deberá usar la opción correspondiente. (Opcion 7)'
                          )
                    input("Presione ENTER para continuar")
            print(f'\n{separador}'
                  f'\nSe han agregado exitosamente los títulos a la base, puede corroborarlo usando la opción 3 del menú principal.'
                  f'\n{separador}'
                  )
        case "2": # Cargar ejemplares
            print(f'\n{separador}'
                  f'\nINGRESAR EJEMPLARES'
                  f'\n{separador}'
                  f'\n\nAdvertencia: Se deberá ingresar la cantidad de ejemplares que se AGREGAN al stock.'
                  f'\nEsto significa que el valor que usted ingrese se sumará al stock actual, no lo reemplazará.'
                  f'\n{separador}'
                  )
            if len(titulos) > 0:
                for i in range(len(titulos)):
                    print(f'\n{separador}'
                          f'\nIngrese la cantidad de copias para el título: {titulos[i]}'
                          )
                    copias = -1
                    while copias < 0:
                        carga_copias = input("- Copias (o presioner ENTER para saltear): ").strip()
                        if carga_copias == "":
                            print("No se agregaron copias.")
                            copias = 0
                        elif carga_copias.isdigit():
                            copias = int(carga_copias)
                            ejemplares[i] += copias
                        else:
                            print("Debe ingresar un número válido.")
                print(f'\n{separador}')
                print("Se han agregado exitosamente las copias al stock.")
                print("Puede corroborarlo usando la opción 3 del menú principal.")
                print(f'{separador}')
                input("Presione ENTER para continuar")
            else:
                print("No hay titulos cargados aún, por favor, elija la opción 1 para cargarlos y luego puede utilizar esta función.")
                input("Presione ENTER para continuar")
        case "3": # MOstrar catalogo
            print(f'\n{separador}')
            print('MOSTRAR CATÁLOGO')
            print(f'{separador}')

            # Como lo voy a mostrar tipo tabla le hago una cabecera.
            if len(titulos) > 0:
                print("ID   Título                                            Ejemplares")
                print("-----------------------------------------------------------------")

                for i in range(len(titulos)):
                    # A las variables para que no me de error las paso a string por las dudas.4
                    if i + 2 > 10:
                        num = str(i + 1)
                    else:
                        num = str(i + 1) + " "
                    titulo = titulos[i]
                    cantidad = str(ejemplares[i])

                    # Alineación básica  para que quede más prolijo
                    # (ajusto los espacios como para que entren bien la mayoria de los titulos)
                    # Esta fue la unica forma que encontre para tabular y que queden mas o menos bien, el problema es si el titulo tiene mas de 30 caracteres
                    if len(titulo) < 50:
                        espacios_titulo = " " * (50 - len(titulo))
                    else:
                        espacios_titulo = " "
                    espacios_num = " " * 4
                    print(f'{num}{espacios_num}{titulo}{espacios_titulo}{cantidad}')

                print(f'{separador}')
                input("Presione ENTER para continuar")
            else:
                print("No hay títulos cargados aún.")
                print("Por favor, elija la opción 1 para cargarlos y luego utilice esta función.")
                input("Presione ENTER para continuar")
        case "4": # Buscar titulos
            print(f'\n{separador}')
            print(f'Titulos en stock')
            print(f'{separador}')
            # Acá se me ocurrio listar los libros cargados para facilitar la busqueda
            if len(titulos) > 0:
                for i in range(len(titulos)):
                    print(f'Titulo {i + 1}: {titulos[i]}')
                print(f'{separador}')
            # Buscar por titulo, si lo encuentra mostrarlo y también cuantos ejemplares hay
            # Voy a reutilizar el formato del punto 3, para mostrar el titulo y cantidades.
            titulo_buscar = ""
            while titulo_buscar == "":
                titulo_buscar = input("Ingrese el nombre del título a buscar: ")
                if titulo_buscar == "":
                    print("Error. No ingreso nombre.")
                elif titulo_buscar not in titulos:
                    print("El título que busca no está en nuestro stock.")
                else:
                    for i in range(len(titulos)):
                        # lo paso a minuscula para evitar error de case sensitive con las mayusculas
                        if titulo_buscar == titulos[i]:
                            print(
                                f'\nLibro encontrado'
                                f'\nNombre del título: {titulos[i]}\n'
                            )
                            if ejemplares[i] == 0:
                                print(f'El libro no tiene copias disponibles.')
                            else:
                                print(f'El libro tiene {ejemplares[i]} copias disponibles.')

            print(f'{separador}')
            input("Presione ENTER para continuar")
        case "5": # Listar agotados
            print(f'\n{separador}')
            print('LISTAR AGOTADOS')
            print(f'{separador}')
            # Acá reutilizo el código de listar catalogo pero solo listo los que tengan cantidad = 0

            # Como lo voy a mostrar tipo tabla le hago una cabecera.
            if len(titulos) > 0:
                print("ID   Título                                            Ejemplares")
                print("-----------------------------------------------------------------")

                for i in range(len(titulos)):
                    # A las variables para que no me de error las paso a string por las dudas.
                    if ejemplares[i] == 0:
                        if i + 2  > 10:
                            num = str(i + 1)
                        else:
                            num = str(i + 1) + " "
                        titulo = titulos[i]
                        cantidad = str(ejemplares[i])

                        # Alineación básica  para que quede más prolijo
                        # (ajusto los espacios como para que entren bien la mayoria de los titulos)
                        # Esta fue la unica forma que encontre para tabular y que queden mas o menos bien, el problema es si el titulo tiene mas de 30 caracteres
                        if len(titulo) < 50:
                            espacios_titulo = " " * (50 - len(titulo))
                        else:
                            espacios_titulo = " "
                        espacios_num = " " * 4
                        print(f'{num}{espacios_num}{titulo}{espacios_titulo}{cantidad}')

                print(f'{separador}')


            else:
                print("No hay títulos cargados aún.")
                print("Por favor, elija la opción 1 para cargarlos y luego utilice esta función.")
            print(f'{separador}')
            input("Presione ENTER para continuar")
        case "6": # Agregar titulos
            print(f'\n{separador}')
            print("AGREGAR TITULOS")
            print(f'{separador}')
            nuevo_titulo = ""
            while nuevo_titulo == "":
                nuevo_titulo = input(f'Ingrese el nombre del libro a agregar: ')
                if nuevo_titulo != "":
                    if nuevo_titulo not in titulos:
                        titulos.append(nuevo_titulo)
                        print(f'\n{separador}'
                            f'\nIngrese la cantidad de ejemplares para el nuevo título: {nuevo_titulo}'
                            )

                        ejemplares_nuevo = -1
                        while ejemplares_nuevo < 0:
                            carga_ejemplare = input("- Ejemplares: ").strip()
                            if carga_ejemplare.isdigit():
                                ejemplares_nuevo = int(carga_ejemplare)
                                ejemplares.append(ejemplares_nuevo)
                            else:
                                print("Debe ingresar un número válido.")
                        print(f'\nSe agregó "{nuevo_titulo}" con {ejemplares_nuevo} ejemplares al catálogo.')
                        print(f'Su número de id es: {len(titulos)}')
                    else:
                        print(f'El título "{nuevo_titulo}" ya existe en el catálogo.')
                else:
                    print(f'\nERROR. No debe ingresar un nombre vacío.')
            input("Presione ENTER para continuar")
        case "7": # Actualizar ejemplares
            print(f'\n{separador}')
            print("ACTUALIZAR EJEMPLARES")
            print(f'{separador}')

            # Verifico que haya títulos cargados
            if len(titulos) == 0:
                print("No hay titulos cargados aún, por favor, elija la opción 1 para cargarlos y luego puede utilizar esta función.")
                input("Presione ENTER para continuar")
            else:
                # Selección por nombre o ID de título
                titulo_seleccionado = ""
                indice_titulo = -1

                while titulo_seleccionado == "":
                    # Cuando terminé de programar se me ocurrio usar los ID que vengo mostrando para hacer esta busqueda mas sencilla
                    titulo_seleccionado = input("Ingrese el nombre EXACTO del título que desea actualizar o su ID: ").strip()

                    if titulo_seleccionado == "":
                        print("Error. Nombre o ID vacío.")
                    # Acá evaluo si el STR que ingreso el usuario es un numero, si lo es, significa que ingresó un ID, no un nombre
                    elif titulo_seleccionado.isdigit():
                        id_ingresado = int(titulo_seleccionado)
                        # Valido que ese ID este en el rango de ids que tengo en la lista
                        if id_ingresado < 1 or id_ingresado > len(titulos):
                            print("Error: ID fuera de rango.")
                            # En caso de error reseteo la variable para que el bucle se siga ejecutando, es decir, el while se siga ejecutando y no se salga
                            titulo_seleccionado = ""
                        else:
                            print(f'\nIngresaste el ID {id_ingresado}.')
                            indice_titulo = id_ingresado - 1
                            # Acá busco el titulo por id - 1 pórque el id es uno mas que el indice de lista
                            # Luego lo sigo procesando como texto, como si el usuario hubiera ingresado correctamente elnombre del libro
                            titulo_seleccionado = titulos[indice_titulo]
                    # Si no ingreso un digito, ingresó un nombre, aca verifico si está en la lista, si no está muestro mensaje de error
                    elif titulo_seleccionado not in titulos:
                        print(f'El título "{titulo_seleccionado}" no se encuentra en el catálogo.')
                        titulo_seleccionado = ""

                    # Si la carga pasó todas las validaciones ya debo tener la variable correctamente cargada como para buscarla.
                    else:
                        # Guardo el índice del título seleccionado si se buscó por nombre
                        for i in range(len(titulos)):
                            if titulo_seleccionado == titulos[i]:
                                indice_titulo = i
                                break

                print(f'\n{separador}')
                print(f'Seleccionó: "{titulos[indice_titulo]}" - Stock actual: {ejemplares[indice_titulo]}')
                print(f'{separador}')
                print("1 - Registrar préstamo")
                print("2 - Registrar devolución")

                accion = ""
                while accion not in ["1", "2"]:
                    accion = input("Seleccione la acción a realizar (1-2): ").strip()

                # Dependiendo lo que ingrese el usuario...
                if accion == "1":
                    if ejemplares[indice_titulo] > 0:
                        ejemplares[indice_titulo] -= 1
                        print(f'\nPréstamo registrado correctamente.')
                        print(f'\nNuevo stock de "{titulos[indice_titulo]}": {ejemplares[indice_titulo]} ejemplares.')
                    else:
                        print(f'\nNo se puede registrar el préstamo porque este libro no tiene ejemplares disponibles')
                elif accion == "2":
                    ejemplares[indice_titulo] += 1
                    print(f'\nDevolución registrada correctamente.')
                    print(f'Nuevo stock de "{titulos[indice_titulo]}": {ejemplares[indice_titulo]} ejemplares.')

                print(f'{separador}')
                input("Presione ENTER para continuar")
        case "8": # Opcion salir
            print(f'\n{separador}')
            print(
                  f'Gracias por usar mi sistema.'
                  f'\nCodificado por Ezequiel Nieva')
            print(f'{separador}')
        case _: # Manejo de errores con opciones invalidas
            print("Opción no válida, volviendo al menú principal.")
