##chess pieces

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

    def get_name(self):
        return self.name


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
