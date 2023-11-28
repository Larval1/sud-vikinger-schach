import os

import pygame as pg


class AimAssist:
    def __init__(self):
        self.moving = False
        self.screen = pg.display.get_surface()
        self.target = 0
        self.direction = 'down'
        self.y=pg.Vector2(0, self.screen.get_height() / 2)

    def get_target(self):
        return self.target
    def is_moving(self):
        return self.moving

    def start_moving(self):
        self.moving = True

    def stop_moving(self):
        self.moving = False

    def update(self):
        self.move_target()

        pg.draw.line(
            self.screen,
            "green",
            self.y,
            pg.Vector2(self.screen.get_width() / 2, self.screen.get_height() / self.screen.get_height() * self.target),
            5
        )
    def move_target(self):
        if self.moving:
            if self.direction == 'down':
                if (self.target < self.screen.get_height()):
                    self.target += 10
                else:
                    self.direction = 'up'
            elif self.direction == 'up':
                if self.target >= 0:
                    self.target -= 10
                else:
                    self.direction = 'down'

