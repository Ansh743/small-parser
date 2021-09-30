#author - Anshul Maske (2830914)

import sys
from LogParser import LogParser


def main():
    file_name = sys.argv[1]

    lp = LogParser(file_name)
    lp.parse()
    print(lp.time)


if __name__ == '__main__':
    main()