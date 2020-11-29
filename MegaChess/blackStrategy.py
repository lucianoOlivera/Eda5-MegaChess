from strategyColour import StrategyChess
from piecesStrategy import PiecesStrategy,MoveScore


class BlackStrategy(StrategyChess):

    def strategyClassLogic(self,board):
        listMoves = [PawnBlack(board).moves(),PawnBlack(board).movesAtack()]
        listMoves.remove([])
        listHighScore = MoveScore().highScore(listMoves)
        print(listHighScore)


class PawnBlack(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "p" and self.board[i + 16].get_name() == " ":
                score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                moves.append(
                    [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),self.board[i + 16].get_column(),score])
                if self.board[i + 32].get_name() == " " and (self.board[i].row == 2 or self.board[i].row == 3):
                    score = MoveScore().moveScore(self.board[i],self.board[i + 32].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 32].get_row(),
                         self.board[i + 32].get_column(),score])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_column() == 0 and self.board[i].get_row() < 9:
                if self.board[i + 17].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                         self.board[i + 17].get_column(),score])
            elif self.board[i].get_column() == 15 and self.board[i].get_row() < 9:
                if self.board[i + 15].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                         self.board[i + 15].get_column(),score])
            else:
                if self.board[i].get_row() < 9:
                    if self.board[i + 17].get_colour() == "white":
                        score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                             self.board[i + 17].get_column(),score])
                elif self.board[i].get_row() < 9:
                    if self.board[i + 15].get_colour() == "white":
                        score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                             self.board[i + 15].get_column(),score])
        return movesAtack
