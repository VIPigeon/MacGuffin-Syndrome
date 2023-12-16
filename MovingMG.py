
import os

from MiniGame import MiniGame
from data import *


class MovingMG(MiniGame):

    def __init__(self, player, fname):
        super().__init__(player)
        self._is_end = False
        self._map = []
        with open(fname, 'r') as f:
            for line in f.readlines():
                line = line[:-1]  # убираем последний пробел
                if not line:
                    # пропускаем пустые строки для удобства при создании карты
                    continue
                # пропускаем пустые символы для удобства при создании карты
                self._map.append(list(line.replace(MAP_NULL_CHAR, '')))
                if '@' in self._map[-1]:
                    self.player.y = len(self._map) - 1
                    for i in range(len(self._map[-1])):
                        if self._map[-1][i] == '@':
                            self._map[-1][i] = '.'
                            self.player.x = i


    def is_end():
        return self._is_end


    def print(self):
        frameX = MAP_FRAME_SIZE_X
        frameY = MAP_FRAME_SIZE_Y
        startY = self.player.y // frameY * frameY
        startX = self.player.x // frameX * frameX
        for i in range(startY, startY + frameY):
            if i == self.player.y:
                line = self._map[i][:]
                line[self.player.x] = '@'
                print(*line[startX:startX + frameX], sep='')
            else:
                print(*self._map[i][startX:startX + frameX], sep='')


    def update(self):
        from getch import getch
        c = getch()
        dx, dy = 0, 0
        if c == 'w':
            dy = -1
        elif c == 'a':
            dx = -1
        elif c == 's':
            dy = 1
        elif c == 'd':
            dx = 1

        if self.check_move(dx, dy):
            self.player.x += dx
            self.player.y += dy


    def check_move(self, dx, dy):
        x = self.player.x + dx
        y = self.player.y + dy
        if self._map[y][x] in MAP_SOLIDS:
            return False
        if self._map[y][x] in MAP_INTERACTIVES:
            ...
            assert False
        return True



if __name__ == "__main__":
    from Player import Player

    fname = 'rogueMap1.txt'
    player = Player()
    mmg = MovingMG(player, fname)
    os.system('cls' if os.name == 'nt' else 'clear')
    mmg.print()
    while True:
        mmg.update()
        os.system('cls' if os.name == 'nt' else 'clear')
        mmg.print()
