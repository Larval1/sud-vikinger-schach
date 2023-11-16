from objects.WikingKing import WikingKing
from objects.Wiking import Wiking


class Game():
    def __init__(self):
        print('im going to summon 6 Wikings and 1 WikingKing')
        self.wikings = self._summon_wikinger()

    def _summon_wikinger(self):
        wikinger = []
        for i in range(0, 2):
            wikinger.append(Wiking())
        wikinger.append(WikingKing())
        for i in range(0, 2):
            wikinger.append(Wiking())

        return wikinger
