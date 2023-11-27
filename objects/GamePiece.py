import pygame as pg
import os


class GamePiece(pg.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image("game_piece.xcf")
        self.pos = pg.Vector2(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        print('Im a Wiking')
        print(pos_x)
        print(pos_y)

    def set_pos(self, pos_x, pos_y):
        self.pos = pg.Vector2(pos_x, pos_y)

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
