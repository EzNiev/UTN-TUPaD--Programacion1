"""
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.
"""

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temp = []

for dia in dias:
    t_min = float(input(f"Ingrese la temperatura mínima del día {dia}: "))
    t_max = float(input(f"Ingrese la temperatura máxima del día {dia}: "))
    temp.append([t_min, t_max])

# Calcular promedios y amplitud
suma_min, suma_max, amplitud = 0, 0, 0
dia_may_amplitud = 0

for i in range(len(temp)):
    suma_min += temp[i][0]
    suma_max += temp[i][1]
    if amplitud < (temp[i][1] - temp[i][0]):
        amplitud = temp[i][1] - temp[i][0]
        dia_may_amplitud = i

# Mostrar resultados
print(f'\nPromedio de temperaturas mínimas: {suma_min / len(temp)}°'
      f'\nPromedio de temperaturas máximas: {suma_max / len(temp)}°'
      f'\nDía de mayor amplitud: {dias[dia_may_amplitud]}'
      f'\nAmplitud de temperatura de ese día: {amplitud}°')
