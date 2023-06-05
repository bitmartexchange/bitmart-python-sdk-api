import asyncio
import json
import zlib

import websockets

from bitmart.lib import cloud_utils


def create_channel(channel, symbol):
    """
    Create channel
    :param channel: futures/kline1min
    :param symbol: BTCUSDT
    :return:
    """
    return f"{channel}:{symbol}"


def create_contract_login_params(api_key, memo, secret_key):
    """
    :rtype: object {"action":"access","args":["<API_KEY>", "<timestamp>", "<sign>", "web"]}
    """
    timestamp = cloud_utils.get_timestamp()
    sign = cloud_utils.sign(cloud_utils.pre_substring(timestamp, memo, 'bitmart.WebSocket'), secret_key)
    return json.dumps({"action": "access", "args": [api_key, timestamp, sign, "web"]})


def create_contract_subscribe_params(channels):
    return json.dumps({
        'action': 'subscribe',
        'args': channels
    })


async def contract_subscribe_without_login(read, uri, is_debug, time_out, param):
    """
    Send subscribe message and receive message
    :param read:  Receive message, callback function
    :param uri: Request domain, eg. "ws://127.0.0.1:8080"
    :param is_debug: False | Ture
    :param time_out: Connection time out (second)
    :param param: Public channels. eg. {"action": "subscribe", "args": ["futures/kline1min:BTCUSDT"]}
    :return:
    """
    print(f'[websockets] Connecting to {uri}')
    try:
        async with websockets.connect(uri, ping_interval=10, ping_timeout=10) as websocket:
            print(f'[websockets] Connected {uri}')
            if is_debug:
                print(f"[websockets] Send:{param}")
            await websocket.send(param)
            await wait_for_recv(websocket, read, is_debug, time_out)
    except (OSError, asyncio.TimeoutError) as e:
        print(e)
    except (websockets.ConnectionClosed, websockets.InvalidHandshake):
        print(f'[websockets] Reconnecting to {uri}')
        await contract_subscribe_without_login(read, uri, is_debug, time_out, param)


async def contract_subscribe_with_login(read, uri, api_key, memo, secret_key, is_debug, time_out, param,
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
    :param param: Private channels. eg. {"action": "subscribe", "args": ["futures/kline1min:BTCUSDT"]}
    :param reconnect: When Server close, the client reconnection.
    :return:
    """
    print(f'[websockets] Connecting to {uri}')
    try:
        async with websockets.connect(uri, ping_interval=10, ping_timeout=10) as websocket:
            print(f'[websockets] Connected {uri}')
            login_params = create_contract_login_params(api_key, memo, secret_key)
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
    except (websockets.ConnectionClosed, websockets.InvalidHandshake):
        print('[websockets] ConnectionClosed')
        if reconnect:
            print(f'[websockets] Reconnecting to {uri}')
            await contract_subscribe_with_login(read, uri, api_key, memo, secret_key, is_debug, time_out, param, True)


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
        except websockets.ConnectionClosed as e:
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
