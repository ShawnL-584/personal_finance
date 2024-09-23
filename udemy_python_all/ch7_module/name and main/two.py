import one

print('We are running codes in two.py now.')


def get_name():
    print(__name__)


if __name__ == '__main__':
    print('We are running two.py directly.')
    get_name()
    one.get_name()
