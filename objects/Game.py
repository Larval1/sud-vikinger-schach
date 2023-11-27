import pygame as pg
from objects.King import King
from objects.GamePiece import GamePiece
from objects.ThrowPowerBar import ThrowPowerBar
from objects.AimAssist import AimAssist
from objects.Player import Player
import os


def start_game():
    # pygame setup
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    running = True
    dt = 0

    center_line_start = pg.Vector2(screen.get_width() / 2, 0)
    center_line_stop = pg.Vector2(screen.get_width() / 2, screen.get_height())

    playerPosition1 = pg.Vector2(0, screen.get_height() / 2)
    playerPosition2 = pg.Vector2(screen.get_width(), screen.get_height() / 2)

    power_bar_start = pg.Vector2((screen.get_width() / 100) * 99, screen.get_height())

    playerNumber = 2
    gamePieceNumber = 6

    game = Game()
    game.setup_game(screen)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('#80B2C9')

    pg.draw.line(screen, "black", center_line_start, center_line_stop, 5)

    # for i in range(0, len(game.game_pieces)):
    #    x = game.game_pieces[i]
    #    pg.draw.circle(screen, x.color, x.pos, 20)

    # for i in range(0, len(game.players)):
    #    x = game.players[i]
    #    pg.draw.circle(screen, x.color, x.pos, 20)

    allsprites = pg.sprite.RenderPlain(game.aim_assist)

    while running:
        screen.fill('#80B2C9')
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                match game.get_game_state():
                    case 'aim_assist':
                        if not game.aim_assist.is_moving():
                            game.aim_assist.start_moving()
                        else:
                            game.aim_assist.stop_moving()
                            game.next_game_state()
                    case 'trow_power':
                        if not game.throw_power_bar.is_moving():
                            game.throw_power_bar.start_moving()
                        else:
                            game.throw_power_bar.stop_moving()
                            game.next_game_state()

            match game.get_game_state():
               case 'hit':
                   print(game.aim_assist.get_target())
                   print(game.throw_power_bar.get_throw_power())
                   exit()
        allsprites.update()
        game.throw_power_bar.update()
        # fill the screen with a color to wipe away anything from last frame
        # allsprites.draw(screen)

        pg.draw.line(screen, "black", center_line_start, center_line_stop, 5)

        # flip() the display to put your work on screen
        pg.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pg.quit()
    return


class Game:
    def __init__(self):

        self.aim_assist = None
        self.throw_power_bar = None
        self.player_list = []
        self.game_pieces = []
        self.game_state = 'aim_assist'

    def next_game_state(self):
        match self.game_state:
            case 'aim_assist':
                self.game_state = 'trow_power'
                self.throw_power_bar.start_moving()
            case 'trow_power':
                self.game_state = 'hit'
            case 'hit':
                self.game_state = 'hit'



    def get_game_state(self):
        return self.game_state

    def setup_game(self, screen):
        self.throw_power_bar = ThrowPowerBar()
        self.aim_assist = AimAssist()

        self.create_players(2, screen.get_width(), screen.get_height())

        self.setup_game_pieces(screen.get_width(), screen.get_height())

    def setup_game_pieces(self, width, height):
        temp_height = 0
        for i in range(0, 2):
            temp_height += height / 6
            self.game_pieces.append(GamePiece(width / 2, temp_height))
        temp_height += height / 6
        self.game_pieces.append(King(width / 2, height / 2))
        for i in range(0, 2):
            temp_height += height / 6
            self.game_pieces.append(GamePiece(width / 2, temp_height))

    def create_players(self, number, width, height):
        for i in range(1, number + 1):
            pos_y = height / 2
            if i % 2 != 0:
                team = 1
                color = "blue"
                pos_x = 0
            else:
                team = 2
                color = "red"
                pos_x = width

            self.player_list.append(Player(i, team, color, pg.Vector2(pos_x, pos_y)))
