import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def printFile(unix_fname):
    if os.name == 'nt':
        fname = unix_fname.replace('/', '\\')
    else:
        fname = unix_fname
    with open(fname, 'r') as f:
        for line in f.readlines():
            print(line, end='')

def printLine(line):
    import time
    import sys
    from data import CPS

    for c in line:
        print(c, end='')
        sys.stdout.flush()
        # if c != ' ':
        time.sleep(1 / CPS)
