from scripts.Screen import Screen
from scripts.Player import Player
import pygame as pg

class GameScreen(Screen):
    def __init__(self, game):

        super().__init__(game)

        self.player = Player()

    def update(self):
        
        self.player.update()

    
    def handle_events(self, event):
        pass
        

    def draw(self, screen):
        screen.fill((50, 100, 100))
        self.player.draw(screen)