import pygame
import random

pygame.init()
pygame.font.init()

# colors creation
cores = [
    (255, 255, 255),
    (255, 0, 255),
    (255, 0, 0),
    (0, 255, 255),
    (0,0,0)
]


# screen size
screen_length = 800
screen_height = 800

# Enemy create
enemy_speed = 3
enemy_size = 30
enemys = []

screen = pygame.display.set_mode((screen_length,screen_height))

# boss atributtes
boss_x = (screen_length // 2 ) - 400
boss_y = 0
boss = pygame.Rect(boss_x, boss_y, 800, 256)
boss_sprite = pygame.image.load('./imgs/Boss1.png').convert()
boss_life = 500

# player atributtes
posicao_x = 400
posicao_y = 600
player = pygame.Rect(posicao_x, posicao_y, 64,64)
sprite = pygame.image.load('./imgs/NaveVerde.png').convert()
lifes = 3
score = 0

# Font declaration
font = pygame.font.SysFont('Comic Sans MS', 32)

running = True
clock = pygame.time.Clock()

# Shots array and variable
shots = []
can_shot = True

# player moviment and actions
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

# create shot function
def create_shot():
    x = player.x + 28
    y = player.y - 48
    shot = pygame.Rect(x, y, 8, 40)
    shots.append(shot)

# manage shots function 
def manage_shots():
    global score, running, boss_life
    
    for shot in shots:
        pygame.draw.rect(screen, cores[2], shot)
        shot.y -= 5
        if shot.y == 0:
            shots.remove(shot)
        
        for enemy in enemys:
            if shot.colliderect(enemy):
                shots.remove(shot)
                enemys.remove(enemy)
                score += 1
                print(score)

        if shot.colliderect(boss):
            boss_life -= 25
            shots.remove(shot)

    if lifes <= 0:
        running = False
        
# create enemy function
def create_enemy():
    x = random.randrange(0 , screen_length - enemy_size)
    y = random.randrange(200 , (screen_height // 2) - enemy_size)
    enemy = pygame.Rect(x, y, enemy_size, enemy_size)
    enemys.append(enemy)

# generate enemy function
def generate_enemy():
    global lifes 
    for enemy in enemys:
        pygame.draw.rect(screen, cores[1], enemy)
        y = random.randrange(1,5)
        enemy.y += y
        if enemy.y == posicao_y or enemy.y == screen_height:
            enemys.remove(enemy)
        elif player.contains(enemy):
            enemys.remove(enemy)
            lifes -= 1

    

# Personalizade events
ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_EVENT, 500)

RELOAD_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(RELOAD_EVENT, 500)

while running:

    screen.fill(cores[4])
    
    # Font declaration
    player_lifes = font.render(f'Lifes: {lifes}', False, cores[0])
    player_score = font.render(f'Score: {score}', False, cores[0])

    # Drawing font
    screen.blit(player_lifes, (50, screen_height - 50))
    screen.blit(player_score, (screen_length - 200, screen_height - 50))

    # draing boss
    pygame.draw.rect(screen, cores[0], boss)
    screen.blit(boss_sprite, boss)

    # Drawing player
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

    # Functions relatable to controlling Rects
    player_moviment(key)
    generate_enemy()
    manage_shots()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()