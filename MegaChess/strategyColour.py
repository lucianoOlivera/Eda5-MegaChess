from abc import ABC,abstractmethod
from board import Board
import numpy as np

"""<<Interface>>StrategyChess"""


class StrategyChess(ABC):
    @abstractmethod
    def strategyClassLogic(self,board: Board) -> object:
        pass

"""Context """


class Context():
    def __init__(self,strategy: StrategyChess):
        self._strategy = strategy

    @property
    def strategy(self) -> StrategyChess:
        return self._strategy

    @strategy.setter
    def strategy(self,strategy: StrategyChess):
        self._strategy = strategy

    def strategyLogic(self,board: Board):
        resultado = self._strategy.strategyClassLogic(board)
