import objects.Game as game, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--debug', choices=['true'])
args = parser.parse_args()

if args.debug == 'true':
    print('Debug mode')

game.start_game(args)
