from const import (
    KING,
    ROOK,
    QUEEN,
    PAWN,
    BISHOP,
    KNIGHT,
    EMPTY)
from pieceValue import PieceValue


class PiecesStrategy(object):
    def __init__(self,board):
        self.board = board

    def moves(self):
        raise NotImplementedError

    def movesAtack(self):
        raise NotImplementedError


def highScore(listMovesScore):
    """
    Resuelve cuál es el movimiento con mayor puntaje

    Devuelve un movimiento

    Parámetro
    listMovesScore ---> Lista de todos los movimientos del turno

    """

    highScoreMove = 0
    moveHighScore = []
    for i,c in enumerate(listMovesScore):
        for w,j in enumerate(c):
            if j[4]>highScoreMove:
                highScoreMove = j[4]
                moveHighScore = j
    return moveHighScore


class MoveScore():
    def moveScore(self,piece,name):
        """
        Resuelve el puntaje del movimiento

        Devuelve el puntaje del movimiento

        Parámetro
        piece----> Pieza que hará el movimiento
        name----> El nombre de la pieza que comerá en caso que sea enemigo

        """
        if piece.get_name() is 'p' or piece.get_name() is 'P':
            scorePiece = PieceValue().value(name)
            return PAWN + scorePiece
        elif piece.get_name() is 'h' or piece.get_name() is 'H':
            scorePiece = PieceValue().value(name)
            return KNIGHT + scorePiece
        elif piece.get_name() is 'q' or piece.get_name() is 'Q':
            scorePiece = PieceValue().value(name)
            return QUEEN + scorePiece
        elif piece.get_name() is 'r' or piece.get_name() is 'R':
            scorePiece = PieceValue().value(name)
            return ROOK + scorePiece
        elif piece.get_name() is 'b' or piece.get_name() is 'B':
            scorePiece = PieceValue().value(name)
            return BISHOP + scorePiece
        elif piece.get_name() is 'K' or piece.get_name() is 'k':
            scorePiece = PieceValue().value(name)
            return KING + scorePiece