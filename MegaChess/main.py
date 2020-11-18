import asyncio
import json
import websockets
import json


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
            }
        )
    print(message)
    await websocket.send(message)


async def start (token):
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(token)
    async with websockets.connect(uri) as websocket:
        messageEvent = {}
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                if data['event'] == 'update_user_list':
                    print(f"< {response}")
                if data['event'] == 'gameover':
                    print(f"< {response}")
                if data['event'] == 'ask_challenge':
                    print(f"< {response}")
                    board_id = data['data']['board_id']
                    messageEvent['action'] = 'accept_challenge'
                    messageEvent['board_id'] = board_id
                    print(f'message{messageEvent}')
                    await send(websocket, messageEvent['action'], {'board_id': messageEvent['board_id'], }, )
                if data['event'] == 'your_turn':
                    print(f"< {response}")
                    messageEvent['action'] = 'move'
                    messageEvent['data'] = data['data']['board_id']
                    messageEvent['data'] = data['data']['turn_token']
                    boardTurn = data['data']['board']
                    colorTurn = data['data']['actual_turn']
                    #crear un game con boardTurn colorTurn



                    await send(
                        websocket,
                        'move',
                        {
                            'board_id': data['data']['board_id'],
                            'turn_token': data['data']['turn_token'],
                            'from_row': "",
                            'from_col': "",
                            'to_row': "",
                            'to_col': "",
                            },
                        )

            except Exception as e:
                print('retry')


asyncio.get_event_loop().run_until_complete(start('59c8d9f1-d9ad-4994-8207-959ed182bf5b'))
