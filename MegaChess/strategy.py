from abc import ABC, abstractmethod


"""<<Interface>>StrategyChess"""


class StrategyChess(ABC):
    @abstractmethod
    def strategyClassLogic (self, board: list) -> object:
        pass


"""( “from_row:” “from_col”:, “to_row”: “to_col”: )ser números entre 0 y 15.son los valores de movimiento de la 
piezas """

""" logic of the strategy of the white pieces"""

class BlackStrategy(StrategyChess):
    def strategyClassLogic (self, board: list):
      return print("black")


"""logic of the strategy of the black pieces """


class WhiteStrategy(StrategyChess):
    def strategyClassLogic (self, board: list):
        return print("while")
            #f' row :{board}'


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

    def strategyLogic (self, board: list):
        resultado = self._strategy.strategyClassLogic(board)


