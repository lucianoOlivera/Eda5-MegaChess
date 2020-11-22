##chess pieces
import numpy as np


class Pieces(object):
    def __init__ (self, row, col):
        self.row = row
        self.column = col


    def __str__ (self):
        return (
            f' row :{self.row}'
            f' colunm : {self.column}'
        )

    def set_position (self, row, col):
        self.row = row
        self.column = col


    def get_row (self):
        return str(self.row)


    def get_colunm (self):
        return str(self.column)


class King(Pieces):
    def __init__ (self, row, col, name):
        super().__init__(row, col)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + self.name

    def get_row (self):
        return super().get_row()

    def get_colunm (self):
        return super().get_colunm()


class Queen(Pieces):
    def __init__ (self, row, col, name):
        super().__init__(row, col)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)

    def get_row (self):
        return super().get_row()

    def get_colunm (self):
        return super().get_colunm()


class Rook(Pieces):
    def __init__ (self, row, col, name):
        super().__init__(row, col)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)

    def get_row (self):
        return super().get_row()

    def get_colunm (self):
        return super().get_colunm()


class Bishop(Pieces):
    def __init__ (self, row, col, name):
        super().__init__(row, col)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)

    def get_row (self):
        return super().get_row()

    def get_colunm (self):
        return super().get_colunm()


class Knight(Pieces):
    def __init__ (self, row, col, name):
        super().__init__(row, col)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)

    def get_row (self):
        return super().get_row()

    def get_colunm (self):
        return super().get_colunm()


class Pawn(Pieces):
    def __init__ (self, row, col, name):
        super().__init__(row, col )
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)

    def get_row (self):
        return super().get_row()

    def get_colunm (self):
        return super().get_colunm()


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

    def __init__ (self):
        self.board = np.arange(256)
        self.board = self.board.reshape((16, 16))

    def __str__(self):
        return self.board
