from time import clock

from easytesting import TestError, MessageType, Message


__author__ = 'Ulltor'


class TestWrapper(object):
    __messages = []

    def __init__(self, name=None):
        self.name = name

        self.start_time = None
        self.end_time = None

        self.exc_type = None
        self.exc_val = None
        self.exc_tb = None

    def message(self, message_type=MessageType.info, text=None):
        self.__messages.append(Message(message_type, text))

    def debug(self, text):
        self.message(MessageType.debug, text)

    def info(self, text):
        self.message(MessageType.info, text)

    def warning(self, text):
        self.message(MessageType.warning, text)

    def error(self, text):
        self.message(MessageType.error, text)

    def check(self, condition, text=None, message_type=MessageType.error, abort_test=False):
        if not condition:
            self.message(message_type, text)

            if abort_test:
                raise TestError()

    def __enter__(self):
        self.start_time = clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = clock()

        # exit if no exceptions
        if not exc_val:
            return False

        # let KeyboardInterrupt pass through
        if exc_type == KeyboardInterrupt:
            return False

        # suppress TestError which is used to abort a test
        if exc_type == TestError:
            return True

        # log any other error and suppress it to let other tests run
        self.error("Unhandled {0} exception: '{1}'.".format(exc_type, exc_val))
        self.exc_type = exc_type
        self.exc_val = exc_val
        self.exc_tb = exc_tb
        return True