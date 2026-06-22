from scripts.Screen import Screen
from scripts.GameScreen import GameScreen
import pygame as pg

class MenuScreen(Screen):

    def __init__(self, game):
        super().__init__(game)

        self.font = pg.font.SysFont('Comic Sans MS', 40)

    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.game.change_current_screen(
                    GameScreen(self.game)
                )

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((40,40,40))

        text = self.font.render('PRESSIONE ENTER PARA INICIAR', True, (255,255,255))

        surface.blit(text, (70, 180))




