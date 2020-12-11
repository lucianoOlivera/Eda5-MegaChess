"""logic of the strategy of the black pieces """
from board import Board
from movesBoard import MovesBoard
from piecesStrategy import PiecesStrategy,MoveScore
from strategyColour import StrategyChess

from piecesStrategy import highScore


class WhiteStrategy(StrategyChess):
    def strategyClassLogic(self,board: Board):
        listMoves = [PawnWhite(board).moves(),QueenWhite(board).movesAtack(),QueenWhite(board).moves(),
                     PawnWhite(board).movesAtack(),KingWhite(board).moves(),
                     KingWhite(board).movesAtack(),RookWhite(board).moves(),RookWhite(board).movesAtack(),
                     BishopWhite(board).moves(),BishopWhite(board).movesAtack(),
                     KnightWhite(board).moves(),KnightWhite(board).movesAtack()
                     ]
        listHighScore = highScore(listMoves)
        from_row = listHighScore[0]
        from_col = listHighScore[1]
        to_row = listHighScore[2]
        to_col = listHighScore[3]
        return from_row,from_col,to_row,to_col

class PawnWhite(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "P" and 0<=self.board[i].get_column()<=15:
                if self.board[i - 16].get_name() == " " and (self.board[i].row == 2 or self.board[i].row == 3):
                    if self.board[i - 32].get_name() == " ":
                        score = MoveScore().moveScore(self.board[i],self.board[i - 32].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 32].get_row(),
                             self.board[i - 32].get_column(),score])
                if self.board[i - 16].get_name() == " " and self.board[i].row>3:
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                         self.board[i - 16].get_column(),score+5])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "P":
                if self.board[i - 17].get_colour() == "black" and 0<self.board[i].get_column()<=15:
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 17].get_row(),
                         self.board[i - 17].get_column(),score+1])
                if self.board[i - 15].get_colour() == "black" and 0<=self.board[i].get_column()<15:
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 15].get_row(),
                         self.board[i - 15].get_column(),score+1])
        return movesAtack


