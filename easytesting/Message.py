__author__ = 'Ulltor'


class Message(object):
    def __init__(self, message_type, text):
        self.type = message_type
        self.text = text

    def __str__(self):
        return "{0}: {1}".format(self.type, self.text)
