import os
import uuid
import time

import log


def hello_log():
    while True:
        log.registry(log.LOGGING_ENUM.INFO, f'Info {uuid.uuid4()}')
        log.registry(log.LOGGING_ENUM.WARNING, f'Warning {uuid.uuid4()}')
        log.registry(log.LOGGING_ENUM.ERROR, f'Error {uuid.uuid4()}')
        time.sleep(15)


if __name__ == '__main__':
    if not os.path.exists(os.path.join(os.getcwd(), 'logs', '.log')):
        os.mkdir(f'{os.getcwd()}/logs3')

    hello_log()
