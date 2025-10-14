def calcular_precio_final(precio, descuento=0):
    precio_final = precio - (precio * descuento / 100)
    return round(precio_final, 2)


resultado = calcular_precio_final(120, 15)
print(resultado)
