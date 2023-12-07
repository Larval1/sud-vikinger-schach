import pygame as pg
import objects.Game as Game
import os


class GamePiece(pg.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = Game.load_image("game_piece.png")
        self.screen = pg.display.get_surface()
        self.area = self.screen.get_rect()
        self.rect.topleft = pos_x - self.rect.width / 2, pos_y - self.rect.height / 2

    def update(self, aimAssistVector, game_state):
        # self.rect.topleft = pos_x - self.rect.width/2, pos_y - self.rect.height/2
        # if game_state == 'hit':
        if self.check_kolision(aimAssistVector) and game_state == 'hit':
            self.image = pg.transform.grayscale(self.image, self.image)
        return

    def check_kolision(self, aimAssistVector):

        if (aimAssistVector.distance_to(self.rect.center) <= 50):
            print(aimAssistVector.distance_to(self.rect.center))
            return True
        else:
            return False
