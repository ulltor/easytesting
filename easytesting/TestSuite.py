from easytesting import TestWrapper

__author__ = 'Ulltor'


class TestSuite(object):
    __tests = []

    def __init__(self, name=None, version='1.0'):
        """
        Initializes a new instance of TestSuite with given name and version

        :param name: test suite name
        :type name: str

        :param version: test suite version
        :type version: str
        """
        self.name = name
        self.version = version

    def create_test(self, name=None):
        """
        Creates a new TestWrapper with a specified name

        :param name: human readable test name
        :type name: str

        :returns: a TestWrapper instance associated with current TestSuite
        :rtype: TestWrapper
        """
        t = TestWrapper(name)
        self.__tests.append(t)
        return t

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # let KeyboardInterrupt pass through
        if exc_type == KeyboardInterrupt:
            return False

        return True