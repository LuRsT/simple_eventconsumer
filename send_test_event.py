import json
import sys
import uuid

import requests


def main(name):
    headers = {
        'Content-Type': 'application/json',
        'ES-EventType': 'hello',
        'ES-EventId': str(uuid.uuid4()),
    }
    requests.post(
        'http://localhost:2113/streams/hello',
        headers=headers,
        data=json.dumps({'name': name})
    )


if __name__ == '__main__':
    main(sys.argv[1])
