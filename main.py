import pygame

from objects.Game import Game

# parser = argparse.ArgumentParser()
# parser.add_argument('--debug', choices=['true'])
# args = parser.parse_args()

game = Game()
game.crate_players(6)

# if args.debug=='true':
#     exit('Debug mode exit now ...')

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

centerLineStart = pygame.Vector2(screen.get_width() / 2, 0)
centerLineStop = pygame.Vector2(screen.get_width() / 2, screen.get_height())

playerPosition1 = pygame.Vector2(0, screen.get_height() / 2)
playerPosition2 = pygame.Vector2(screen.get_width(), screen.get_height() / 2)

playerNumber = 2
gamePieceNumber = 6





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.line(screen, "black", centerLineStart, centerLineStop, 5 )
    pygame.draw.circle(screen, "red", playerPosition1, 20)
    pygame.draw.circle(screen, "blue", playerPosition2, 20)
    pygame.draw.line(screen, "yellow", playerPosition1, centerLineStart, 3)
    pygame.draw.line(screen, "yellow", playerPosition1, centerLineStop, 3)
    #pygame.draw.line


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
