import pygame as pg
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

menu_music = os.path.join(
    BASE_DIR,
    'audio',
    'music',
    'Wewe_Space_Menu.mp3'
)

musics = {
    "menu_music" : menu_music
}

class MusicPlayer:

    def __init__(self, name):
        self.path = musics[name]

    def play(self):
        pg.mixer.music.load(self.path)
        pg.mixer.music.play(-1)

    def pause(self):
        pg.mixer.music.pause()

    def stop(self):
        pg.mixer.music.stop()