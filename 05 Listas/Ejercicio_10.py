"""
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana
"""

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas = []

# Cargar matriz 4x7
for i in range(4):
    print(f"\nProducto {i+1}")
    fila = []
    for j in range(len(dias)):
        venta = int(input(f"Total de ventas del producto {i+1} en el día {dias[j]}: "))
        fila.append(venta)
    ventas.append(fila)

# --- Total vendido por producto ---
totales_productos = []
for i in range(len(ventas)):
    suma = sum(ventas[i])
    totales_productos.append(suma)
    print("=" * 50)
    print(f"Total de ventas del producto {i+1}: {suma}")

# Producto mas vendido
cant_mas_vendido, mas_vendido = 0, ""

for i in range(len(ventas)):
    suma = sum(ventas[i])
    if suma > cant_mas_vendido:
        cant_mas_vendido = suma
        mas_vendido = i + 1
print(f"\nEl producto más vendido en la semana es el producto {mas_vendido}, con {cant_mas_vendido} unidades vendidas.")


# Dia con mayores ventas

dia_mas_ventas_sum = 0
dia_mas_ventas = ""
for i in range(len(ventas[0])):  # recorre los días
    suma = 0
    for j in range(len(ventas)):  # recorre los productos
        suma += ventas[j][i]      # sumo todas las ventas del día
    if suma > dia_mas_ventas_sum:
        dia_mas_ventas_sum = suma
        dia_mas_ventas = dias[i]

print(f"\nEl día con más ventas fue {dia_mas_ventas} con {dia_mas_ventas_sum} unidades vendidas.")
