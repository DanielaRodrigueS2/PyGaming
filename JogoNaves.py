import pygame
import random

pygame.init()

cores = [
    (255, 255, 255),
    (255, 0, 255),
    (255, 0, 0),
    (0, 255, 255)
]

screen_length = 800
screen_height = 800

enemy_speed = 3
enemy_size = 30
enemys = []

posicao_x = 400
posicao_y = 600

screen = pygame.display.set_mode((screen_length,screen_height))

sprite = pygame.image.load('./imgs/NaveVerde.png').convert()

running = True
clock = pygame.time.Clock()


def player_moviment(key):

    global posicao_x, posicao_y

    if key[pygame.K_RIGHT] and posicao_x < (screen_length - 64):
        posicao_x += 5
    if key[pygame.K_LEFT] and posicao_x >= 0:
        posicao_x -= 5
    if key[pygame.K_DOWN] and posicao_y < (screen_length - 64):
        posicao_y += 5
    if key[pygame.K_UP] and posicao_y >= screen_height / 2:
        posicao_y -= 5   
    

def create_enemy():
    x = random.randrange(0 , screen_length - enemy_size)
    y = random.randrange(0 , (screen_length // 2) - enemy_size)
    enemy = pygame.Rect(x, y, enemy_size, enemy_size)
    enemys.append(enemy)

def generate_enemy():
    cor = random.randrange(1, 3)
    for enemy in enemys:
        pygame.draw.rect(screen, cor, enemy)
        y = random.randrange(1,5)
        enemy.y += y
        if enemy.y == posicao_y or enemy.y == screen_height:
            enemys.remove(enemy)
    

ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_EVENT, 1000)

while running:


    screen.fill(cores[0])
    screen.blit(sprite, (posicao_x, posicao_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == ENEMY_EVENT:
            create_enemy()

    key = pygame.key.get_pressed()

    player_moviment(key)
    generate_enemy()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()