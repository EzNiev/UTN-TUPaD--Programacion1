"""
4) Dada una lista con valores repetidos:
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.

"""

datos_original = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_procesado = []

# Creo lista sin repetidos
for i in datos_original:
    if i not in datos_procesado:
        datos_procesado.append(i)

# Muestro lista original
print("\nLista original:")
for i in datos_original:
    print(f"- {i}")

# Muestro lista sin repetidos
print("\nLista sin repetidos:")
for i in datos_procesado:
    print(f"- {i}")
