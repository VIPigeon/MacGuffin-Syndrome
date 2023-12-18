
from MiniGame import MiniGame


class Monolog(MiniGame):

    def __init__(self, player):
        super().__init__(player)
        self._is_end = False

    def is_end(self):
        return self._is_end

    def update(self):
        assert False

    def _printPlayer(self):
        print(f'Здоровье: {self.player.health}')
        print(f'Рассудок: {self.player.mind}')


if __name__ == '__main__':
    pass
