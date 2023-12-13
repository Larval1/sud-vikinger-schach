import os

import pygame as pg

from objects.AimAssist import AimAssist
from objects.GamePiece import GamePiece
from objects.King import King


def load_image(name, color_key=None, scale=1):
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


class Game:
    def __init__(self, screen):
        self.aim_assist = None
        self.game_pieces = list[GamePiece]
        self.game_state = 'aim_assist'
        self.activePlayer = 'left'
        self.playerPosition1 = pg.Vector2(0, screen.get_height() / 2)
        self.playerPosition2 = pg.Vector2(screen.get_width(), screen.get_height() / 2)
        self.activePlayerPosition = pg.Vector2()
        self.gameOverMessage = 'loses'

    def next_game_state(self):
        match self.game_state:
            case 'aim_assist':
                self.game_state = 'trow_power'
                self.aim_assist.start_side_side_moving()
            case 'trow_power':
                self.game_state = 'hit'
            case 'hit':
                self.game_state = 'reset'
            case 'rethrow_aim_assist':
                self.game_state = 'rethrow_trow_power'
            case 'rethrow_trow_power':
                self.game_state = 'rethrow_hit'
            case 'rethrow_hit':
                self.game_state = 'reset'
            case 'reset':
                self.aim_assist.reset()
                self.switch_player()
                self.game_state = 'aim_assist'

    def switch_player(self):
        if self.activePlayer == 'left':
            self.activePlayer = 'right'
            self.activePlayerPosition = self.playerPosition2
        else:
            self.activePlayer = 'left'
            self.activePlayerPosition = self.playerPosition1

    def setup_game(self, screen):
        self.aim_assist = AimAssist()
        self.activePlayerPosition = self.playerPosition1
        self.game_pieces = pg.sprite.RenderPlain(self.setup_game_pieces(screen.get_width(), screen.get_height()))

    def setup_game_pieces(self, width, height):
        game_pieces = []
        temp_height = 0
        for i in range(0, 2):
            temp_height += height / 6
            game_pieces.append(GamePiece(width / 2, temp_height))
        temp_height += height / 6
        game_pieces.append(King(width / 2, height / 2))
        for i in range(0, 2):
            temp_height += height / 6
            game_pieces.append(GamePiece(width / 2, temp_height))

        return game_pieces
