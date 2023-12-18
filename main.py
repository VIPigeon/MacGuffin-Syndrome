
from Player import Player
from FrameAnimation import FrameAnimation
from StartOfTheGame import StartOfTheGame


player = Player()
FrameAnimation(player, "Animations/MorningClock").play()
StartOfTheGame(player).play()
