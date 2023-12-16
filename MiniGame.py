
class MiniGame:
    def __init__(self, player):
        self.player = player

    def is_end(self):
        assert False

    def update(self):
        assert False

    def clearScreen(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    mg = MiniGame()
