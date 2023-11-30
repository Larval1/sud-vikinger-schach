import os

import pygame as pg


class AimAssist:
    def __init__(self, ):
        self.up_down_moving = False
        self.side_side_moving = False
        self.screen = pg.display.get_surface()
        self.height = 0
        self.width = 0
        self.height_direction = False
        self.width_direction = False
        self.start_side = True

    def reset(self):
        self.start_side=not self.start_side
        if self.start_side:
            self.width = 0
        else:
            self.width =self.screen.get_width()

        self.height = 0
        self.up_down_moving = False
        self.side_side_moving = False


    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

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
            self.move_height()
        if game_state == 'trow_power':
            self.move_width()

        # print(pg.Vector2(0, self.screen.get_height() / 2))

        pg.draw.circle(
            self.screen,
            "green",
            # pg.Vector2(self.screen.get_width() / 2, self.screen.get_height() /2),
            pg.Vector2(self.screen.get_width() / self.screen.get_width() * self.width,
                       self.screen.get_height() / self.screen.get_height() * self.height
                       ),
            50
        )

    def move_height(self):
        if self.up_down_moving:
            if not self.height_direction:
                if self.height < self.screen.get_height():
                    self.height += 10
                else:
                    self.height_direction = True
            elif self.height_direction:
                if self.height >= 0:
                    self.height -= 10
                else:
                    self.height_direction = False

    def move_width(self):
        if self.side_side_moving:
            if not self.width_direction:
                if self.width < self.screen.get_width():
                    self.width += 10
                else:
                    self.width_direction = True
            elif self.width_direction:
                if self.width >= 0:
                    self.width -= 10
                else:
                    self.width_direction = False
