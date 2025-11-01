"""
PROGRAMACIÓN 1 - Segundo Parcial
Alumno: Nieva Gabriel Ezequiel
DNI: 41153456
"""

import os


def main():
    # Fuerzo la creacion del archivo para evitar errores.
    inicializado = os.path.exists("catalogo.csv")
    while True:
        print("\n--- MENÚ ---")
        # Opción 1 inicializa el archivo si no esta creado
        print("1 - Ingresar multiples títulos.")
        print("2 - Ingresar ejemplares")
        print("3 - Mostrar catálogo")
        print("4 - Consultar disponibilidad")
        print("5 - Listar agotados")
        print("6 - Agregar título")
        print("7 - Actualizar ejemplares (préstamo/devolución)")
        print("8 - Salir del programa")
        opcion = input("Seleccione una opción:\n> ")
        # Meto una validacion para forzar al usuario a crear el archivo
        if not inicializado and opcion != "1":
            print(
                "ERROR. Primero debe inicializar el archivo para poder usar las otras opciones. Elija Opcion 1 primero."
            )
            continue

        match opcion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida, intente otra vez.")


if __name__ == "__main__":
    main()
