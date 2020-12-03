import asyncio
import websockets
import json
from factoryEvent import FactoryEvent
from const import ws,token


async def send(websocket,action,data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
            }
        )
    print(message)
    await websocket.send(message)
async def start(token):
    uri = ws.format(token)
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                my_factory = FactoryEvent()
                print(data)
                if data['event'] == 'update_user_list':
                    my_factory.get_event('update_user_list',data)
                if data['event'] == 'gameover':
                    my_factory.get_event('gameover',data)
                if data['event'] == 'ask_challenge':
                    messageEvent = my_factory.get_event('ask_challenge',data)
                    print(messageEvent)
                    await send(websocket,messageEvent['action'],{'board_id': messageEvent['board_id']},)
                if data['event'] == 'your_turn':
                    messageEvent = my_factory.get_event('your_turn',data)
                    print(messageEvent)
                    await send(websocket, 'move', {'board_id': data['data']['board_id'],'turn_token': data['data']['turn_token'], 'from_row':messageEvent['data']['from_row'],'from_col':messageEvent['data']['from_col'],'to_row':messageEvent['data']['to_row'],'to_col':messageEvent['data']['to_col']}, )
            except Exception as e:
                print('retry')

asyncio.get_event_loop().run_until_complete(start(token))
