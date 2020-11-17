import asyncio
import json
import websockets
import json


async def send (websocket, action, data):
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
        while True:
            try:
                response = await websocket.recv()
                print(f"< {response}")
                data = json.loads(response)
                if data['event'] == 'update_user_list':
                    pass
                if data['event'] == 'gameover':
                    pass
                if data['event'] == 'ask_challenge':
                    await send(websocket, 'accept_challenge',
                               {
                                   'board_id': data['data']['board_id'],
                                   },
                               )
                if data['event'] == 'your_turn':
                    board = data['data']['board']
                    color = data['data']['actual_turn']
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
