import asyncio
import logging


@asyncio.coroutine
def handle_hello(msg):
    name = msg.data['name']
    logging.warning(f'Hi {name}')


def build_handlers():
    handlers = {
        'hello': {
            'hello': handle_hello,
        },
    }

    @asyncio.coroutine
    def handle(msg):
        if msg.stream not in handlers:
            logging.warning(f'Unhandled stream {msg.stream}')
            return False

        stream_handler = handlers[msg.stream]
        if msg.type not in stream_handler:
            logging.debug(f'Unhandled message type {msg.type}')
            return False

        handler = handlers[msg.stream][msg.type]
        yield from handler(msg)

    return handle
