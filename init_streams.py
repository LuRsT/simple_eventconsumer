import yaml
import uuid
import requests


def emit_empty_event(stream, host, port):
    url = 'http://{host}:{port}/streams/{stream}'.format(
        host=host,
        stream=stream,
        port=port,
    )
    headers = {
        "Content-Type": "application/json",
        "ES-EventType": "init",
        "ES-EventId": str(uuid.uuid4()),
    }
    requests.post(url, data="{}", headers=headers)


def initialise_streams():
    with open('config.yml') as conf:
        config = yaml.load(conf)
        host = config['atomicpuppy']['host']
        port = config['atomicpuppy']['port']
        for stream in config['atomicpuppy']['streams']:
            emit_empty_event(stream, host, port)


if __name__ == "__main__":
    initialise_streams()
