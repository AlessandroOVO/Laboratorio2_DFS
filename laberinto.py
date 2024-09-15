# resolver_labirinto.py
from biblioteca1 import Pila

def es_valido(maze, visitado, fila, columna):
    """Verifica si la posición (fila, columna) es válida para moverse."""
    filas = len(maze)
    columnas = len(maze[0])
    return (0 <= fila < filas and 0 <= columna < columnas and
            maze[fila][columna] == 0 and not visitado[fila][columna])

def dfs_labirinto(maze, start, end):
    filas = len(maze)
    columnas = len(maze[0])
    pila = Pila()
    visitado = [[False] * columnas for _ in range(filas)]
    pila.apilar((start, [start]))  # (posición actual, camino tomado)

    while not pila.esta_vacia():
        (fila, columna), camino = pila.desapilar()

        if (fila, columna) == end:
            return camino

        if not visitado[fila][columna]:
            visitado[fila][columna] = True

            # Movimientos posibles: abajo, arriba, derecha, izquierda
            movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for df, dc in movimientos:
                nueva_fila, nueva_columna = fila + df, columna + dc
                if es_valido(maze, visitado, nueva_fila, nueva_columna):
                    pila.apilar(((nueva_fila, nueva_columna), camino + [(nueva_fila, nueva_columna)]))

    return None

# Ejemplo de uso
if __name__ == "__main__":
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]
    start = (0, 1)
    end = (3, 4)
    solucion = dfs_labirinto(maze, start, end)

    if solucion:
        print("Camino a la solución:")
        for paso in solucion:
            print(paso)
    else:
        print("No se encontró solución.")
