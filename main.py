import objects.Game as game
import logging ,argparse

parser = argparse.ArgumentParser()
parser.add_argument('--logLevel', choices=['debug'],default='warning')
args = parser.parse_args()

numeric_level = getattr(logging, args.logLevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.debug)
logging.basicConfig(level=numeric_level)

game.start_game(args)
