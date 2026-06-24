import pygame as pg
import random as rd

class Enemy2(pg.sprite.Sprite):

    def __init__(self, x_random, x_random2, y_random, y_random2, speed):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((20,20))
        self.image.fill((25, 0, 25))
        self.x = rd.randrange(x_random, x_random2)
        self.y = rd.randrange(y_random, y_random2)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

        if self.rect.x >= 1000 or self.rect.x <= -200:
            self.kill

    def draw(self, screen):
        screen.blit(self.image, self.rect)