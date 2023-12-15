
from data import *


class Player:
    def __init__(self):
        """
        Все поля публичны
        """
        self.face = PLAYER_START_FACE
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.health = PLAYER_START_HEALTH
        self.mind = PLAYER_START_MIND


if __name__ == '__main__':
    player = Player()
