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
        messageEvent['board_id'] = self.response['data']['board_id']
        messageEvent['turn_token'] = self.response['data']['turn_token']
        boardTurn = self.response['data']['board']
        colorTurn = self.response['data']['actual_turn']
        moveleft = self.response['data']['move_left']
        turntoken = self.response['data']['turn_token']
        game = Game(turntoken,colorTurn,moveleft)
        result = game.defineStrategy(boardTurn)
        print(result)
        messageEvent['from_row'] = result[0]
        messageEvent['from_col'] = result[1]
        messageEvent['to_row'] = result[2]
        messageEvent['to_col'] = result[3]
        return messageEvent

