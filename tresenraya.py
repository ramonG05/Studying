def imprimir_tablero(tablero):
    """Imprime el tablero de juego actual."""
    print("\n")
    for i in range(3):
        print(" | ".join(tablero[i]))
        if i < 2:
            print("-" * 9)
    print("\n")

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador ha ganado."""
    # Verificar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
    
    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    
    return False

def tablero_lleno(tablero):
    """Verifica si el tablero está lleno."""
    for fila in tablero:
        if " " in fila:
            return False
    return True

def jugar_tres_en_raya():
    """Función principal del juego."""
    print("¡Bienvenido al juego de Tres en Raya!")
    print("Para jugar, ingresa las coordenadas (fila,columna) del 1 al 3.")
    
    # Inicializar tablero vacío
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    
    # Determinar quién comienza
    jugador_actual = "X"
    
    while True:
        # Mostrar tablero
        imprimir_tablero(tablero)
        
        # Pedir movimiento al jugador
        print(f"Turno del jugador {jugador_actual}")
        
        while True:
            try:
                fila = int(input("Ingresa el número de fila (1-3): ")) - 1
                columna = int(input("Ingresa el número de columna (1-3): ")) - 1
                
                # Verificar coordenadas válidas
                if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                    print("¡Coordenadas fuera de rango! Intenta de nuevo.")
                    continue
                
                # Verificar si la celda está vacía
                if tablero[fila][columna] != " ":
                    print("¡Esa celda ya está ocupada! Intenta de nuevo.")
                    continue
                
                break
            except ValueError:
                print("¡Entrada inválida! Ingresa números del 1 al 3.")
        
        # Realizar movimiento
        tablero[fila][columna] = jugador_actual
        
        # Verificar si hay ganador
        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break
        
        # Verificar si hay empate
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate! El tablero está lleno.")
            break
        
        # Cambiar de jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"
    
    print("¡Gracias por jugar!")

# Iniciar el juego si este archivo se ejecuta directamente
if __name__ == "__main__":
    jugar_tres_en_raya()