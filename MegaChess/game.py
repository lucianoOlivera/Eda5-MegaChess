import numpy as np

from core import Rook, Knight, Bishop, Queen, King, Pawn
from strategy import Context, WhiteStrategy, BlackStrategy


class Game():
    def __init__ (self, board_id, turn_token, move_left) -> object:
        self.board_id = board_id
        self.turn_token = turn_token
        self.move_left = move_left

    def boardGame(self, board):
        """     i = 0
                    arr = []
                    listBoard =[]
                    for s, v in enumerate(board):
                        listBoard.append(v)
                    for row in range(0, 16):
                        for col in range(0, 16):
                            print(i)
                            if listBoard[i] == 'r':
                                i += 1
                                rook = Rook(row, col, 'r')
                                arr.append(rook)
                            elif listBoard[i] == 'h':
                                pass
                            elif listBoard[i] == 'b':
                                pass
                            elif listBoard[i] == 'q':
                                pass
                            elif listBoard[i] == 'k':
                                pass
                            elif listBoard[i] == 'p':
                                pass
                            elif listBoard[i] == 'R':
                                pass
                            elif listBoard[i] == 'H':
                                pass
                            elif listBoard[i] == 'B':
                                pass
                            elif listBoard[i] == 'Q':
                                pass
                            elif listBoard[i] == 'K':
                                pass
                            elif listBoard[i] == 'P':
                                pass

                                i += 1

                    return arr"""
        listBoard = []
        for row, c in enumerate(board):
            for col, a in enumerate(c):
                if a == "r":
                    rook = Rook(row,col,'r')
                    listBoard.append(rook)
                elif a == 'h':
                    knight = Knight(row,col,'k')
                    listBoard.append(knight)
                elif a == 'b':
                    bishop = Bishop(row,col,'b')
                    listBoard.append(bishop)
                elif a == 'q':
                    queen = Queen(row,col,'q')
                    listBoard.append(queen)
                elif a == 'k':
                    king = King(row,col,'k')
                    listBoard.append(king)
                elif a == 'p':
                    pawn = Pawn(row,col,'p')
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


    def definestrategy (self,board):
        boardGame = self.boardGame(board)
        if self.turn_token == "white":
            ctx = Context(WhiteStrategy())
            ctx.strategyLogic(boardGame)
        elif self.turn_token == "black":
            ctx = Context(BlackStrategy())
            ctx.strategyLogic(boardGame)


a = Game("a","white","d")

board = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                        P       PPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
s = a.definestrategy(board)


