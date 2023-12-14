import objects.Game as Game
from objects.GamePiece import GamePiece


class King(GamePiece):
    def __init__(self, pos_x, pos_y):
        GamePiece.__init__(self, pos_x, pos_y)
        self.image, self.rect = Game.load_image("king.jpg")
        self.rect.topleft = pos_x - self.rect.width / 2, pos_y - self.rect.height / 2
    def hit_management(self,game):

            if len(game.game_pieces) == 1:
                print(game.activePlayer + " is the winner!!!")
            else :
                print(game.activePlayer + " is the looser!!!")
            game.game_state = 'game_over'
            self.kill()
