# TP6 – Estructuras de datos complejas
# =====================================================================
# 1) Dado el diccionario precios_frutas:
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# • Naranja = 1200
# • Manzana = 1500
# • Pera = 2300
# =====================================================================

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print("1) Diccionario actualizado con nuevas frutas:")
print(precios_frutas)
print()

# =====================================================================
# 2) Siguiendo con el diccionario anterior, actualizar los precios:
# • Banana = 1330
# • Manzana = 1700
# • Melón = 2800
# =====================================================================

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("2) Diccionario con precios actualizados:")
print(precios_frutas)
print()

# =====================================================================
# 3) Crear una lista que contenga únicamente las frutas (sin los precios).
# =====================================================================

lista_nombre_frutas = []

for fruta in precios_frutas:
    lista_nombre_frutas.append(fruta)

print("3) Lista de frutas sin precios:")
print(lista_nombre_frutas)
print()

# =====================================================================
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# =====================================================================

agenda = {}
print("4) Carga de contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input("Ingrese el número de teléfono: ")
    agenda[nombre] = numero

buscar = input("Ingrese el nombre a buscar: ")
if buscar in agenda:
    print(f"El número de {buscar} es {agenda[buscar]}")
else:
    print("No se encontró ese contacto.")
print()

# =====================================================================
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# =====================================================================

frase = input("5) Ingrese una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)

dicc_palabras = {}
for palabra in palabras:
    dicc_palabras[palabra] = dicc_palabras.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Cantidad de apariciones:", dicc_palabras)
print()

# =====================================================================
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# =====================================================================

alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("Promedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
print()

# =====================================================================
# 7) Dado dos sets de números, representando estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrar los que aprobaron ambos parciales.
# • Mostrar los que aprobaron solo uno de los dos.
# • Mostrar la lista total de los que aprobaron al menos uno (sin repetir).
# =====================================================================

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

print("7) Alumnos:")
print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)
print()

# =====================================================================
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
# =====================================================================

stock = {"Mouse": 10, "Teclado": 5, "Monitor": 2}
producto = input("Ingrese producto a consultar: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades desea agregar? (0 para ninguna): "))
    stock[producto] += agregar
else:
    print("Producto no encontrado, se agregará nuevo.")
    unidades = int(input("Ingrese cantidad inicial: "))
    stock[producto] = unidades

print("Stock actualizado:", stock)
print()

# =====================================================================
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
# =====================================================================

agenda_eventos = {
    ("Lunes", "10:00"): "Asado",
    ("Martes", "14:00"): "Basquet",
    ("Viernes", "18:00"): "Boliche",
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (ej. 10:00): ")

evento = agenda_eventos.get((dia, hora), "No hay actividad registrada.")
print(f"En {dia} a las {hora}: {evento}")
print()

# =====================================================================
# 10) Dado un diccionario que mapea nombres de países con sus capitales,
# construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima"}

# diccionario auxiliar
capitales = {}

for pais in paises:
    # guardola capital
    capital = paises[pais]
    # invierto clave y valor
    capitales[capital] = pais

print("10) Diccionario invertido (capitales como clave):")
print(capitales)
print()
