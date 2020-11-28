from abc import ABC

from game import Game

messageEvent = {}


class ServerEvent(object):
    def run(self):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError


class UpdateUserList(ServerEvent):
    def __init__(self,response):
        self.response = response

    def run(self):
        return print(f"< {self.response}")


class GameOver(ServerEvent):
    def __init__(self,response):
        self.response = response

    def run(self):
        return print(f"< {self.response}")


class AskChallenge(ServerEvent):
    def __init__(self,response):
        self.response = response

    def run(self):
        board_id = self.response['data']['board_id']
        messageEvent['action'] = 'accept_challenge'
        messageEvent['board_id'] = board_id
        return messageEvent


class YourTurn(ServerEvent):
    def __init__(self,response):
        self.response = response

    def run(self):
        messageEvent['action'] = 'move'
        messageEvent['data']['board_id'] = self.response['data']['board_id']
        messageEvent['data']['turn_token'] = self.response['data']['turn_token']
        boardTurn = self.response['data']['board']
        colorTurn = self.response['data']['actual_turn']
        moveleft = self.response['data']['move_left']
        turntoken = self.response['data']['turn_token']
        game = Game(boardTurn,turntoken,moveleft)
        game.defineStrategy(colorTurn)

        return messageEvent
