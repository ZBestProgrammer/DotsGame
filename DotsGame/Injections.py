from DotsGame.PlayerSwitcher import *
from DotsGame.CicleFinder import CicleFinder
from DotsGame.GameField import GameField

gameField = GameField()
cicleFinderA = CicleFinder()
cicleFinderB = CicleFinder()

uiInput = Input()
inputs = [uiInput, uiInput]
plA = Player(uiInput, gameField, cicleFinderA, "blue")
plB = Player(uiInput, gameField, cicleFinderB, "red")
players = [plA, plB]
playerSwitcher = PlayerSwitcher(players)
