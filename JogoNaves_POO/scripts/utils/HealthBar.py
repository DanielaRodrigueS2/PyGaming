import pygame as pg

class HealthBar(pg.sprite.Sprite):
     
    def __init__(self, x_position, y_position, life):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((life, 20))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position + 10)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)