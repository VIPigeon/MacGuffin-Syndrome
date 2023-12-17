
from MonologMG import MonologMG
import os
import screen
import time


class FrameAnimation(MonologMG):
    def __init__(self, player, fps, path):
        super().__init__(player)
        self.frame = 0
        self.fps = fps
        self.file = {self.frame}
        self.path = path
        self._is_end = False

    def getFname(self):
        if os.name == 'nt':
            return self.path.replace("/", "\\") + '\\' + f'{self.frame}.txt'
        return f'{self.path}/{self.frame}.txt'

    def update(self):
        screen.clear()
        self._printPlayer()
        screen.printFile(self.getFname())
        self.frame += 1
        if not os.path.exists(self.getFname()):
            self.frame -= 1
            self._is_end = True
        time.sleep(1 / self.fps)

    def is_end(self):
        return self._is_end


if __name__ == '__main__':
    from Player import Player
    mg = FrameAnimation(Player(), 1, 'Animations/MorningClock')
    while not mg.is_end():
        mg.update()
