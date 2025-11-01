import os


# 1. Crear archivo inicial
def crear_archivo():
    if not os.path.exists("productos.txt"):
        with open("productos.txt", "w") as archivo:
            archivo.write("Lapicera,120.5,30\n")
            archivo.write("Cuaderno,500,15\n")
            archivo.write("Goma,80,50\n")
    print("1 - Archivo creado correctamente.\n")


# 2. Leer archivo y mostrar productos
def leer_archivo():
    print("\n2 - Lectura del archivo.")
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# 3. Agregar un nuevo producto. No trabaja en memoria, modifica directamente el archivo tal como pide la consigna
def agregar_producto():
    print("\n3 - Agregar un nuevo producto.")
    with open("productos.txt", "a") as archivo:
        nombre = input("Nombre del producto:\n> ")
        # Valido un poco la entrada de datos.
        try:
            precio = float(input("Precio:\n> "))
            cantidad = int(input("Cantidad:\n> "))
        except ValueError:
            print("ERROR: Debe ingresar números válidos.")
            return
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado correctamente.")


# 4. Cargar productos en una lista de diccionarios. Esto trabaja con un diccionario en memoria y no modifica el archivo.
def cargar_diccionarios():
    print("\n4 - Cargar productos en una lista de diccionarios.")
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad),
            }
            productos.append(producto)

    print("\nLista de productos en memoria (diccionarios):")
    for p in productos:
        print(p)
    return productos


# 5. Buscar producto por nombre
def buscar_producto(diccionario_productos):
    print("\n5 - Buscar producto por nombre.")
    nombre_buscar = input("Ingrese el nombre del producto a buscar:\n> ").strip()
    for producto_buscado in diccionario_productos:
        if nombre_buscar.lower() == producto_buscado["nombre"].lower():
            print("Producto encontrado!")
            print(
                f"Producto: {producto_buscado['nombre']} | Precio: ${producto_buscado['precio']} | Cantidad: {producto_buscado['cantidad']}"
            )
            return producto_buscado

    print("ERROR. El producto no fue encontrado en la lista.")
    return None


# 6. Guardar productos desde lista al archivo (sobrescribir)
def guardar_archivo(productos):
    print("\n6 - Guardar productos en el archivo.")
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo sobrescrito correctamente con los datos actualizados.")


# ------ MENÚ PRINCIPAL ------
def main():
    # Fuerzo la creacion del archivo para evitar errores.
    inicializado = os.path.exists("productos.txt")
    dicc_productos = []
    while True:
        print("\n--- MENÚ ---")
        print("1 - Inicializar Archivo")
        print("2 - Mostrar productos")
        print("3 - Agregar producto")
        print("4 - Cargar productos en diccionarios")
        print("5 - Buscar producto")
        print("6 - Guardar modificaciones en archivo")
        print("7 - Salir")
        opcion = input("Seleccione una opción:\n> ")
        # Meto una validacion para forzar al usuario a crear el archivo
        if not inicializado and opcion != "1":
            print(
                "ERROR. Primero debe inicializar el archivo para poder usar las otras opciones. Elija Opcion 1 primero."
            )
            continue

        try:
            match opcion:
                case "1":
                    crear_archivo()
                    inicializado = True
                case "2":
                    leer_archivo()
                case "3":
                    agregar_producto()
                case "4":
                    dicc_productos = cargar_diccionarios()
                case "5":
                    if dicc_productos == []:
                        dicc_productos = cargar_diccionarios()
                        print(
                            "La lista de productos en memoria no habia sido generada pero ahora se generó automaticamente (opcion 4)."
                        )
                    buscar_producto(dicc_productos)
                case "6":
                    guardar_archivo(dicc_productos)
                case "7":
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
