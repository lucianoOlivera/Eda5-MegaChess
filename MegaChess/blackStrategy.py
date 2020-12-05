from strategyColour import StrategyChess
from piecesStrategy import PiecesStrategy,MoveScore
from movesBoard import MovesBoard


class BlackStrategy(StrategyChess):

    def strategyClassLogic(self,board):
        listMoves = [QueenBlack(board).movesAtack(),QueenBlack(board).moves(),
                     PawnBlack(board).moves(),PawnBlack(board).movesAtack(),KingBlack(board).moves(),
                     KingBlack(board).movesAtack(),RookBlack(board).moves(),RookBlack(board).movesAtack(),
                     BishopBlack(board).moves(),BishopBlack(board).movesAtack()]

        listHighScore = MoveScore().highScore(listMoves)
        from_row = listHighScore[0]
        from_col = listHighScore[1]
        to_row = listHighScore[2]
        to_col = listHighScore[3]
        listMoves =RookBlack(board).movesAtack()
        print(listMoves)
        return from_row,from_col,to_row,to_col


class PawnBlack(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "p" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i + 16].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),
                         self.board[i + 16].get_column(),score])
                    if self.board[i + 32].get_name() == " " and (self.board[i].row == 2 or self.board[i].row == 3):
                        score = MoveScore().moveScore(self.board[i],self.board[i + 32].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 32].get_row(),
                             self.board[i + 32].get_column(),score+1])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "p" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i + 17].get_colour() == "white":
                        score = MoveScore().moveScore(self.board[i],self.board[i+17].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             self.board[i+17].get_row(),
                             self.board[i+17].get_column(),score])
                if self.board[i + 15].get_colour() == "white":
                        score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             self.board[i + 15].get_row(),
                             self.board[i + 15].get_column(),score])
        return movesAtack


class QueenBlack(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "q" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i + 16].get_name() == " ":
                    spaceUp = MovesBoard().moveLine("up",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceUp[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceUp[0].get_row(),spaceUp[0].get_column(),score])
                if self.board[i - 16].get_name() == " ":
                    spaceDown = MovesBoard().moveLine("down",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceDown[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceDown[0].get_row(),spaceDown[0].get_column(),score])
                if self.board[i + 1].get_name() == " " :
                    spaceRight = MovesBoard().moveLine("right",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRight[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRight[0].get_row(),spaceRight[0].get_column(),score])
                if self.board[i - 1].get_name() == " ":
                    spaceLeft = MovesBoard().moveLine("left",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceLeft[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceLeft[0].get_row(),spaceLeft[0].get_column(),score])
                if self.board[i + 17].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("rd",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                         spaceRD[0].get_column(),score])
                if self.board[i + 15].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("ldd",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                         spaceRD[0].get_column(),score])
                if self.board[i - 17].get_name() == " ":
                    spaceDR = MovesBoard().moveDiagonal("dl",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceDR[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceDR[0].get_row(),
                         spaceDR[0].get_column(),score])
                if self.board[i - 15].get_name() == " " :
                    spaceRD = MovesBoard().moveDiagonal("dr",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                         spaceRD[0].get_column(),score])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "q" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i+16].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i +16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i +16].get_row(),
                         self.board[i +16].get_column(),score])
                elif self.board[i+16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("up",self.board,self.board[i+16],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 16].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),self.board[i - 16].get_column(),score])
                elif self.board[i - 16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("down",self.board,self.board[i - 16],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i + 1].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                         self.board[i + 1].get_column(),score])
                elif self.board[i+ 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("right",self.board,self.board[i + 1],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 1].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                         self.board[i - 1].get_column(),score])
                elif self.board[i - 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("left",self.board,self.board[i - 1],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i + 17].get_colour() == "white":
                        score=MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             self.board[i + 17].get_row(), self.board[i + 17].get_column(),score])
                elif self.board[i + 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("rd",self.board,self.board[i+17],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i + 15].get_colour() == "white":
                    score=MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 15].get_row(),self.board[i + 15].get_column(),score])
                elif self.board[i + 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("ldd",self.board,self.board[i + 15],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 17].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 17].get_row(),self.board[i - 17].get_column(),score])
                elif self.board[i - 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dl",self.board,self.board[i - 17],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 15].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 15].get_row(),self.board[i - 15].get_column(),score])
                elif self.board[i - 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dr",self.board,self.board[i - 15],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),space[0].get_column(),score])
        return movesAtack


class KingBlack(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "k" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                     if self.board[i + 16].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),
                             self.board[i + 16].get_column(),score])
                     if self.board[i - 16].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                             self.board[i - 16].get_column(),score])
                     if  self.board[i + 1].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                             self.board[i + 1].get_column(),score])
                     if  self.board[i - 1].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                             self.board[i - 1].get_column(),score])
                     if self.board[i + 15].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                             self.board[i + 15].get_column(),score])
                     if  self.board[i - 17].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 17].get_row(),
                             self.board[i  - 17].get_column(),score])
                     if self.board[i].get_row()< 15 and self.board[i + 17].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                             self.board[i + 17].get_column(),score])
                     if self.board[i - 15].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 15].get_row(),
                             self.board[i - 15].get_column(),score])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "k" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i +16].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),
                         self.board[i + 16].get_column(),score])
                if self.board[i - 16].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                         self.board[i - 16].get_column(),score])
                if self.board[i + 1].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                         self.board[i + 1].get_column(),score])
                if self.board[i - 1].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                         self.board[i - 1].get_column(),score])
                if self.board[i + 15].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                         self.board[i + 15].get_column(),score])
                if self.board[i - 17].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 17].get_row(),
                         self.board[i - 17].get_column(),score])
                if self.board[i + 17].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                         self.board[i + 17].get_column(),score])
                if self.board[i - 15].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 15].get_row(),
                         self.board[i - 15].get_column(),score])
        return movesAtack

