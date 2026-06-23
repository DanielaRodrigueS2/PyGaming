import pygame as pg
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

sprite_path = os.path.join(
    BASE_DIR,
    'assets',
    'imgs',
    'Boss1.png'
)

class Boss(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 138)
        self.life = 2000

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)