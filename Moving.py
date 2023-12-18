
import os

from MiniGame import MiniGame
from data import *
import interactives


class Moving(MiniGame):

    def __init__(self, player, fname):
        super().__init__(player)
        self._is_end = False
        self._map = []
        self.text = [[''] * MAP_FRAME_SIZE_X for _ in range(MAP_FRAME_SIZE_Y)]  # текст поверх карты
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
            print(MAP_INDENT, end='')
            for j in range(startX, startX + frameX):
                if self.player.y == i and self.player.x == j:
                    print('@', end='')
                elif self.text[i][j]:
                    print(self.text[i][j])
                else:
                    print(self._map[i][j], end='')
            print()
            # if i == self.player.y:
            #     line = self._map[i][:]
            #     line[self.player.x] = '@'
            #     print(MAP_INDENT, *line[startX:startX + frameX], sep='')
            # else:
            #     print(MAP_INDENT, *self._map[i][startX:startX + frameX], sep='')


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
        tile = self._map[y][x]
        if tile in '[]#':
            return False
        if tile in '_-|':
            # interactives.
            return False
        return True



if __name__ == "__main__":
    from Player import Player

    fname = 'rogueMap1.txt'
    player = Player()
    mmg = Moving(player, fname)
    os.system('cls' if os.name == 'nt' else 'clear')
    mmg.print()
    while True:
        mmg.update()
        os.system('cls' if os.name == 'nt' else 'clear')
        mmg.print()
