import asyncio
import signal
import yaml

import atomicpuppy

from handlers import build_handlers


def main():
    full_config = 'config.yml'
    with open(full_config) as conf:
        global_config = yaml.load(conf)
        loop = asyncio.get_event_loop()
        handlers = build_handlers()
        ap = atomicpuppy.AtomicPuppy(global_config, handlers, loop)

    loop.add_signal_handler(signal.SIGINT, ap.stop)
    loop.run_until_complete(ap.start())


if __name__ == '__main__':
    main()
