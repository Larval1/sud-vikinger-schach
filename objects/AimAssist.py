import os

import pygame as pg


class AimAssist:
    def __init__(self, ):
        self.up_down_moving = False
        self.side_side_moving = False
        self.screen = pg.display.get_surface()
        self.angel=0
        self.throwPower = self.screen.get_width()/4
        self.height_direction = False
        self.width_direction = False
        self.start_side = True
        self.vector = pg.Vector2()

    def reset(self):
        self.throwPower =self.screen.get_width()/4

        self.angel=0
        self.up_down_moving = False
        self.side_side_moving = False
    def get_angel(self):
        return  self.angel

    def get_throwPower(self):
        return self.throwPower
    def get_vector(self):
        return self.vector

    def is_up_down_moving(self):
        return self.up_down_moving

    def start_up_down_moving(self):
        self.up_down_moving = True

    def stop_up_down_moving(self):
        self.up_down_moving = False

    def is_side_side_moving(self):
        return self.side_side_moving

    def start_side_side_moving(self):
        self.side_side_moving = True

    def stop_side_side_moving(self):
        self.side_side_moving = False

    def update(self, game_state):
        if game_state == 'aim_assist':
            self.move_angel()
        if game_state == 'trow_power':
            self.move_throwPower()

        self.vector.from_polar((self.get_throwPower(), self.get_angel()))

    def move_angel(self):
        if self.up_down_moving:
            if not self.height_direction:
                if self.angel <70:
                    self.angel += 2
                else:
                    self.height_direction = True
            elif self.height_direction:
                if self.angel >-70:
                    self.angel -= 2
                else:
                    self.height_direction = False

    def move_throwPower(self):
        if self.side_side_moving:
            if not self.width_direction:
                if self.throwPower < self.screen.get_width():
                    self.throwPower += 10
                else:
                    self.width_direction = True
            elif self.width_direction:
                if self.throwPower >= 0:
                    self.throwPower -= 10
                else:
                    self.width_direction = False
