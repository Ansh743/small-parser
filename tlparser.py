#author - Anshul Maske (2830914)

import sys
from LogParser import LogParser
from flask import Flask, render_template


def main():
    file_name = sys.argv[1:]
    lp = LogParser()
    lp.setFile(file_name[0])
    lp.parse()
    print(lp.time)


if __name__ == '__main__':
    main()