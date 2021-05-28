import enum
import logging
import platform

MACHINE = platform.node()
MODULE = 'my_module'
COMPANY = 'Company Name'


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    filename='logs/.log',
    filemode='a',
    level=logging.INFO,
)


class LOGGING_ENUM(enum.Enum):
    INFO = logging.info
    ERROR = logging.error
    WARNING = logging.warning


def registry(logging_enum, message):
    """Registry

    Args:
        logging_enum (LOGGING_ENUM)
        message (str)

    Returns:
        timestamp status container module message
    """
    return logging_enum(f'|| {MACHINE} || {MODULE} || {COMPANY} || {message}')
