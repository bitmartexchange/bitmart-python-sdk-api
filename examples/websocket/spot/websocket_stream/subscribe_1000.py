import logging
import time
from collections import deque

from bitmart.api_spot import APISpot
from bitmart.lib.cloud_consts import SPOT_PUBLIC_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.spot_socket_client import SpotSocketClient

spot_socket_client_counter = 0


def message_handler(message):
    if isinstance(message, dict):

        if "errorCode" in message:
            # 1.Subscription failed: {'errorMessage': 'Invalid symbol param', 'errorCode': '92001'}
            logging.error(message)

        elif "event" in message:
            # 2.Subscription successful: {"event": "subscribe","topic": "spot/ticker:BTC_USDT"}
            # logging.debug(f"Subscription successful topic: {message['topic']}")
            pass

        elif "table" in message:
            # 3.After successful subscription, push data: {"table":"spot/ticker:BTC_USDT","data":[]}
            # logging.debug(f"Subscription successful, Server return data: {message['data']}")
            pass


def send_in_chunks(symbols, channel="spot/depth50", batch_size=115, chunk_size=20):
    global spot_socket_client_counter  # Reference the global counter
    queue = deque(symbols)
    logging.info("Start Subscribe Topic: %d", len(queue))
    while len(queue) > 0:
        # Take up to 115 symbols from the front of the queue
        batch = [queue.popleft() for _ in range(min(batch_size, len(queue)))]

        # Create a new WebClient for this batch
        my_client = SpotSocketClient(stream_url=SPOT_PUBLIC_WS_URL,
                                     on_message=message_handler)
        spot_socket_client_counter += 1
        message_counter = 0

        # Split the batch into chunks of `chunk_size` (20 in this case)
        for i in range(0, len(batch), chunk_size):
            chunk = batch[i:i + chunk_size]
            args = [f"{channel}:{symbol}" for symbol in chunk]
            my_client.send({"op": "subscribe", "args": args})
            message_counter += len(args)
            time.sleep(1)

        logging.info(f"Total SpotSocketClient {spot_socket_client_counter} Send: {message_counter}")


if __name__ == '__main__':
    config_logging(logging, logging.DEBUG, log_file='app/sdk.log')

    spotAPI = APISpot(timeout=(2, 10))
    response = spotAPI.get_symbols()

    # Initialize symbols and the queue
    # symbols = ["BTC_USDT", "ETH_USDT", "XRP_USDT", "LTC_USDT", "ADA_USDT", "BNB_USDT", "SOL_USDT", "DOGE_USDT",
    #            "DOT_USDT", "MATIC_USDT", "LINK_USDT", "SHIB_USDT", "AVAX_USDT", "TRX_USDT", "VET_USDT", "EOS_USDT",
    #            "XLM_USDT", "FIL_USDT", "ICP_USDT", "MKR_USDT"]
    send_in_chunks(response[0]['data']['symbols'])

    logging.info(f"Total SpotSocketClient instances created: {spot_socket_client_counter}")
