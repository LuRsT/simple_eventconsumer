import logging


class HelloHandler:

    def handle(msg):
        print('HI')


def build_handlers():
    handlers = {
        'hello': {
            'hello': HelloHandler().handle,
        },
    }

    def handle(msg):
        if msg.stream not in handlers:
            logging.warning('Unhandled stream ' + msg.stream)
            return False

        stream_handler = handlers[msg.stream]
        if msg.type not in stream_handler:
            logging.debug('Unhandled message type ' + msg.type)
            return False
        handler = handlers[msg.stream][msg.type]
        return handler(msg)

    return handle
