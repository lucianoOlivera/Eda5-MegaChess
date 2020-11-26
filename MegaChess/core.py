##chess pieces
import numpy as np


class Pieces(object):
    def __init__(self,row,col,name):
        self.row = row
        self.column = col
        self.name = name

    def __str__(self):
        return f'row : {self.row} col = {self.column} name: {self.name}'

    def set_position(self,row,col):
        self.row = row
        self.column = col

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


class King(Pieces):
    pass


class Queen(Pieces):
    pass


class Rook(Pieces):
    pass


class Bishop(Pieces):
    pass


class Knight(Pieces):
    pass


class Pawn(Pieces):
    pass


class Empty(Pieces):
    pass


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


"""
    rrhhbbqqkkbbhhrr
    rrhhbbqqkkbbhhrr

                
                      
                        
          ↑ 
          Q →
    RRHHBB QKKBBHHRR
    RRHHBBQQKKBBHHRR

"""


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


"""
    rrhhbbqqkkbbhhrr
    rrhhbbqqkkbbhhrr

                
              ↔            
            ↔                
          ↔
        H   
    RRH BBQKKBBHHRR
    RRHHBBQQKKBBHHRR
"""


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


"""
two movements
pppppppppppppppp
pppppppppppppppp
                
                
                
                
                
     P            5
     ↑          

PPPP PPPPPPPPPPP    
PPPPPPPPPPPPPPPP

"""


# board

class Board:

    def __init__(self):
        self.board = np.arange(256)
        self.board = self.board.reshape((16,16))

    def __str__(self):
        return self.board



a = King(12,34,'k')

print(a)