from Screen import Screen
from Player import Player
import pygame as pg

class GameScreen(Screen):
    def __init__(self, game, sprites):
        super.__init__(game)

        self.player = Player()

    def update(self):
        self.player.update()
        

    def draw(self, screen):
        
        self.fill((50, 100, 100))
        self.player.draw(screen)