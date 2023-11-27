import pygame as pg
from pygame import Surface

class AimAssist(pg.sprite.Sprite):
    def __init__(self, screen: Surface):
        pg.sprite.Sprite.__init__(self)
        self.moving = False
        self.screen = screen
        self.target = 0

    def get_target(self):
        return self.target

    def start_moving(self):
        self.moving = True

    def stop_moving(self):
        self.moving = False

    def move_aim_assist(self, dt):
        if self.moving:
            self.target += 1 * dt