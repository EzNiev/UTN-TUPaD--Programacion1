"""
5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.
"""
estudiantes = []
modificar = True

for i in range(3):
    print("=" * 60)
    estudiantes.append(input(f"Ingrese el nombre del estudiante {i+1}: "))

while modificar:
    print("=" * 60)
    print("\nListado actual")
    for i in estudiantes:
        print(f"- {i}")
    print('\n¿Desea agregar un nuevo estudiante o eliminar uno?'
          '\n 1- Agregar un nuevo estudiante.'
          '\n 2- Eliminar uno.'
          '\n 3- No hacer nada.'
          )
    opcion = input("Elección:")
    if opcion == '1':
        nombre = input("Ingrese el nombre del alumno a agregar: ")
        estudiantes.append(nombre)
    elif opcion == '2':
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        if nombre in estudiantes:
            estudiantes.remove(nombre)
        else:
            print("*" * 50)
            print("Ese alumno no existe en el listado.")
            print("*" * 50)
            input("Presione enter para continuar.")
    else:
        print("Decidió no modificar la lista.")
        modificar = False
