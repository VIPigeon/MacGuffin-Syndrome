
class MiniGame:
    def __init__(self, player):
        self.player = player

    def is_end(self):
        assert False

    def update(self):
        assert False

    def play(self):
        while not self.is_end():
            self.update()


if __name__ == '__main__':
    mg = MiniGame()
