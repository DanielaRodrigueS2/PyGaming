import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../assets/imgs/NaveVerde.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center(400, 600)
        self.speed = 5
        self.lifes = 3
        self.can_shot = True

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and self.x < (800 - 64):
            self.x += self.speed
        if key[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.speed
        if key[pygame.K_DOWN] and self.y < (800 - 64):
            self.y += self.speed
        if key[pygame.K_UP] and self.y >= 800 // 3:
            self.y -= self.speed
        if key[pygame.K_SPACE] and self.can_shot:
            # create_shot()
            can_shot = False

    def drawn(self, screen):
        screen.blit(self.image, self.rect)