class QueenWhite(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "Q":
                if 0<=self.board[i].get_row()<15 and self.board[i + 16].get_name() == " ":
                    spaceUp = MovesBoard().moveLine("up",self.board,self.board[i])
                    if spaceUp:
                        score = MoveScore().moveScore(self.board[i],spaceUp[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceUp[0].get_row(),
                             spaceUp[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),
                             self.board[i + 16].get_column(),score-15])
                if 0<self.board[i].get_row()<=15 and self.board[i - 16].get_name() == " ":
                    spaceDown = MovesBoard().moveLine("down",self.board,self.board[i])
                    if spaceDown:
                        score = MoveScore().moveScore(self.board[i],spaceDown[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceDown[0].get_row(),
                             spaceDown[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                             self.board[i - 16].get_column(),score-15])
                if 0<=self.board[i].get_column()<15 and self.board[i + 1].get_name() == " ":
                    spaceRight = MovesBoard().moveLine("right",self.board,self.board[i])
                    if spaceRight:
                        score = MoveScore().moveScore(self.board[i],spaceRight[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRight[0].get_row(),
                             spaceRight[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                             self.board[i + 1].get_column(),score-15])
                if 0<self.board[i].get_column()<=15 and self.board[i - 1].get_name() == " ":
                    spaceLeft = MovesBoard().moveLine("left",self.board,self.board[i])
                    if spaceLeft:
                        score = MoveScore().moveScore(self.board[i],spaceLeft[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceLeft[0].get_row(),
                             spaceLeft[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                             self.board[i - 1].get_column(),score-15])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("rd",self.board,self.board[i])
                    if spaceRD:
                        score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                             spaceRD[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                             self.board[i + 17].get_column(),score-15])
                if 0<=self.board[i].get_row()<15 and 0<self.board[i].get_column()<15 and self.board[
                    i + 15].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("ldd",self.board,self.board[i])
                    if spaceRD:
                        score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                             spaceRD[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                             self.board[i + 15].get_column(),score-15])
                if 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_name() == " ":
                    spaceDR = MovesBoard().moveDiagonal("dl",self.board,self.board[i])
                    if spaceDR:
                        score = MoveScore().moveScore(self.board[i],spaceDR[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceDR[0].get_row(),
                             spaceDR[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 17].get_row(),
                             self.board[i - 17].get_column(),score-15])
                if 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("dr",self.board,self.board[i])
                    if spaceRD:
                        score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                             spaceRD[0].get_column(),score-15])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 15].get_row(),
                             self.board[i - 15].get_column(),score-15])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "Q":
                if 0<=self.board[i].get_row()<15 and self.board[i + 16].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 16].get_row(),
                         self.board[i + 16].get_column(),score])
                elif 0<=self.board[i].get_row()<15 and self.board[i + 16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("up",self.board,self.board[i + 16],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<self.board[i].get_row()<=15 and self.board[i - 16].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                         self.board[i - 16].get_column(),score])
                elif 0<self.board[i].get_row()<=15 and self.board[i - 16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("down",self.board,self.board[i - 16],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<=self.board[i].get_column()<15 and self.board[i + 1].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                         self.board[i + 1].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and self.board[i + 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("right",self.board,self.board[i + 1],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<self.board[i].get_column()<=15 and self.board[i - 1].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                         self.board[i - 1].get_column(),score])
                elif 0<self.board[i].get_column()<=15 and self.board[i - 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("left",self.board,self.board[i - 1],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 17].get_row(),self.board[i + 17].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("rd",self.board,self.board[i + 17],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 15].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 15].get_row(),self.board[i + 15].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("ldd",self.board,self.board[i + 15],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),
                             space[0].get_column(),score])
                if 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 17].get_row(),self.board[i - 17].get_column(),score])
                elif 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dl",self.board,self.board[i - 17],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 15].get_row(),self.board[i - 15].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dr",self.board,self.board[i - 15],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),
                             space[0].get_column(),score])
        return movesAtack


class KingWhite(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "K":
                if 0<=self.board[i].get_row()<15 and self.board[i + 16].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),
                         self.board[i + 16].get_column(),score-85])
                if 0<self.board[i].get_row()<=15 and self.board[i - 16].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                         self.board[i - 16].get_column(),score-85])
                if 0<=self.board[i].get_column()<15 and self.board[i + 1].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                         self.board[i + 1].get_column(),score-85])
                if 0<self.board[i].get_column()<=15 and self.board[i - 1].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                         self.board[i - 1].get_column(),score-85])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 15].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                         self.board[i + 15].get_column(),score-85])
                if 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 17].get_row(),
                         self.board[i - 17].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                         self.board[i + 17].get_column(),score-85])
                if 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 15].get_row(),
                         self.board[i - 15].get_column(),score-85])

        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "K":
                if 0<=self.board[i].get_row()<15 and self.board[i + 16].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),
                         self.board[i + 16].get_column(),score])
                if 0<self.board[i].get_row()<=15 and self.board[i - 16].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                         self.board[i - 16].get_column(),score])
                if 0<=self.board[i].get_column()<15 and self.board[i + 1].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                         self.board[i + 1].get_column(),score])
                if 0<self.board[i].get_column()<=15 and self.board[i - 1].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                         self.board[i - 1].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 15].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                         self.board[i + 15].get_column(),score])
                if 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 17].get_row(),
                         self.board[i - 17].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                         self.board[i + 17].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 15].get_row(),
                         self.board[i - 15].get_column(),score])
        return movesAtack


