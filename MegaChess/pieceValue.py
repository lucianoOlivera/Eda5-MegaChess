from const import(
    KING,
    ROOK,
    QUEEN,
    PAWN,
    BISHOP,
    KNIGHT,
    EMPTY)

class PieceValue(object):
    def value(self, name):
        """
        :param name: El nombre de la pieza
        :return: El valor de la pieza
        """
        if name is "p" or name is 'P':
            return PAWN
        elif name is "h" or name is 'H':
            return KNIGHT
        elif name is "q" or name is 'Q':
            return QUEEN
        elif name is "k" or name is 'K':
            return KING
        elif name is "r" or name is 'R':
            return ROOK
        elif name is "b" or name is 'B':
            return BISHOP
        elif name is " ":
            return EMPTY
