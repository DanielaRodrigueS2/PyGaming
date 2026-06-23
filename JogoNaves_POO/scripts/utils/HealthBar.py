import pygame as pg

class HealthBar(pg.sprite.Sprite):
     
    def __init__(self, x_position, y_position, life):
        pg.sprite.Sprite.__init__(self)
        self.life = life
        self.image = pg.Surface((self.life, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, 0)
        self.x = x_position

    def update(self, life):
        self.life = life
        self.image = pg.Surface((self.life, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)