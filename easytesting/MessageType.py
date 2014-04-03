from enum import Enum

__author__ = 'Ulltor'


class MessageType(Enum):
    debug = 1
    info = 2
    warning = 3
    error = 4

    def __str__(self):
        if self == MessageType.debug:
            return "Debug"
        elif self == MessageType.info:
            return "Info"
        elif self == MessageType.warning:
            return "Warning"
        elif self == MessageType.error:
            return "Error"
        else:
            raise ValueError("Unsupported MessageType value {0}.".format(self))