class RookBlack(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "r" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i + 16].get_name() == " ":
                    spaceUp = MovesBoard().moveLine("up",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceUp[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceUp[0].get_row(),spaceUp[0].get_column(),score])
                if self.board[i - 16].get_name() == " ":
                    spaceDown = MovesBoard().moveLine("down",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceDown[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceDown[0].get_row(),spaceDown[0].get_column(),score])
                if self.board[i + 1].get_name() == " " :
                    spaceRight = MovesBoard().moveLine("right",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRight[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRight[0].get_row(),spaceRight[0].get_column(),score])
                if self.board[i - 1].get_name() == " ":
                    spaceLeft = MovesBoard().moveLine("left",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceLeft[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceLeft[0].get_row(),spaceLeft[0].get_column(),score])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "r" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i+16].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i +16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i +16].get_row(),
                         self.board[i +16].get_column(),score])
                elif self.board[i+16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("up",self.board,self.board[i+16],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 16].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),self.board[i - 16].get_column(),score])
                elif self.board[i - 16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("down",self.board,self.board[i - 16],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i + 1].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                         self.board[i + 1].get_column(),score])
                elif self.board[i+ 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("right",self.board,self.board[i + 1],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 1].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                         self.board[i - 1].get_column(),score])
                elif self.board[i - 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("right",self.board,self.board[i - 1],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
        return movesAtack


class BishopBlack(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "b" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i + 17].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("rd",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                         spaceRD[0].get_column(),score])
                if self.board[i + 15].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("ldd",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                         spaceRD[0].get_column(),score])
                if self.board[i - 17].get_name() == " ":
                    spaceDR = MovesBoard().moveDiagonal("dl",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceDR[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceDR[0].get_row(),
                         spaceDR[0].get_column(),score])
                if self.board[i - 15].get_name() == " " :
                    spaceRD = MovesBoard().moveDiagonal("dr",self.board,self.board[i])
                    score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                         spaceRD[0].get_column(),score])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "b" and 0<self.board[i].get_row()<15 and 0<self.board[i].get_column()<15:
                if self.board[i + 17].get_colour() == "white":
                        score=MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             self.board[i + 17].get_row(), self.board[i + 17].get_column(),score])
                elif self.board[i + 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("rd",self.board,self.board[i+17],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i + 15].get_colour() == "white":
                    score=MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 15].get_row(),self.board[i + 15].get_column(),score])
                elif self.board[i + 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("ldd",self.board,self.board[i + 15],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 17].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 17].get_row(),self.board[i - 17].get_column(),score])
                elif self.board[i - 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dl",self.board,self.board[i - 17],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if self.board[i - 15].get_colour() == "white":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 15].get_row(),self.board[i - 15].get_column(),score])
                elif self.board[i - 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dr",self.board,self.board[i - 15],"white")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),space[0].get_column(),score])
        return movesAtack