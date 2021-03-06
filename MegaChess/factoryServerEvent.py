from serverEvent import (
    AskChallenge,
    GameOver,
    UpdateUserList,
    YourTurn
    )

class FactoryServerEvent(object):
    @classmethod
    def get_event(self,event,response):
        if event is 'update_user_list':
            return UpdateUserList(response).run()
        elif event is 'gameover':
            return GameOver(response).run()
        elif event is 'ask_challenge':
            return AskChallenge(response).run()
        elif event is 'your_turn':
            return YourTurn(response).run()
