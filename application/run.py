import uuid
import time

import log


def hello_log():
    while True:
        log.registry(log.LOGGING_ENUM.INFO, f'Info {uuid.uuid4()}')
        log.registry(log.LOGGING_ENUM.WARNING, f'Warning {uuid.uuid4()}')
        log.registry(log.LOGGING_ENUM.ERROR, f'Error {uuid.uuid4()}')
        time.sleep(5)


if __name__ == '__main__':
    # TODO: treating if not has directory logs
    hello_log()
