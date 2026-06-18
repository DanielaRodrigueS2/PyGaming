import pygame as pg

class Screen:
    def __init__ (self, game, width, height):
        self.game = game
        self.widht = width
        self.height = height
        
    def update(self):
        pass
    
    def handle_events(self, event):
        pass

    def drawn (self, surface):
        pass
    