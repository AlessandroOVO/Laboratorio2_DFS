from collections import deque    

class Lista_Generica:
    def __init__(self):
        self.items = []
    
    def lista_vacia(self):
        return len(self.items) == 0
    
    def agregar(self, item,indice):
        if indice < 0 or indice > len(self.items):
            raise IndexError("Indice fuera de rango")
        self.items.insert(indice, item)

    def eliminar(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError("Elemento no encontrado en la cola")
    
    def obtener(self, indice):
        if 0 <= indice < len(self.items):
            return self.items[indice]
        raise IndexError("Indice fuera de rango")
  
    def tamaño(self):
        return len(self.items)
  
    def __repr__(self):
        return f"Lista Generica({self.items})"
    


class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("Desapilar desde una pila vacía")
        return self.items.pop()

    def cima(self):
        if self.esta_vacia():
            raise IndexError("Ver la cima de una pila vacía")
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Pila({self.items})"


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("Desencolar desde una cola vacía")
        return self.items.pop(0)

    def frente(self):
        if self.esta_vacia():
            raise IndexError("Ver el frente de una cola vacía")
        return self.items[0]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Cola({self.items})"
