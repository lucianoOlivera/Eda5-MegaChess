from const import King,Rook,Queen,Pawn,Bishop,Knight,Empty
from pieceValue import PieceValue


class PiecesStrategy(object):
    def __init__(self,board):
        self.board = board

    def moves(self):
        raise NotImplementedError

    def movesAtack(self):
        raise NotImplementedError


class MoveScore():
    def moveScore(self,board,name):
        if board.get_name() is 'p' or board.get_name() is 'P':
            scorePiece = PieceValue().value(name)
            return Pawn + scorePiece
        elif board.get_name() is 'h' or board.get_name() is 'H':
            scorePiece = PieceValue().value(name)
            return Knight + scorePiece
        elif board.get_name() is 'q' or board.get_name() is 'Q':
            scorePiece = PieceValue().value(name)
            return Queen + scorePiece
        elif board.get_name() is 'r' or board.get_name() is 'R':
            scorePiece = PieceValue().value(name)
            return Rook + scorePiece
        elif board.get_name() is 'b' or board.get_name() is 'B':
            scorePiece = PieceValue().value(name)
            return Bishop + scorePiece
        elif board.get_name() is 'K' or board.get_name() is 'k':
            scorePiece = PieceValue().value(name)
            return Knight + scorePiece

    def highScore(self,listMovesScore):
        highScore = 0
        moveHighScore = []
        for i,c in enumerate(listMovesScore):
            for w,j in enumerate(c):
               if j[4] > highScore:
                   highScore = j[4]
                   moveHighScore = j
        return moveHighScore

