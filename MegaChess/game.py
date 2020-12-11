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
        """ Define la estrategia que se va a utilizar en este turno dependiendo del color del asignado

            Devuelve de la estrategia el from_row,from_col,to_row,to_col del movimiento
        """
        boardGame = Board(board)
        boardStrategy = boardGame.boardGame()
        result = ""
        if self.turn_token == "white":
            result = Context(WhiteStrategy()).strategyLogic(boardStrategy)
        elif self.turn_token == "black":
            result = Context(BlackStrategy()).strategyLogic(boardStrategy)
        return result

