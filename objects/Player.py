import pygame as pg
from objects.AimAssist import AimAssist
class Player(pg.sprite.Sprite):
    def __init__(self, name, team, color, pos):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.team = team
        self.color = color
        self.pos = pos

    def start_aiming(self):
        return

    def stop_aiming(self):
        return
