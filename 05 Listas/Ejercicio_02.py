"""
Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""

productos = []

# Cargo los productos
for i in range(5):
    carga = input(f"Por favor ingrese el nombre del producto {i+1} a cargar: ")
    productos.append(carga)

# Ordeno la lista y la muestro
productos.sort()
print("Lista de productos ordenada:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]}")

# Pregunto qué producto eliminar
eliminar = 0
while eliminar < 1 or eliminar > len(productos):
    eliminar = int(input(f"Ingrese el número de producto que desea eliminar: "))

# Elimino el producto por índice
print(f"Se procede a eliminar el producto {eliminar} - {productos[eliminar - 1]}")
productos.remove(productos[eliminar - 1])

# Muestro la lista actualizada
print("Lista de productos actualizada:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]}")
