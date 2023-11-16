from objects.Knecht import Knecht
from objects.Konig import König

class Game():
    def __init__(self):
        print('im going to summon 10 Knechte and 1 King')
        self.wikinger=self._summon_wikinger()

    def _summon_wikinger(self):
        wikinger=[]
        for i in range(0,2):
            wikinger.append(Knecht())

        for i in range(0,2):
            wikinger.append(König())

        return wikinger
