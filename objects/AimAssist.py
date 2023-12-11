import pygame as pg


class AimAssist:
    def __init__(self, ):
        self.up_down_moving = False
        self.side_side_moving = False
        self.screen = pg.display.get_surface()
        self.angel = 0
        self.throwPower = self.screen.get_width() / 4
        self.height_direction = False
        self.width_direction = False
        self.start_side = True

    def reset(self):
        self.throwPower = self.screen.get_width() / 4
        self.angel = 0
        self.up_down_moving = False
        self.side_side_moving = False

    def get_vector(self):
        vector = pg.Vector2()
        vector.from_polar((self.throwPower, self.angel))
        return vector

    def start_up_down_moving(self):
        self.up_down_moving = True

    def stop_up_down_moving(self):
        self.up_down_moving = False

    def start_side_side_moving(self):
        self.side_side_moving = True

    def stop_side_side_moving(self):
        self.side_side_moving = False

    def update(self, target_point):
        if self.up_down_moving:
            self.move_angel()
        if self.side_side_moving:
            self.move_throwPower(target_point)

    def move_angel(self):
        if not self.height_direction:
            if self.angel < 70:
                self.angel += 2
            else:
                self.height_direction = True
        elif self.height_direction:
            if self.angel > -70:
                self.angel -= 2
            else:
                self.height_direction = False

    def move_throwPower(self, target_point):
        if target_point.x > self.screen.get_height() or target_point.x < 0:
            self.width_direction = not self.width_direction

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
