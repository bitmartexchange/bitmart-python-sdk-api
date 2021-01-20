import asyncio
import json
import zlib

import websockets

from bitmart import cloud_utils


def create_channel(channel, symbol):
    """
    Create channel
    :param channel: spot/ticker
    :param symbol: ETH_BTC
    :return:
    """
    return f"{channel}:{symbol}"


def create_spot_login_params(api_key, memo, secret_key):
    """
    :rtype: object {"op":"login","args":["<API_KEY>", "<timestamp>", "<sign>"]}
    """
    timestamp = cloud_utils.get_timestamp()
    sign = cloud_utils.sign(cloud_utils.pre_substring(timestamp, memo, 'bitmart.WebSocket'), secret_key)
    return json.dumps({"op": "login", "args": [api_key, timestamp, sign]})


def create_spot_subscribe_params(channels):
    return json.dumps({
        'op': 'subscribe',
        'args': channels
    })


async def spot_subscribe_without_login(read, uri, is_debug, time_out, param):
    """
    Send subscribe message and receive message
    :param read:  Receive message, callback function
    :param uri: Request domain, eg. "ws://127.0.0.1:8080"
    :param is_debug: False | Ture
    :param time_out: Connection time out (second)
    :param param: Public channels. eg. {"op": "subscribe", "args": ["spot/user/ticker:ETH_BTC"]}
    :return:
    """
    print(f'[websockets] Connecting to {uri}')
    try:
        async with websockets.client.connect(uri, ping_interval=10, ping_timeout=10) as websocket:
            print(f'[websockets] Connected {uri}')
            if is_debug:
                print(f"[websockets] Send:{param}")
            await websocket.send(param)
            await wait_for_recv(websocket, read, is_debug, time_out)
    except (OSError, asyncio.TimeoutError) as e:
        print(e)
    except (websockets.exceptions.ConnectionClosed, websockets.exceptions.InvalidHandshake):
        print(f'[websockets] Reconnecting to {uri}')
        await spot_subscribe_without_login(read, uri, is_debug, time_out, param)


async def spot_subscribe_with_login(read, uri, api_key, memo, secret_key, is_debug, time_out, param,
                                    reconnect: bool = False):
    """
    First login, then send subscribe message and receive message
    :param read: Receive message, callback function
    :param uri: Request domain, eg. "ws://127.0.0.1:8080"
    :param api_key: Your api key
    :param memo: Your api key's memo
    :param secret_key: Your api key's secret
    :param is_debug: False | Ture
    :param time_out: The next invocation of recv() will return it. (second)
    :param param: Private channels. eg. {"op": "subscribe", "args": ["spot/user/order:ETH_BTC"]}
    :param reconnect: When Server close, the client reconnection.
    :return:
    """
    print(f'[websockets] Connecting to {uri}')
    try:
        async with websockets.client.connect(uri, ping_interval=10, ping_timeout=10) as websocket:
            print(f'[websockets] Connected {uri}')
            login_params = create_spot_login_params(api_key, memo, secret_key)
            if is_debug:
                print(f'[websockets] Send:{login_params}')
            await websocket.send(login_params)
            message = await websocket.recv()
            if is_debug:
                print(f'[websockets] Recv:{message}')
            read(message)

            if 'errorCode' not in message:
                reconnect = True

            if is_debug:
                print(f'[websockets] Send:{param}')
            await websocket.send(param)
            await wait_for_recv(websocket, read, is_debug, time_out)
    except (OSError, asyncio.TimeoutError) as e:
        print(e)
    except (websockets.exceptions.ConnectionClosed, websockets.exceptions.InvalidHandshake):
        print('[websockets] ConnectionClosed')
        if reconnect:
            print(f'[websockets] Reconnecting to {uri}')
            await spot_subscribe_with_login(read, uri, api_key, memo, secret_key, is_debug, time_out, param, True)


async def wait_for_recv(websocket, read, is_debug, time_out):
    while True:
        try:
            message = await asyncio.wait_for(websocket.recv(), timeout=time_out)
            message = convert(message)
            if is_debug:
                print(f'[websockets] Recv:{message}')
            read(message)
        except asyncio.TimeoutError:
            continue
        except websockets.exceptions.ConnectionClosed as e:
            print('[websockets] ConnectionClosed')
            raise e


def convert(message):
    if type(message) == bytes:
        return inflate(message)
    else:
        return message


def inflate(data):
    decompress = zlib.decompressobj(
            -zlib.MAX_WBITS
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated.decode('UTF-8')
