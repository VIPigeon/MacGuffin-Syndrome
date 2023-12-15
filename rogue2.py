
import os
import sys
from getch import getch


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def update(self, key):
        if key == 'w':
            self.y -= 1
        elif key == 's':
            self.y += 1
        elif key == 'a':
            self.x -= 1
        elif key == 'd':
            self.x += 1


class Map:
    def __init__(self, player, fname):
        self.map = []
        self.player = player
        with open(fname, 'r') as f:
            for line in f.readlines():
                self.map.append(list(line))
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print()


    def print(self):
        for i in range(len(self.map)):
            if i == self.player.y:
                line = self.map[i][:]
                line[self.player.x] = '@'
                print(*line[:-1], sep='')
            else:
                print(*self.map[i][:-1], sep='')


def update(key):
    global gplayer, gmap
    # if key.name == 'esc':
        # print("esc", 1 / 0)
        # sys.exit(0)
    gplayer.update(key)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(key.name)
    gmap.print()



gplayer = Player(1, 2)
gmap = Map(gplayer, 'rogueMap1.txt')
# getch()
while True:
    gplayer.update(getch())
    os.system('cls' if os.name == 'nt' else 'clear')
    gmap.print()
