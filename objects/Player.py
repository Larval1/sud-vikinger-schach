import pygame as pg
class Player(pg.sprite.Sprite):
    def __init__(self, name, team):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.team = team
        print(self.name)
        print(self.team)
