print('We are running codes in one.py')


def get_name():
    print(__name__)


if __name__ == '__main__':
    print('We are running one.py directly.')
    get_name()
else:
    print('one.py is imported.')
    get_name()
