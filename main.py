import argparse
import logging
import objects.Game as Game

parser = argparse.ArgumentParser()
parser.add_argument('--logLevel', choices=['debug'],default='warning')
args = parser.parse_args()

numeric_level = getattr(logging, args.logLevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.debug)
logging.basicConfig(level=numeric_level,format='%(levelname)s:%(message)s')

Game.start_game(args)
