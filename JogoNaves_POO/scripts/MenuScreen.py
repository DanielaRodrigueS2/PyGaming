from Screen import Screen
import pygame as pg

class MenuScreen(Screen):
    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.game.change_screen("game")

    def draw(self, surface):
        surface.fill((40,40,40))




