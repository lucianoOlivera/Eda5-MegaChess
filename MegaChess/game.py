import numpy as np
from strategyColour import Context
from board import Board
from blackStrategy import BlackStrategy
from whiteStrategy import WhiteStrategy


class Game():
    def __init__(self,board_id,turn_token,move_left):
        self.board_id = board_id
        self.turn_token = turn_token
        self.move_left = move_left

    def defineStrategy(self,board):
        boardGame = Board(board)
        boardStrategy = boardGame.boardGame()
        result = ""
        if self.turn_token == "white":
            ctx = Context(WhiteStrategy())
            result = ctx.strategyLogic(boardStrategy)
        elif self.turn_token == "black":
            ctx = Context(BlackStrategy())
            result = ctx.strategyLogic(boardStrategy)
        return result


