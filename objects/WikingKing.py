from objects.Wiking import Wiking

class WikingKing(Wiking):
    def __init__(self,wiking_nummber):
        super().__init__(wiking_nummber)
        print(f'but wait {self.wiking_nummber} is also the king')
