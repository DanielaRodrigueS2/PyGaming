from scripts.screens.Screen import Screen
from scripts.player.Player import Player
from scripts.enemies.Enemy import Enemy
from scripts.enemies.Enemy2 import Enemy2
from scripts.bosses.Boss import Boss
from scripts.player.PlayerShot import PlayerShot
import pygame as pg


class GameScreen(Screen):

    ENEMY_EVENT = pg.USEREVENT + 1
    RELOAD_EVENT = pg.USEREVENT + 2
    BOSS_ATTACK_EVENT = pg.USEREVENT + 3
    RESET_HITBOX_EVENT = pg.USEREVENT + 4
    ENEMY_EVENT2 = pg.USEREVENT + 5

    def __init__(self, game):

        super().__init__(game)
        self.font = pg.font.SysFont('Comic Sans MS', 32)

        #Events Timer
        pg.time.set_timer(self.ENEMY_EVENT, 200)
        pg.time.set_timer(self.ENEMY_EVENT2, 10000)
        pg.time.set_timer(self.RELOAD_EVENT, 300)
        pg.time.set_timer(self.BOSS_ATTACK_EVENT, 4000)
        pg.time.set_timer(self.RESET_HITBOX_EVENT, 2500)

        self.enemies = pg.sprite.Group()
        self.enemies2 = pg.sprite.Group()
        self.shots = pg.sprite.Group()
        self.player = Player()
        self.boss = Boss()

    def update(self):
        
        self.player.update()
        self.boss.update()
        self.enemies.update()
        self.enemies2.update()
        self.shots.update()

        self.check_collisions()

    def handle_events(self, event):
        if event.type == self.ENEMY_EVENT:
            enemy = Enemy()
            self.enemies.add(enemy)

        if event.type == self.ENEMY_EVENT2:
            self.enemies.empty()
            for x in range(1,20):
                enemy = Enemy2(-100, 0, 200, 800, 2, 5)
                enemy2 = Enemy2(800, 900, 200, 800, -5, -2)
                self.enemies2.add(enemy)
                self.enemies2.add(enemy2)
                print(x)

        if event.type == self.RELOAD_EVENT:
            self.player.reload()
            self.player.manageShots(self.shots)
        

    def check_collisions(self):

        pg.sprite.groupcollide(self.shots, self.enemies, False, True)
        if pg.sprite.spritecollide(self.player, self.enemies, True):
            self.player.lifes -= 1

        if pg.sprite.spritecollide(self.boss, self.shots, True):
            self.boss.life -= 25
        

    def draw(self, screen):
 
        screen.fill((50, 100, 100))

        # Player/Enemies
        self.player.draw(screen)
        self.boss.draw(screen)
        self.shots.draw(screen)
        self.enemies.draw(screen)
        self.enemies2.draw(screen)

        #Text

        lifes = self.font.render(f'Lifes: {self.player.lifes}', True, (255,255,255))
        screen.blit(lifes, (50, 750))
