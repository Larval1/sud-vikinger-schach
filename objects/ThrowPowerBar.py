import os

import pygame as pg


class ThrowPowerBar:
    def __init__(self):
        self.throw_power = 0
        self.screen = pg.display.get_surface()
        self.moving = False
        self.direction = 'down'

    def get_throw_power(self):
        return self.throw_power

    def is_moving(self):
        return self.moving

    def start_moving(self):
        self.moving = True

    def stop_moving(self):
        self.moving = False

    def update(self):
        self.move_powerbar()
        pg.draw.line(
            self.screen,
            "pink",
            pg.Vector2((self.screen.get_width() / 100) * 99, self.screen.get_height()),
            pg.Vector2((self.screen.get_width() / 100) * 99,
                       self.screen.get_height() - (self.screen.get_height() / self.screen.get_height()) *self.throw_power),
            5
        )

    def move_powerbar(self):
        if self.moving:
            if self.direction == 'down':
                if (self.throw_power < self.screen.get_height()):
                    self.throw_power += 10
                else:
                    self.direction = 'up'
            elif self.direction == 'up':
                if self.throw_power >= 0:
                    self.throw_power -= 10
                else:
                    self.direction = 'down'
    def load_image(self, name, color_key=None, scale=1):
        data_dir = os.path.join(os.path.abspath(""), "assets")

        fullname = os.path.join(data_dir, name)
        image = pg.image.load(fullname)

        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pg.transform.scale(image, size)

        image = image.convert()
        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pg.RLEACCEL)
        return image, image.get_rect()