class RookWhite(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "R":
                if 0<=self.board[i].get_row()<15 and self.board[i + 16].get_name() == " ":
                    spaceUp = MovesBoard().moveLine("up",self.board,self.board[i])
                    if spaceUp:
                        score = MoveScore().moveScore(self.board[i],spaceUp[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceUp[0].get_row(),
                             spaceUp[0].get_column(),score-45])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 16].get_row(),
                             self.board[i + 16].get_column(),score-45])
                if 0<self.board[i].get_row()<=15 and self.board[i - 16].get_name() == " ":
                    spaceDown = MovesBoard().moveLine("down",self.board,self.board[i])
                    if spaceDown:
                        score = MoveScore().moveScore(self.board[i],spaceDown[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceDown[0].get_row(),
                             spaceDown[0].get_column(),score-45])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                             self.board[i - 16].get_column(),score-45])
                if 0<=self.board[i].get_column()<15 and self.board[i + 1].get_name() == " ":
                    spaceRight = MovesBoard().moveLine("right",self.board,self.board[i])
                    if spaceRight:
                        score = MoveScore().moveScore(self.board[i],spaceRight[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRight[0].get_row(),
                             spaceRight[0].get_column(),score-45])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                             self.board[i + 1].get_column(),score-45])
                if 0<self.board[i].get_column()<=15 and self.board[i - 1].get_name() == " ":
                    spaceLeft = MovesBoard().moveLine("left",self.board,self.board[i])
                    if spaceLeft:
                        score = MoveScore().moveScore(self.board[i],spaceLeft[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceLeft[0].get_row(),
                             spaceLeft[0].get_column(),score-45])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                             self.board[i - 1].get_column(),score-45])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "R":
                if 0<=self.board[i].get_row()<15 and self.board[i + 16].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 16].get_row(),
                         self.board[i + 16].get_column(),score])
                elif 0<=self.board[i].get_row()<15 and self.board[i + 16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("up",self.board,self.board[i + 16],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<self.board[i].get_row()<=15 and self.board[i - 16].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 16].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 16].get_row(),
                         self.board[i - 16].get_column(),score])
                elif 0<self.board[i].get_row()<=15 and self.board[i - 16].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("down",self.board,self.board[i - 16],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<=self.board[i].get_column()<15 and self.board[i + 1].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 1].get_row(),
                         self.board[i + 1].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and self.board[i + 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("right",self.board,self.board[i + 1],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<self.board[i].get_column()<=15 and self.board[i - 1].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 1].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 1].get_row(),
                         self.board[i - 1].get_column(),score])
                elif 0<self.board[i].get_column()<=15 and self.board[i - 1].get_name() == " ":
                    space = MovesBoard().moveLineEnemy("right",self.board,self.board[i - 1],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
        return movesAtack


class BishopWhite(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "B":
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("rd",self.board,self.board[i])
                    if spaceRD:
                        score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                             spaceRD[0].get_column(),score-25])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 17].get_row(),
                             self.board[i + 17].get_column(),score-25])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 15].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("ldd",self.board,self.board[i])
                    if spaceRD:
                        score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                             spaceRD[0].get_column(),score-25])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 15].get_row(),
                             self.board[i + 15].get_column(),score-25])
                if 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_name() == " ":
                    spaceDR = MovesBoard().moveDiagonal("dl",self.board,self.board[i])
                    if spaceDR:
                        score = MoveScore().moveScore(self.board[i],spaceDR[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceDR[0].get_row(),
                             spaceDR[0].get_column(),score-25])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 17].get_row(),
                             self.board[i - 17].get_column(),score-25])
                if 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_name() == " ":
                    spaceRD = MovesBoard().moveDiagonal("dr",self.board,self.board[i])
                    if spaceRD:
                        score = MoveScore().moveScore(self.board[i],spaceRD[0].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),spaceRD[0].get_row(),
                             spaceRD[0].get_column(),score-25])
                    else:
                        score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                        moves.append(
                            [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 15].get_row(),
                             self.board[i - 15].get_column(),score-25])
        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "B":
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 17].get_row(),self.board[i + 17].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("rd",self.board,self.board[i + 17],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 15].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i + 15].get_row(),self.board[i + 15].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("ldd",self.board,self.board[i + 15],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),
                             space[0].get_column(),score])
                if 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 17].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 17].get_row(),self.board[i - 17].get_column(),score])
                elif 0<self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 17].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dl",self.board,self.board[i - 17],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),
                             space[0].get_row(),space[0].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 15].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),
                         self.board[i - 15].get_row(),self.board[i - 15].get_column(),score])
                elif 0<=self.board[i].get_column()<15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 15].get_name() == " ":
                    space = MovesBoard().moveDiagonalEnemy("dr",self.board,self.board[i - 15],"black")
                    if space:
                        score = MoveScore().moveScore(self.board[i],space[0].get_name())
                        movesAtack.append(
                            [self.board[i].get_row(),self.board[i].get_column(),space[0].get_row(),
                             space[0].get_column(),score])
        return movesAtack


