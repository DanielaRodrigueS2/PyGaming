from scripts.screens.Screen import Screen
from scripts.Player import Player
from scripts.Enemy import Enemy
from scripts.Boss import Boss
from scripts.PlayerShot import PlayerShot
import pygame as pg


class GameScreen(Screen):

    ENEMY_EVENT = pg.USEREVENT + 1
    RELOAD_EVENT = pg.USEREVENT + 2
    BOSS_ATTACK_EVENT = pg.USEREVENT + 3
    RESET_HITBOX_EVENT = pg.USEREVENT + 4

    def __init__(self, game):

        super().__init__(game)
        self.font = pg.font.SysFont('Comic Sans MS', 32)

        #Events Timer
        pg.time.set_timer(self.ENEMY_EVENT, 200)
        pg.time.set_timer(self.RELOAD_EVENT, 300)
        pg.time.set_timer(self.BOSS_ATTACK_EVENT, 4000)
        pg.time.set_timer(self.RESET_HITBOX_EVENT, 2500)

        self.enemies = pg.sprite.Group()
        self.shots = pg.sprite.Group()
        self.player = Player()
        self.boss = Boss()

    def update(self):
        
        self.player.update()
        self.boss.update()
        self.enemies.update()
        self.shots.update()

        self.check_collisions()

    def handle_events(self, event):
        if event.type == self.ENEMY_EVENT:
            enemy = Enemy()
            self.enemies.add(enemy)

        if event.type == self.RELOAD_EVENT:
            self.player.reload()
            self.player.manageShots(self.shots)
        

    def check_collisions(self):

        pg.sprite.groupcollide(self.shots, self.enemies, False, True)
        if pg.sprite.spritecollide(self.player, self.enemies, True):
            self.player.lifes -= 1
        

    def draw(self, screen):
 
        screen.fill((50, 100, 100))

        # Player/Enemies
        self.player.draw(screen)
        self.boss.draw(screen)
        self.shots.draw(screen)
        self.enemies.draw(screen)

        #Text

        lifes = self.font.render(f'Lifes: {self.player.lifes}', True, (255,255,255))
        screen.blit(lifes, (50, 750))
