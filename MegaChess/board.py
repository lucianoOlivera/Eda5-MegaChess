import numpy as np
from factoryBoardPieces import FactoryBoardPieces


class Board:

    def __init__(self,board):
        self.board = board

    def boardGame(self):
        """crea un tablero a partir del board del turno"""
        boardGame=[]
        try:
            listboard = np.array([d for c,d in enumerate(self.board)]).reshape(16,16)
            for col,c in enumerate(listboard):
                for row,name in enumerate(c):
                    boardGame.append(FactoryBoardPieces().get_BoardPieces(col,row,name))
            return boardGame
        except Exception as e:
            print("wrong board size",e)

