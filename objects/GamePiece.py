import pygame as pg
import logging


class GamePiece(pg.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)
        self.color = "red"
        self.pos = pg.Vector2(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_pos(self, pos_x, pos_y):
        self.pos = pg.Vector2(pos_x, pos_y)
