import pygame as pg
import random as rd

class Enemy(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((20,25))
        self.image.fill((255, 0, 255))
        self.x = rd.randrange(0, 800 - 10)
        self.y = rd.randrange(200, 400 - 10)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = rd.randrange(3,5)

    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= 800:
            self.kill

    def draw(self, screen):
        screen.blit(self.image, self.rect)