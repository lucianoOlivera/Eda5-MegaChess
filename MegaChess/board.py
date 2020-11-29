import numpy as np
from factoryBoardPieces import Factory


class Board:

    def __init__(self,board):
        self.board = board

    def __str__(self):
        return self.board

    def boardGame(self):
        lista = []
        for c, d in enumerate(self.board):
            lista.append(d)
        lista = np.array(lista)
        lista = lista.reshape(16,16)
        listBoard = []
        for col, c in enumerate(lista):
            for row, a in enumerate(c):
                my_Factory = Factory()
                pieces = my_Factory.get_BoardPieces(col,row,a)
                listBoard.append(pieces)
        return listBoard

