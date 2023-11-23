import logging

import pygame as pg
import logging
class Player(pg.sprite.Sprite):
    def __init__(self, name, team):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.team = team
        logging.debug(f'Player with Name {self.name} in Team {self.team}')
