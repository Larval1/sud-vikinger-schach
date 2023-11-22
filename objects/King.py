from objects.GamePiece import GamePiece


class King(GamePiece):
    def __init__(self,wiking_nummber):
        super().__init__(wiking_nummber)
        print('but wait im also the king')
