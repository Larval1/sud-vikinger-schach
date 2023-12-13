import pygame as pg


class AimAssist:
    def __init__(self, ):
        self.up_down_moving = False
        self.side_side_moving = False
        self.screen = pg.display.get_surface()
        self.angel = 0
        self.throwPower = 0
        self.height_direction = False
        self.width_direction = False
        self.start_side = True
        self.countUp = True
        self.stopThrowPower = True

    def reset(self):
        self.throwPower = 0
        self.angel = 0
        self.up_down_moving = False
        self.side_side_moving = False
        self.countUp = True
        self.stopThrowPower = True

    def get_vector(self):
        return pg.Vector2.from_polar((200, self.angel))

    def get_target_vector(self):
        return pg.Vector2.from_polar(((self.screen.get_width() / 100) * self.throwPower, self.angel))

    def start_up_down_moving(self):
        self.up_down_moving = True

    def stop_up_down_moving(self):
        self.up_down_moving = False

    def update(self, target_point):
        if self.up_down_moving:
            self.move_angel()
        if not self.stopThrowPower:
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
        if self.countUp:
            if self.throwPower < 100:
                self.throwPower += 1
            elif self.throwPower == 100:
                self.countUp = False
        else:
            if self.throwPower > 0:
                self.throwPower -= 1
            elif self.throwPower == 0:
                self.countUp = True

        # if target_point.x > self.screen.get_height() or target_point.x < 0:
        # self.width_direction = not self.width_direction
        # if not self.width_direction:
        #   if self.throwPower < 100:
        #      self.throwPower += 1
        # else:
        #    self.width_direction = True
        # elif self.width_direction:
        #   if self.throwPower >= 0:
        #      self.throwPower -= 1
        # else:
        #    self.width_direction = False
