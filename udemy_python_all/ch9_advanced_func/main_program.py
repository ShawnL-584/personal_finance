import sys


def main():
    contents = sys.stdin.read()
    new_contents = contents.replace(sys.argv[0], sys.argv[1])
    sys.stdout.write(new_contents)


main()
