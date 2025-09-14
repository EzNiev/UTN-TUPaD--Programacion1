"""
8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.
"""
# Inicializo matriz vacía
notas = []

# Cargar notas de 5 estudiantes en 3 materias
for i in range(5):
    # Variable auxiliar para crear la minilista, que va a ser el indice 0 en la lista mayor
    fila = []
    print(f"\nEstudiante {i+1}:")
    # Ciclo para cargar 3 notas en este estudiante
    for j in range(3):
        nota = float(input(f"Ingrese la nota de la materia {j+1}: "))
        fila.append(nota)
    #Cuando el usuario ya ingreso 3 notas se sale del for chico y se guardan esa lista de 3 elementos en el indice 0 de la lista mayor
    notas.append(fila)

print("\nMatriz de notas:")
for fila in notas:
    print(fila)

# Promedio por estudiante (fila)
print("\nPromedio de cada estudiante:")
for i in range(5):
    promedio_estudiante = sum(notas[i]) / 3
    print(f"Estudiante {i+1}: {promedio_estudiante}")

# Promedio por materia (columna)
print("\nPromedio de cada materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio_materia = suma / 5
    print(f"Materia {j+1}: {promedio_materia}")
