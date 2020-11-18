##chess pieces
import numpy as np


class Pieces(object):
    def __init__ (self, row, col, flag):
        self.row = row
        self.column = col
        self.colour = flag

    def __str__ (self):
        return (
            f' row :{self.row}'
            f' colunm : {self.column}'
            f' colorur : {self.colour}'
        )

    def set_position (self, row, col):
        self.row = row
        self.column = col

    @property
    def get_row (self):
        return self.row

    @property
    def get_colunm (self):
        return self.column


class King(Pieces):
    def __init__ (self, row, col, flag, name):
        super().__init__(row, col, flag)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + self.name


class Queen(Pieces):
    def __init__ (self, row, col, flag, name):
        super().__init__(row, col, flag)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)


class Castle(Pieces):
    def __init__ (self, row, col, flag, name):
        super().__init__(row, col, flag)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)


class Bishop(Pieces):
    def __init__ (self, row, col, flag, name):
        super().__init__(row, col, flag)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)


class Knight(Pieces):
    def __init__ (self, row, col, flag, name):
        super().__init__(row, col, flag)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)


class Pawn(Pieces):
    def __init__ (self, row, col, flag, name):
        super().__init__(row, col, flag)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)


# move

def moveLine (movementN, dir, obj):
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
    return col, row


"""
    rrhhbbqqkkbbhhrr
    rrhhbbqqkkbbhhrr

                
                      
                        
          ↑ 
          Q →
    RRHHBB QKKBBHHRR
    RRHHBBQQKKBBHHRR

"""


def moveDiagonal (movementN, dir, obj):
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
    return row, col


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


def moveSpecial (movementN1, movementN2, dir1, dir2, obj):
    row = obj.get_row
    col = obj.get_row
    name = obj.name
    if name == "P" or "p":
        if dir1 == 'up':
            col += movementN1
        return row, col
    # other special movements
    return row, col


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

    def __init__ (self, board):
        self.board = np.arange(256)
        self.board = self.board.reshape((16, 16))

