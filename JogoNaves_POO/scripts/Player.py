import pygame as pg
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sprite_path = os.path.join(
    BASE_DIR,
    'assets',
    'imgs',
    'NaveVerde.png'
)

print(sprite_path)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 600)
        self.speed = 5
        self.lifes = 3
        self.can_shot = True

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT] and self.rect.x < (800 - 64):
            self.rect.x += self.speed
        if key[pg.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if key[pg.K_DOWN] and self.rect.y < (800 - 64):
            self.rect.y += self.speed
        if key[pg.K_UP] and self.rect.y >= 800 // 3:
            self.rect.y -= self.speed
        if key[pg.K_SPACE] and self.can_shot:
            # create_shot()
            self.can_shot = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)