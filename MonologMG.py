
from MiniGame import MiniGame


class MonologMG(MiniGame):

    def __init__(self, player):
        super().__init__(player)
        self._is_end = False

    def is_end(self):
        return self._is_end

    def update(self):
        assert False

    def _printLine(self, line):
        import time
        import sys
        from data import CPS

        for c in line:
            print(c, end='')
            sys.stdout.flush()
            # if c != ' ':
            time.sleep(1 / CPS)

    def _printFile(self, unix_fname):
        import os
        if os.system == 'nt':
            fname = unix_fname.replace('/', '\\')
        else:
            fname = unix_fname
        with open(fname, 'r') as f:
            for line in f.readlines():
                self._printLine(line)

    def _printPlayer(self):
        self._printLine(f'Здоровье: {self.player.health}\n')
        self._printLine(f'Рассудок: {self.player.mind}\n')


if __name__ == '__main__':
    pass
