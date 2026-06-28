from scripts.screens.Screen import Screen
from scripts.screens.GameScreen import GameScreen
from scripts.utils.MusicPlayer import MusicPlayer
import pygame as pg

class MenuScreen(Screen):

    def __init__(self, game):
        super().__init__(game)
        self.music = MusicPlayer("menu_music")
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        self.music.play()

    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.music.stop()
                self.game.change_current_screen(
                    GameScreen(self.game)
                )

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((0,0,0))

        # Initial Text
        text_iniciar = self.font.render('PRESSIONE ENTER PARA INICIAR', True, (255,255,255))
        text_center = text_iniciar.get_rect(center=(400,350))
        surface.blit(text_iniciar, text_center)

        # Game Name
        game_name = pg.font.SysFont('Comic Sans MS', 60).render('WEWE SPACE', True, (255,255,20))
        game_name_center = game_name.get_rect(center=(400, 100))
        surface.blit(game_name, game_name_center)

        # Credits
        dev_name = pg.font.SysFont('Comic Sans MS', 20).render('Made by: DanielaRodrigueS2', True, (0,255,20))
        dev_name_center = dev_name.get_rect(center = (400, 700))
        surface.blit(dev_name, dev_name_center)



