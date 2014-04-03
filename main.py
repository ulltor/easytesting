from easytesting import TestSuite

__author__ = 'Ulltor'


def main():
    with TestSuite("Example test suite") as ts:
        with ts.create_test("Example test") as t:
            t.check(True)
            t.message('Sample message')
            t.check([])


if __name__ == "__main__":
    main()