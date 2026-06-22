import pygame as pg
import random as rd

class Enemy():

    def __init__(self, size):
        self.x = rd.randrange(0, 800 - size)
        self.y = rd.randrange(200, 400 - size)
        self.rect = pg.Rect(self.x, self.y, size, size)
        self.speed = rd.randrange(1,4)

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pg.draw.rect(screen, (255, 0, 255), self.rect)