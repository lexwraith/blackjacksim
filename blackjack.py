"""
Dealer can either stand on all 17's or only hard 17's in casinos
Need to implement blackjack check
Surrendering can allow you to get half your bet
Implement "stand" flag for players
Currently assuming house wins in blackjack tie
"""

standard = ["A",2,3,4,5,6,7,8,9,10,10,10,10]
from random import shuffle

class decks:
	"""Effectively the shoe"""
	def __init__(self,size,decktype):
		self.size = size
		self.deckstyle = decktype
		self.shoe = []
		self.generate()
		self.garbage = []

	def generate(self):
		self.shoe = [(self.deckstyle[i]) for i in range(13) for z in range(4) for j in range(self.size)]
		for x in range(2): shuffle(self.shoe)

	def spit(self):
		if(len(self.shoe) == 0): 
			self.shoe = self.garbage
			self.garbage = []
		toreturn = self.shoe[0]
		del self.shoe[0]
		return toreturn;

	def shuffle(self):
		shuffle(self.shoe)

	def showshoe(self):
		print(self.shoe)

	def isempty(self):
		if(len(self.shoe) == 0): return True

	def get(self,card):
		"""
		Used for leftover cards in the event the dealer
		runs out of cards for the current hand and needs
		to use old ones.
		"""

class player:
	"""Players that can come in and out"""
	def __init__(self,bank,lowbet,hibet):
		self.hand = []
		self.bank = bank
		self.low = lowbet
		self.high = hibet
		self.done = False
		self.bet = 0
		self.betbig = False
	def eval(self):
		if("A" not in self.hand): 
			return(sum(self.hand))
		else:
			while("A" in self.hand):
				self.hand[self.hand.index("A")] = 11
			while(sum(self.hand) > 21):
				if(11 in self.hand):
					self.hand[self.hand.index(11)] = 1
				else:
					break
			return sum(self.hand)
	
	def get(self,card):
		self.hand.append(card)

	def rem(self):
		garbage = self.hand
		self.hand = []
		return garbage

	def lost(self):
		self.done = True
		self.bank -= self.bet
		self.bet = 0

class table:
	def __init__(self,bank):
		self.slots = []
		self.hand = []

	def addplayer():
		self.slots.append(player(1000,5,25))

	def remplayer(index):
		del(self.slots[index])

	def eval(self):
		if("A" not in self.hand): 
			return(sum(self.hand))
		else:
			while("A" in self.hand):
				self.hand[self.hand.index("A")] = 11
			while(sum(self.hand) > 21):
				if(11 in self.hand):
					self.hand[self.hand.index(11)] = 1
				else:
					break
		return sum(self.hand)


def runtests(numplayers,shoesize,magicnumber,bankroll,lowbet,highbet):
	players = [player(bankroll,lowbet,highbet) for z in range(numplayers)]
	table = player(1000000,5,25)
	shoe = decks(shoesize,standard)
	rounds = 0
	while(rounds < 1000):
		#Counter
		rounds += 1

		#Players placing their bets
		for person in players:
			person.bet = person.high if person.betbig else person.low
			person.bank - person.bet

		#Dealing the cards
		for z in range(2):
			for x in range(len(players)):
				players[x].get(shoe.spit())
			table.get(shoe.spit())
		

		#Check if a player got blackjack 
		for person in players: 
			if person.eval() == 21: person.bank += person.bet + person.bet*2.5
			person.bet = 0
		
		#Players turn to hit/stand
		for person in players:
			#Arbitary rule hitting while under 17
			while(person.eval() < 17):
				person.get(shoe.spit())
				if(person.eval() > 21):
					person.lost()
					shoe.garbage.append(person.rem())
		
		#If dealer has 21, everyone automatically loses (for now)
		if(table.eval() == 21):
			for person in players:
				person.lost()

		#Dealer's turn to get cards
		while(table.eval() < 18):
			#Arbitrary hit at 17
			table.get(shoe.spit())
		
		#Check to see if dealer is over
		if(table.eval() > 21):
			for person in players:
				if(person.done):
					person.bank += person.bet
		
		#Evaluate survivors against dealer
		for person in players:
			if person.done:
				continue
			if table.eval() == person.eval():
				person.lost()
			if table.eval() > person.eval():
				person.lost()
			else:
				person.bank += person.bet

		#print([players[x].eval() for x in range(numplayers)],table.eval())
		#print([round(players[x].bank/float(bankroll),2) for x in range(numplayers)])
		#print([players[x].hand for x in range(numplayers)])

		#Takeback all cards and put it in garbage
		for person in players:
			shoe.garbage.append(person.rem())
		

		



runtests(5,5,17,1000,5,100)


