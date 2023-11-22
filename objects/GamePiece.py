import pygame

class GamePiece(pygame.sprite.Sprite):

    def __init__(self, wiking_nummber):
        pygame.sprite.Sprite.__init__(self)
        self.wiking_nummber=wiking_nummber
        print(f'Im a Wiking {self.wiking_nummber}')



