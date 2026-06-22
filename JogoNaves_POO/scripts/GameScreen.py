from scripts.Screen import Screen
from scripts.Player import Player
from scripts.Enemy import Enemy
import pygame as pg


class GameScreen(Screen):

    ENEMY_EVENT = pg.USEREVENT + 1
    RELOAD_EVENT = pg.USEREVENT + 2
    BOSS_ATTACK_EVENT = pg.USEREVENT + 3
    RESET_HITBOX_EVENT = pg.USEREVENT + 4

    def __init__(self, game):

        super().__init__(game)

        #Events Timer
        pg.time.set_timer(self.ENEMY_EVENT, 200)
        pg.time.set_timer(self.RELOAD_EVENT, 500)
        pg.time.set_timer(self.BOSS_ATTACK_EVENT, 4000)
        pg.time.set_timer(self.RESET_HITBOX_EVENT, 2500)

        self.enemies = pg.sprite.Group()
        self.player = Player()

    def update(self):
        
        self.player.update()

        self.enemies.update()

    
    def handle_events(self, event):
        if event.type == self.ENEMY_EVENT:
            enemy = Enemy()
            self.enemies.add(enemy)
        

    def draw(self, screen):

        screen.fill((50, 100, 100))
        self.player.draw(screen)

        self.enemies.draw(screen)