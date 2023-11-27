import os

import pygame as pg
from pygame import Surface


class AimAssist(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image("Aimassist.png",(255,255,255,255), 4)
        self.rect.topleft = 10, 90
        self.moving = False
        self.screen = pg.display.get_surface()
        self.target = 0
        self.direction = 'down'

    def get_target(self):
        return self.target
    def is_moving(self):
        return self.moving

    def start_moving(self):
        self.moving = True

    def stop_moving(self):
        self.moving = False

    def update(self):
        self.move_taget()

        pg.draw.line(
            self.screen,
            "green",
            pg.Vector2(0, self.screen.get_height() / 2),
            pg.Vector2(self.screen.get_width() / 2, self.screen.get_height() / self.screen.get_height() * self.target),
            5
        )
    def move_taget(self):
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
