# from biblioteca1 import Pila, Cola, Lista_Generica

# def estado_objetivo(puzzle):
#     return puzzle == [1,2,3,0]

# def obtener_vecinos(puzzle):
#     def intercambiar(puzzle, i, j):
#         """Intercambiar los valores en las posiciones i y j de la lista de puzzle"""
#         puzzle[i], puzzle[j] = puzzle[j], puzzle[i]
#         return puzzle
    
#     vecinos = []
#     pos_espacio = puzzle.index(0)
#     movimientos = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]} #Posibles movimientos para cada posicion

#     for mov in movimientos[pos_espacio]:
#         nuevo_puzzle = puzzle[:]
#         intercambiar(nuevo_puzzle, pos_espacio, mov)
#         vecinos.append(nuevo_puzzle)

#     return vecinos

# def resolucion_puzzle(puzzle):
#     pila = Pila()
#     pila.push((puzzle, [])) #(estado del puzzle, camino tomado)
#     visitados = set()
#     visitados.add(tuple(puzzle))

#     while not pila.esta_vacia():
#         estado_actual, camino = pila.pop()

#         if estado_objetivo(estado_actual):
#             return camino + [estado_actual]
        
#         for vecino in obtener_vecinos(estado_actual):
#             if tuple(vecino) not in visitados:
#                 visitados.add(tuple(vecino))
#                 pila.push((vecino, camino + [estado_actual]))

#     return None

# #Ejemplo de uso

# if __name__ == "__main__":
#     puzzle_inicial = [0,1,2,3]
#     solucion = resolucion_puzzle(puzzle_inicial)

#     if solucion:
#         print("Camino a la solucion")
#         for estado in solucion:
#             print(estado)
#         else:
#             print("No se encontro solucion")


# resolver_puzzle.py
from biblioteca1 import Pila

def es_estado_objetivo(puzzle):
    return puzzle == [1, 2, 3, 0]

def obtener_vecinos(puzzle):
    def intercambiar(puzzle, i, j):
        """Intercambia los valores en las posiciones i y j de la lista puzzle."""
        puzzle[i], puzzle[j] = puzzle[j], puzzle[i]
        return puzzle

    vecinos = []
    pos_espacio = puzzle.index(0)
    movimientos = {
        0: [1, 2],  # Movimiento posible desde la posición 0
        1: [0, 3],  # Movimiento posible desde la posición 1
        2: [0, 3],  # Movimiento posible desde la posición 2
        3: [1, 2]   # Movimiento posible desde la posición 3
    }

    for mov in movimientos[pos_espacio]:
        nuevo_puzzle = puzzle[:]
        intercambiar(nuevo_puzzle, pos_espacio, mov)
        vecinos.append(nuevo_puzzle)
    
    return vecinos

def dfs_resolver_puzzle(puzzle):
    pila = Pila()
    pila.apilar((puzzle, []))  # (estado del puzzle, camino tomado)
    visitados = set()
    visitados.add(tuple(puzzle))

    while not pila.esta_vacia():
        estado_actual, camino = pila.desapilar()

        if es_estado_objetivo(estado_actual):
            return camino + [estado_actual]

        for vecino in obtener_vecinos(estado_actual):
            if tuple(vecino) not in visitados:
                visitados.add(tuple(vecino))
                pila.apilar((vecino, camino + [estado_actual]))

    return None

# Ejemplo de uso
if __name__ == "__main__":
    puzzle_inicial = [1,0,2,3]  # Estado inicial
    solucion = dfs_resolver_puzzle(puzzle_inicial)

    if solucion:
        print("Camino a la solución:")
        for estado in solucion:
            print(estado)
    else:
        print("No se encontró solución.")
