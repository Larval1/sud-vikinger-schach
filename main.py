import pygame as pg

from objects.Game import Game


def game_loop(game, screen, font, clock, running, center_line_start, center_line_stop):
    while running and game.game_state != 'game_over':
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                match game.game_state:
                    case 'aim_assist' | 'rethrow_aim_assist':
                        if not game.aim_assist.up_down_moving:
                            game.aim_assist.start_up_down_moving()
                        else:
                            game.aim_assist.stop_up_down_moving()
                            game.next_game_state()
                    case 'trow_power' | 'rethrow_trow_power':
                        if not game.aim_assist.side_side_moving:
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
            30,
        )

        game.aim_assist.update(x.yx)

        print(game.activePlayerPosition.yx.x)

        # refresh sprites
        game.game_pieces.update(x, game)
        game.game_pieces.draw(screen)

        # flip() the display to put your work on screen
        pg.display.flip()

        match game.game_state:
            case 'hit' | 'reset' | 'rethrow_hit':
                game.next_game_state()

        # limits FPS to 60
        clock.tick(60) / 1000

    if game.game_state == 'game_over':
        # screen.fill('#b43126')
        text = font.render(f"{game.activePlayer} {game.gameOverMessage}", True, (255, 0, 0))
        screen.blit(text, text.get_rect(center=screen.get_rect().center))
        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    return
    pg.quit()
    return


def start_game():
    # pygame setup
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    running = True
    dt = 0
    font = pg.font.SysFont(None, 50)

    center_line_start = pg.Vector2(screen.get_width() / 2, 0)
    center_line_stop = pg.Vector2(screen.get_width() / 2, screen.get_height())

    game = Game(screen)
    game.setup_game(screen)

    game_loop(game, screen, font, clock, running, center_line_start, center_line_stop)

    pg.draw.line(screen, "black", center_line_start, center_line_stop, 5)


try:
    start_game()
except:
    print('Bai bai')
