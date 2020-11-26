##chess pieces
import numpy as np
from factoryBoardPieces import Factory
# move
def moveLine(movementN,dir,obj):
    row = obj.get_row
    col = obj.get_row
    if dir == 'up':
        row -= movementN
    elif dir == 'down':
        row += movementN
    elif dir == 'rigth':
        col += movementN
    elif dir == 'left':
        col -= movementN
    return col,row


def moveDiagonal(movementN,dir,obj):
    row = obj.get_row
    col = obj.get_row
    if dir == 'rd':  # (right diagonal up)
        row -= movementN
        col += movementN
    elif dir == 'ldd':  # (left diagonal up)
        row -= movementN
        col -= movementN
    elif dir == 'dr':  # (right diagonal down)
        row += movementN
        col += movementN
    elif dir == 'dl':  # (left diagonal down)
        row += movementN
        col -= movementN
    return row,col


def moveSpecial(movementN1,movementN2,dir1,dir2,obj):
    row = obj.get_row
    col = obj.get_row
    name = obj.name
    if name == "P" or "p":
        if dir1 == 'up':
            col += movementN1
        return row,col
    # other special movements
    return row,col


# board

class Board:

    def __init__(self,board):
        self.board = board

    def __str__(self):
        return self.board

    def boardGame(self):
        lista = []
        for c,d in enumerate(self.board):
            lista.append(d)
        lista = np.array(lista)
        lista = lista.reshape(16,16)
        for col,c in enumerate(lista):
            for row,a in enumerate(c):
                my_Factory = Factory()
                my_Factory.get_BoardPices(row, col, a)


board = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                        P       PPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
c = Board(board)
c.boardGame()
