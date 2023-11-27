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
    #all_sprites =

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('#80B2C9')

    pg.draw.line(screen, "black", center_line_start, center_line_stop, 5)

    # for i in range(0, len(game.game_pieces)):
    #    x = game.game_pieces[i]
    #    pg.draw.circle(screen, x.color, x.pos, 20)

    # for i in range(0, len(game.players)):
    #    x = game.players[i]
    #    pg.draw.circle(screen, x.color, x.pos, 20)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill('#80B2C9')

        pg.draw.line(screen, "black", center_line_start, center_line_stop, 5)

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            game.throw_power_bar.trow_power_increase(dt)
        else:
            game.throw_power_bar.trow_power_decrease(dt)

        pg.draw.line(
            screen,
            "pink",
            power_bar_start,
            pg.Vector2((screen.get_width() / 100) * 99,
                       screen.get_height() - (screen.get_height() / 100) * game.throw_power_bar.get_throw_power()),
            5
        )

        game.aim_assist.move_aim_assist(dt)
        # game.aim_assist.

        pg.draw.line(
            screen,
            "green",
            pg.Vector2(0, screen.get_height() / 2),
            pg.Vector2(screen.get_width() / 2, screen.get_height() / 100 * 50),
            5
        )

        pg.draw.circle(screen, "red", playerPosition1, 20)
        pg.draw.circle(screen, "blue", playerPosition2, 20)

        # pg.draw.line(screen, "yellow", playerPosition1, centerLineStart, 3)
        # pg.draw.line(screen, "yellow", playerPosition1, centerLineStop, 3)

        # refresh sprites
        # screen.blit(pg.Surface(screen.get_size()), (0, 0))
        game.game_pieces.update()
        game.game_pieces.draw(screen)
        # flip() the display to put your work on screen

        pg.display.flip()

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
    def __init__(self):
        self.aim_assist = None
        self.throw_power_bar = None
        self.player_list = []
        self.game_pieces = []

    def setup_game(self, screen):
        self.throw_power_bar = ThrowPowerBar()
        self.aim_assist = AimAssist(screen)

        self.create_players(2, screen.get_width(), screen.get_height())

        self.game_pieces = pg.sprite.RenderPlain(self.setup_game_pieces(screen.get_width(), screen.get_height()))
        #self.setup_game_pieces(screen.get_width(), screen.get_height())

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
