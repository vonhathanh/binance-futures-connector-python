#!/usr/bin/env python
import json
import logging
from binance.lib.utils import config_logging
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    message = json.loads(message)
    print(message)


my_client = UMFuturesWebsocketClient(on_message=message_handler)

my_client.agg_mark_price(
    id=13,
    speed=1,
)
