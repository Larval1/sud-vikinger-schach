import objects.Game as Game
from objects.GamePiece import GamePiece


class King(GamePiece):
    def __init__(self, pos_x, pos_y):
        GamePiece.__init__(self, pos_x, pos_y)
        self.image, self.rect = Game.load_image("king.png")
        self.rect.topleft = pos_x - self.rect.width / 2, pos_y - self.rect.height / 2
