import pygame as pg
class Player(pg.sprite.Sprite):
    def __init__(self, name, team):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.team = team
        print(f'name {self.name}')
        print(f'team {self.team}')
