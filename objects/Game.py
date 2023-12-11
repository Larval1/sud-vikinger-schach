import pygame as pg
from objects.King import King
from objects.GamePiece import GamePiece
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

    game = Game(screen)
    game.setup_game(screen)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('#80B2C9')

    pg.draw.line(screen, "black", center_line_start, center_line_stop, 5)

    while running:
        screen.fill('#80B2C9')
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                match game.get_game_state():
                    case 'rethrow':
                        game.next_game_state()

                match game.get_game_state():
                    case 'aim_assist' | 'rethrow_aim_assist':
                        if not game.aim_assist.is_up_down_moving():
                            game.aim_assist.start_up_down_moving()
                        else:
                            game.aim_assist.stop_up_down_moving()
                            game.next_game_state()
                    case 'trow_power'| 'rethrow_trow_power':
                        if not game.aim_assist.is_side_side_moving():
                            game.aim_assist.start_side_side_moving()
                        else:
                            game.aim_assist.stop_side_side_moving()
                            game.next_game_state()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill('#80B2C9')

        pg.draw.line(screen, "black", center_line_start, center_line_stop, 5)

        pg.draw.circle(screen, "red", game.playerPosition1, 20)
        pg.draw.circle(screen, "blue", game.playerPosition2, 20)

        if game.activePlayer == 'left':
            x = game.activePlayerPosition + game.aim_assist.get_vector()
        else:
            x = game.activePlayerPosition - game.aim_assist.get_vector()

        pg.draw.line(screen, "yellow", game.activePlayerPosition, x, 3)
        pg.draw.circle(
            screen,
            "green",
            x,
            50,
        )
        # refresh sprites
        game.game_pieces.update(
            x,
            game.get_game_state(),
            game
        )
        game.game_pieces.draw(screen)

        game.aim_assist.update(game.get_game_state())

        # flip() the display to put your work on screen
        pg.display.flip()

        match game.get_game_state():
            case 'hit'|'reset':
                game.next_game_state()
            case'rethrow_hit':
                print(game.aim_assist.get_vector())

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pg.quit()
    return


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

    def next_game_state(self):
        match self.game_state:
            case 'aim_assist':
                self.game_state = 'trow_power'
                self.aim_assist.start_side_side_moving()
            case 'trow_power':
                self.game_state = 'hit'
            case 'hit':
                self.game_state = 'reset'
            case 'rethrow':
                self.game_state = 'rethrow_aim_assist'
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
        print(self.game_state)
    def get_game_state(self):
        return self.game_state

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
