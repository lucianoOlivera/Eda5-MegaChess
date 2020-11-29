from const import Rook,Pawn,King,Knight,Queen,Bishop,Empty


class PieceValue(object):
    def value(self, name):
        if name is "p" or name is 'P':
            return Pawn
        elif name is "h" or name is 'H':
            return Knight
        elif name is "q" or name is 'Q':
            return Queen
        elif name is "k" or name is 'K':
            return King
        elif name is "r" or name is 'R':
            return Rook
        elif name is "b" or name is 'B':
            return Bishop
        elif name is " ":
            return Empty


