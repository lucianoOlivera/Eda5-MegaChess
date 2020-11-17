from __future__ import annotations
from abc import ABC, abstractmethod


class StrategyChess(ABC):
    @abstractmethod
    def strategyClassLogic(self):
        pass


class BlackStrategy(StrategyChess):
    def strategyClassLogic(self):
        return


class WhiteStrategy(StrategyChess):
    def strategyClassLogic(self):
        return


class Context():
    def __init__(self, strategy: StrategyChess):
        self._strategy = strategy

    @property
    def strategy(self) -> StrategyChess:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StrategyChess):
        self._strategy = strategy

    def strategyLogic(self):
        print("Context: muestra los movimiento ,todabia nose como)")

