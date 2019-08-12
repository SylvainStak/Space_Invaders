from Game import Game
from config import INVADERS_SPEED, BULLET_SPEED, PLAYER_SPEED

g = Game(60, INVADERS_SPEED, BULLET_SPEED, PLAYER_SPEED)

g.StartGameLoop()
