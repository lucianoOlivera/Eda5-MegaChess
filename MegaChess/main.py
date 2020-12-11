import asyncio
import websockets
import json
from const import TOKEN,WS
from factoryServerEvent import FactoryServerEvent


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
    uri = WS.format(token)
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                print(data)
                if data['event'] == 'update_user_list':
                    FactoryServerEvent().get_event('update_user_list',data)
                if data['event'] == 'gameover':
                    FactoryServerEvent().get_event('gameover',data)
                if data['event'] == 'ask_challenge':
                    messageEvent = FactoryServerEvent().get_event('ask_challenge',data)
                    await send(websocket,messageEvent['action'],{'board_id': messageEvent['board_id']},)
                if data['event'] == 'your_turn':
                    messageEvent = FactoryServerEvent().get_event('your_turn',data)
                    await send(websocket,'move',
                               {'board_id': messageEvent['board_id'],'turn_token': messageEvent['turn_token'],
                                'from_row': messageEvent['from_row'],'from_col': messageEvent['from_col'],
                                'to_row': messageEvent['to_row'],'to_col': messageEvent['to_col']})
            except Exception as e:
                print('Error in messageEvent :',e)


asyncio.get_event_loop().run_until_complete(start(TOKEN))
