import pygame
import random

pygame.init()

cores = [
    (255, 255, 255),
    (255, 0, 255),
    (255, 0, 0),
    (0, 255, 255),
]

screen_length = 800
screen_height = 800

enemy_speed = 3
enemy_size = 30
enemys = []

posicao_x = 400
posicao_y = 600

screen = pygame.display.set_mode((screen_length,screen_height))

player = pygame.Rect(posicao_x, posicao_y, 64,64)
sprite = pygame.image.load('./imgs/NaveVerde.png').convert()

running = True
clock = pygame.time.Clock()

shots = []
can_shot = True

def player_moviment(key):

    global can_shot

    if key[pygame.K_RIGHT] and player.x < (screen_length - 64):
        player.x += 5
    if key[pygame.K_LEFT] and player.x >= 0:
        player.x -= 5
    if key[pygame.K_DOWN] and player.y < (screen_length - 64):
        player.y += 5
    if key[pygame.K_UP] and player.y >= screen_height / 2:
        player.y -= 5   
    if key[pygame.K_SPACE] and can_shot:
        create_shot()
        can_shot = False


def create_shot():
    x = player.x + 28
    y = player.y - 48
    shot = pygame.Rect(x, y, 8, 40)
    shots.append(shot)

def manage_shots():
    for shot in shots:
        pygame.draw.rect(screen, cores[2], shot)
        shot.y -= 5
        if shot.y == 0:
            shots.remove(shot)
        
        for enemy in enemys:
            if shot.colliderect(enemy):
                shots.remove(shot)
                enemys.remove(enemy)
        

def create_enemy():
    x = random.randrange(0 , screen_length - enemy_size)
    y = random.randrange(0 , (screen_length // 3) - enemy_size)
    enemy = pygame.Rect(x, y, enemy_size, enemy_size)
    enemys.append(enemy)

def generate_enemy():
    for enemy in enemys:
        pygame.draw.rect(screen, cores[1], enemy)
        y = random.randrange(1,5)
        enemy.y += y
        if enemy.y == posicao_y or enemy.y == screen_height:
            enemys.remove(enemy)
        elif player.contains(enemy):
            enemys.remove(enemy)
    

ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_EVENT, 1000)

RELOAD_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(RELOAD_EVENT, 500)


while running:

    screen.fill(cores[0])
    
    pygame.draw.rect(screen, cores[0], player)
    screen.blit(sprite, player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == ENEMY_EVENT:
            create_enemy()

        elif event.type == RELOAD_EVENT:
            can_shot = True

    key = pygame.key.get_pressed()

    player_moviment(key)
    generate_enemy()
    manage_shots()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()