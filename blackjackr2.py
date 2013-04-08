import numpy as np
"""
I decided to make the shoe NumPy and the hand NOT NumPy.
It made sense to make the shoe NumPy, especially with larger decks.
That logic didn't seem to matter as much for individual hands.
I also just create a new deck when the shoe is up. Seems faster
and more logical.

Notes from last time:
Dealer stands iff dealer is hard 17.
Blackjack gets you your money immediately, as opposed to pushing if dealer also blackjacks.
The arbitrary truecount for these simulations will be +2.
    If truecount >= +2, players will not hit.
"""


class shoe:
    def __init__(self,
                 size,
                 deck = ["A",2,3,4,5,6,7,8,9,10,10,10,10],
                 decksets = 4
                 ):
        decksize = decksets * len(deck)
        self.deck = np.array(deck * decksize * size)
        #Marking when to use a new deck
        self.yellowcard = np.random.randint(self.deck.size/2,self.deck.size-30)
        #Counter towards the yellowcard
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
    def __init__(self,
                 bank,
                 lowbet = 25, 
                 hibet = 100,
                 countsystem = {"2":1, "3":1, "4":1, "5":1, "6":1, 
                                "7":0, "8":0, "9":0, "10":-1, "A":-1},
                 countaccuracy = 100
                 ):
        self.hand = []
        self.bank = bank
        self.low = lowbet
        self.high = hibet
        self.done = False
        self.bet = 0
        self.mycount = 0
        self.betbig = False
        self.countsystem = countsystem
        self.countaccuracy = countaccuracy

    def evalhand(self):
        """
        This method might be a bit redundant
        but it allows adjustment of hands to optimal
        value. It is useful post deal.
        """
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

    def count(self,card):
        """
        Currently this only allows players to mis-read
        cards, i.e. not factoring them into count.
        """
        if(np.random.randint(0,self.countaccuracy + 1)):
            self.mycount += self.countsystem[card]

class dealer:
    def __init__(self):
        self.hand = []
        
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
        
    def show(self):
        print(self.hand)

    def reset(self):
        self.hand = []

    def get(self,card):
        if(card == "A" and sum(self.hand) <= 10):
            self.hand.append(11)
        elif(card == "A"):
            self.hand.append(1)
        else:
            self.hand.append(int(card))

#players = np.array([player(1000),player(1000)],dtype=object)
#players[:].get(x.deal())



def dealplayer(shoe,player,table):
    """
    This method handles dealing cards and counting.
    """
    dealing = shoe.deal()
    for card_counters in table:
        card_counters.count(dealing)
    player.get(dealing)

def runtest(num_players,numdecks = 1,initial_bank = 1000):
    tableshoe = shoe(numdecks)
    """
    Unsure if I want to make dealer part of the table.
    table = np.array([dealer()])
    table = np.append(table,[player(initial_bank) for z in range(num_players)])
    """
    tabledealer = dealer()
    table = np.array([player(initial_bank,countaccuracy = 50) for z in range(num_players)])
    
    #Placing bets
    """
    Is there a point in making a wager memory slot?
    For now I'm ignoring this.
    """

    #Initial deal
    for i in range(2):
        for seat in table:
            dealplayer(tableshoe,seat,table)
        dealplayer(tableshoe,tabledealer,table)
    
    #Check for blackjack
    for seat in table:
        if(seat.evalhand() == 21):
            seat.bank += seat.high * 1.5 if seat.betbig else seat.low * 1.5
            seat.done = True

    #Player options
    for seat in table:
        if(seat.done): continue
        while(seat.evalhand() <= 10):
            dealplayer(tableshoe,seat,table)
        #Arbitrary counting rule 1
        if(seat.evalhand() <= 12 and seat.mycount/numdecks < -1):
            dealplayer(tableshoe,seat,table)
        #Arbitrary counting rule 2
        if(seat.evalhand() <= 15 and seat.mycount/numdecks < -2):
            dealplayer(tableshoe,seat,table)
        seat.done = True


        #At this point I am considering implementing basic strategy
        #for the non-counting player

    #Dealer checks for blackjack
    if(tabledealer.evalhand() == 21):
        pass

    #Dealer options
    while(tabledealer.evalhand() < 18):
        dealplayer(tableshoe,tabledealer,table)

    #Check if dealer busts
    if(tabledealer.evalhand > 21):
        for seat in table:
            seat.bank += seat.high if seat.betbig else seat.low
    else:
    #Evaluate remaining vs dealer
        for seat in table:
            if (seat.evalhand() > 21) or (tabledealer.evalhand >= seat.evalhand()):
                seat.bank -= seat.high if seat.betbig else seat.low
            else:
                seat.bank += seat.high if seat.betbig else seat.low
    #Check if we need a new shoe

    for seats in table:
        print seats.hand,seats.bank,seats.mycount
  
    print tabledealer.hand

    if(tableshoe.reset):
        tableshoe = shoe(numdecks)

runtest(5,1000)

