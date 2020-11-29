"""logic of the strategy of the black pieces """
from board import Board
from strategyColour import StrategyChess


class WhiteStrategy(StrategyChess):
    def strategyClassLogic(self,board: Board):
        self.Pawn(board)

    def Quen(self,board):
        for i in range(0,len(board)):
            print()

    def Pawn(self,board):
        for i in range(0,len(board)):
            if board[i].get_name() == 'p':
                print(board[i].get_name())
