import numpy as np
"""
I decided to make the shoe NumPy and the hand NOT NumPy.
It made sense to make the shoe NumPy, especially with larger decks.
That logic didn't seem to matter as much for individual hands.
I also just create a new deck when the shoe is up. Seems faster
and more logical.

Notes from last time:
Dealer stands iff dealer is hard 17.
Surrendering allows you to get half your bet back
Implement a "stand" flag for players
Blackjack gets you your money immediately.
"""

class shoe:
    def __init__(self,
                 size,
                 deck = ["A",2,3,4,5,6,7,8,9,10,10,10,10],
                 decksets = 4
                     ):
        decksize = decksets * len(deck)
        self.deck = np.array(deck * decksize * size)
        """
        Yellow card is the mark at which the dealer will shuffle.
        The shoe's count variable is the counter towards yellow card,
        NOT the count used for betting progression.
        """
        self.yellowcard = np.random.randint(self.deck.size/2,self.deck.size-30)
        self.count = 0
        self.reset = False
        np.random.shuffle(self.deck)

    def show(self):
        print(self.deck)

    def deal(self):
        self.count += 1
        if self.count > self.yellowcard : self.reset = True
        todeal = self.deck[0]
        if(not todeal == "A"): (int(todeal))
        self.deck = np.delete(self.deck,0)
        return todeal

class player:
    def __init__(self,bank,lowbet = 25, hibet = 100):
        self.hand = []
        self.bank = bank
        self.low = lowbet
        self.high = hibet
        self.done = False
        self.bet = 0
        self.betbig = False
    
    def evalhand(self):
        if(not 11 in self.hand and not 1 in self.hand):
            return sum(self.hand)
        else:
            while(sum(self.hand) > 21):
                if(11 in self.hand):
                    self.hand[self.hand.index(11)] = 1
                else:
                    break
            return sum(self.hand)

    def get(self,card):
        if(card == "A" and sum(self.hand) <= 10):
            self.hand.append(11)
        elif(card == "A"):
            self.hand.append(1)
        else:
            self.hand.append(int(card))

    def reset(self):
        self.hand = []

    def show(self):
        print(self.hand)

x = shoe(2)
jamie = player(1000)
for z in range(5):
    jamie.get(x.deal())
jamie.show()
print(jamie.evalhand())
jamie.show()

