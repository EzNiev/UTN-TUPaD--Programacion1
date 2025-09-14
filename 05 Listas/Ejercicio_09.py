"""
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.
"""

# Inicializo tablero 3x3 lleno de guiones
tablero = [["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"]]

# Juego
jugadores = ["X", "O"]

for turno in range(9):  # máximo 9 jugadas
    jugador = jugadores[turno % 2]
    print(f"Turno del jugador {jugador}")

    # Muestro el tablero en cada turno
    for fila in tablero:
        print(" ".join(fila))
    print()


    # Pedir posición válida
    while True:
        fila = int(input("Ingrese fila (0-2): "))
        col = int(input("Ingrese columna (0-2): "))

        # El siguiente condicional es el dificil, verifico que no se salga de rango la posicion y que donde se vaya a grabar una X u O sea una posicial que tenga un -, para asegurarme de que no se usó todavia
        if (0 <= fila < 3) and (0 <= col < 3) and tablero[fila][col] == "-":
            tablero[fila][col] = jugador
            break
        else:
            print("Posición inválida, intente otra vez.")

for fila in tablero:
        print(" ".join(fila))

print("Juego finalizado.")
