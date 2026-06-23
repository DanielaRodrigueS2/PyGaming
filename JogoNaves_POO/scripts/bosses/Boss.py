import pygame as pg
import os
from scripts.utils.HealthBar import HealthBar

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
        self.life = 800

        self.life_bar = HealthBar(self.rect.centerx, self.rect.centery, self.life)

    def update(self):
        self.life_bar.update(self.life)
        print(self.life)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.life_bar.draw(screen)