##chess pieces

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


class King(Pieces):
    def __init__ (self, row, col, flag, name):
        super().__init__(row, col, flag)
        self.name = name

    def __str__ (self):
        return super().__str__() + " name: " + str(self.name)


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



