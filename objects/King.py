import logging

from objects.GamePiece import GamePiece


class King(GamePiece):
    def __init__(self, pos_x, pos_y):
        GamePiece.__init__(self, pos_x, pos_y)
