
from MonologMG import MonologMG
import screen


class StartOfTheGame(MonologMG):

    def __init__(self, player):
        super().__init__(player)
        screen.clear()
        self._printPlayer()
        screen.printFile('StartOfTheGame/init.txt')
        self._sleep_index = 0

    def update(self):
        from getch import getch
        c = getch()
        if c == '1':
            self._is_end = True
        elif c == '2' and self._sleep_index < 3:
            self._sleep_index += 1
            screen.clear()
            self._printPlayer()
            screen.printFile(f'StartOfTheGame/sleep{self._sleep_index}.txt')


if __name__ == '__main__':
    from Player import Player
    mg = StartOfTheGame(Player())
    while not mg.is_end():
        mg.update()