class KnightWhite(PiecesStrategy):
    def moves(self):
        moves = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "H":
                if 2<=self.board[i].get_column()<=15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 14].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 14].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 14].get_row(),
                         self.board[i + 14].get_column(),score-15])
                if 0<=self.board[i].get_column()<14 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 18].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 18].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 18].get_row(),
                         self.board[i + 18].get_column(),score-15])
                if 1<=self.board[i].get_column()<=15 and 0<=self.board[i].get_row()<14 and self.board[
                    i + 31].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 31].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 31].get_row(),
                         self.board[i + 31].get_column(),score-15])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<14 and self.board[
                    i + 33].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 33].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 33].get_row(),
                         self.board[i + 33].get_column(),score-15])
                if 0<=self.board[i].get_column()<14 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 14].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 14].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 14].get_row(),
                         self.board[i - 14].get_column(),score-15])
                if 2<=self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 18].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 18].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 18].get_row(),
                         self.board[i - 18].get_column(),score-15])
                if 0<=self.board[i].get_column()<15 and 1<self.board[i].get_row()<=15 and self.board[
                    i - 31].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 31].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 31].get_row(),
                         self.board[i - 31].get_column(),score-15])
                if 0<self.board[i].get_column()<=15 and 1<self.board[i].get_row()<=15 and self.board[
                    i - 33].get_name() == " ":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 33].get_name())
                    moves.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 33].get_row(),
                         self.board[i - 33].get_column(),score-15])

        return moves

    def movesAtack(self):
        movesAtack = []
        for i in range(0,len(self.board)):
            if self.board[i].get_name() == "H":
                if 2<=self.board[i].get_column()<=15 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 14].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 14].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 14].get_row(),
                         self.board[i + 14].get_column(),score])
                if 0<=self.board[i].get_column()<14 and 0<=self.board[i].get_row()<15 and self.board[
                    i + 18].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 18].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 18].get_row(),
                         self.board[i + 18].get_column(),score])
                if 1<=self.board[i].get_column()<=15 and 0<=self.board[i].get_row()<14 and self.board[
                    i + 31].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 31].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 31].get_row(),
                         self.board[i + 31].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 0<=self.board[i].get_row()<14 and self.board[
                    i + 33].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i + 33].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i + 33].get_row(),
                         self.board[i + 33].get_column(),score])
                if 0<=self.board[i].get_column()<14 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 14].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 14].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 14].get_row(),
                         self.board[i - 14].get_column(),score])
                if 2<=self.board[i].get_column()<=15 and 0<self.board[i].get_row()<=15 and self.board[
                    i - 18].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 18].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 18].get_row(),
                         self.board[i - 18].get_column(),score])
                if 0<=self.board[i].get_column()<15 and 1<self.board[i].get_row()<=15 and self.board[
                    i - 31].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 31].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 31].get_row(),
                         self.board[i - 31].get_column(),score])
                if 0<self.board[i].get_column()<=15 and 1<self.board[i].get_row()<=15 and self.board[
                    i - 33].get_colour() == "black":
                    score = MoveScore().moveScore(self.board[i],self.board[i - 33].get_name())
                    movesAtack.append(
                        [self.board[i].get_row(),self.board[i].get_column(),self.board[i - 33].get_row(),
                         self.board[i - 33].get_column(),score])
        return movesAtack
