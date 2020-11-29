from abc import ABC, abstractmethod
from board import Board

"""<<Interface>>StrategyChess"""
class StrategyChess(ABC):
    @abstractmethod
    def strategyClassLogic (self, board: Board) -> object:
        pass

""" logic of the strategy of the white pieces"""

class BlackStrategy(StrategyChess):
    def strategyClassLogic (self, board: Board):
        for i in range(0, len(board)):
            if board[i].get_row() == '0':
                print(board[i].get_row())

    def Quen(self,board):
        for i in range(0, len(board)):
            print()
    def Pawn(self,board):
        for i in range(0, len(board)):
            if board[i].get_name() == 'p':
                print(board[i].get_name())

"""logic of the strategy of the black pieces """


class WhiteStrategy(StrategyChess):
    def strategyClassLogic(self, board: Board):
        self.Pawn(board)

    def Quen(self,board):
        for i in range(0, len(board)):
            print()
    def Pawn(self,board):
        for i in range(0, len(board)):
            if board[i].get_name() == 'p':
                print(board[i].get_name())




"""Context """


class Context():
    def __init__ (self, strategy: StrategyChess):
        self._strategy = strategy

    @property
    def strategy (self) -> StrategyChess:
        return self._strategy

    @strategy.setter
    def strategy (self, strategy: StrategyChess):
        self._strategy = strategy

    def strategyLogic (self, board: Board):
        resultado = self._strategy.strategyClassLogic(board)


