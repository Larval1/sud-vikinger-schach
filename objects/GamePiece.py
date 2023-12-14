import pygame as pg

import objects.Game as game


class GamePiece(pg.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = game.load_image("game_piece.png")
        self.OriginalImage = self.image
        self.screen = pg.display.get_surface()
        self.area = self.screen.get_rect()
        self.rect.topleft = pos_x - self.rect.width / 2, pos_y - self.rect.height / 2
        self.rethrown = False
        self.rethrowActiveGamePiece = False

    def update(self, aimAssistVector, game_state, game):
        if self.check_collision(aimAssistVector) and game_state == 'hit':
            self.image = pg.transform.grayscale(self.image)
            self.hit_management(game)
        if self.rethrowActiveGamePiece and game_state == 'rethrow_hit':
            self.rethrowActiveGamePiece = False
            self.image = self.OriginalImage
            self.rect.center = aimAssistVector
            if game.activePlayer == 'left':
                if self.rect.x < self.screen.get_width() / 2:
                    self.kill()
            else:
                if self.rect.x > self.screen.get_width() / 2:
                    self.kill()
        return

    def hit_management(self, game):
        game.game_state = 'rethrow'
        game.aim_assist.reset()
        if not self.rethrown:
            self.rethrown = True
            self.rethrowActiveGamePiece = True
        else:
            game.game_state = 'reset'
            self.kill()

    def check_collision(self, aimAssistVector):

        if (aimAssistVector.distance_to(self.rect.center) <= 60):
            return True
        else:
            return False
