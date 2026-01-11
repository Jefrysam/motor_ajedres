##crear tablero y posiciones
class tablero:
    def __init__(self):
        self.tablero = [ ["." for _ in range(8)] for _ in range(8)]
        self.tablero[0]= ["R", "N", "B", "Q", "K", "B", "N", "R"]
        self.tablero[1]= ["P", "P", "P", "P", "P", "P", "P", "P"]
        self.tablero[6]= ["p", "p", "p", "p", "p", "p", "p", "p"]
        self.tablero[7]= ["r", "n", "b", "q", "k", "b", "n", "r"]


    def mostrar_tablero(self):
        for fila in self.tablero:
            print(" ".join(fila)) 

tablero = tablero()
tablero.mostrar_tablero()