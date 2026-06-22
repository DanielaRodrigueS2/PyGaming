import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('../assets/imgs/NaveVerde.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center(400, 600)
        self.speed = 5
        self.lifes = 3
        self.can_shot = True

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT] and self.x < (800 - 64):
            self.x += self.speed
        if key[pg.K_LEFT] and self.x >= 0:
            self.x -= self.speed
        if key[pg.K_DOWN] and self.y < (800 - 64):
            self.y += self.speed
        if key[pg.K_UP] and self.y >= 800 // 3:
            self.y -= self.speed
        if key[pg.K_SPACE] and self.can_shot:
            # create_shot()
            can_shot = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)