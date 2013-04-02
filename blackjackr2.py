import numpy as np

class shoe:
    def __init__(self,
                 size,
                 deck = ["A",2,3,4,5,6,7,8,9,10,10,10,10],
                 decksets = 4
                     ):
        decksize = decksets * len(deck)
        self.deck = np.array((decksize) * size)
        """
        Yellow card is the mark at which the dealer will shuffle.
        The shoe's count variable is the counter towards yellow card,
        NOT the count used for betting progression.
        """
        print(self.deck)
        self.yellowcard = np.random.randint(self.deck/2, self.deck - 30)
        self.count = 0
        self.reset = False
        np.random.shuffle(self.deck)

    def show(self):
        print(self.deck)

    def deal(self):
        self.count += 1
        if count > yellowcard : self.reset = True
        todeal = self.deck[0]
        np.delete(self.deck,0)

x = shoe(2)
x.show()

