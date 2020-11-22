import numpy as np

from core import Rook, Knight, Bishop, Queen, King, Pawn, Board
from strategy import Context, WhiteStrategy, BlackStrategy


class Game():
    def __init__ (self, board_id, turn_token, move_left) -> object:
        self.board_id = board_id
        self.turn_token = turn_token
        self.move_left = move_left

    def boardGame (self, board):
        lista = []
        for c, d in enumerate(board):
            lista.append(d)
        lista = np.array(lista)
        lista = lista.reshape(16, 16)
        listBoard = []
        for col, c in enumerate(lista):
            for row, a in enumerate(c):
                if a == "r":
                    rook = Rook(row, col, 'r')
                    listBoard.append(rook)
                elif a == 'h':
                    knight = Knight(row, col, 'k')
                    listBoard.append(knight)
                elif a == 'b':
                    bishop = Bishop(row, col, 'b')
                    listBoard.append(bishop)
                elif a == 'q':
                    queen = Queen(row, col, 'q')
                    listBoard.append(queen)
                elif a == 'k':
                    king = King(row, col, 'k')
                    listBoard.append(king)
                elif a == 'p':
                    pawn = Pawn(row, col, 'p')
                    listBoard.append(pawn)
                elif a == 'R':
                    rook = Rook(row, col, 'R')
                    listBoard.append(rook)
                elif a == 'H':
                    knight = Knight(row, col, 'H')
                    listBoard.append(knight)
                elif a == 'B':
                    bishop = Bishop(row, col, 'B')
                    listBoard.append(bishop)
                elif a == 'Q':
                    queen = Queen(row, col, 'Q')
                    listBoard.append(queen)
                elif a == 'K':
                    king = King(row, col, 'K')
                    listBoard.append(king)
                elif a == 'P':
                    pawn = Pawn(row, col, 'P')
                    listBoard.append(pawn)
        return listBoard

    def definestrategy (self, board):
        boardGame = self.boardGame(board)
        if self.turn_token == "white":
            ctx = Context(WhiteStrategy())
            ctx.strategyLogic(boardGame)
        elif self.turn_token == "black":
            ctx = Context(BlackStrategy())
            ctx.strategyLogic(boardGame)


a = Game("a", "white", "d")

board = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                        P       PPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
a.definestrategy(board)
