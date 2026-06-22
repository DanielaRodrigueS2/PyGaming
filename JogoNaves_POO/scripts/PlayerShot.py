import pygame as pg

class PlayerShot(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((8, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x + 28, y - 48)
        self.speed = -5

    def update(self):
        self.rect.y += self.speed

        if self.rect.y <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)