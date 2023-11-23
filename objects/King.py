from objects.GamePiece import GamePiece


class King(GamePiece):
    def __init__(self, pos_x, pos_y):
        GamePiece.__init__(self, pos_x, pos_y)
        print('but wait im also the king')
