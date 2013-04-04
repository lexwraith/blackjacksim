"""
Dealer can either stand on all 17's or only hard 17's in casinos
Need to implement blackjack check
Surrendering can allow you to get half your bet
Implement "stand" flag for players
Currently assuming house wins in blackjack tie
Implement "yellow card" signifying end of desk.
"""

standard = ["A",2,3,4,5,6,7,8,9,10,10,10,10]
from random import shuffle
import numpy as np

wizard = True

class decks:
	"""Effectively the shoe"""
	def __init__(self,size,decktype):
		self.size = size
		self.deckstyle = decktype
		self.shoe = []
		self.generate()
		self.garbage = []
		self.count = 0

	def generate(self):
		self.shoe = [(self.deckstyle[i]) for i in range(13) for z in range(4) for j in range(self.size)]
		for x in range(2): shuffle(self.shoe)

	def spit(self):
		if(len(self.shoe) == 0): 
			self.shoe = self.garbage
			self.garbage = []
			self.count = 0
		toreturn = self.shoe[0]
		del self.shoe[0]
		return toreturn;

	def shuffle(self):
		shuffle(self.shoe)

	def showshoe(self):
		print(self.shoe)

	def showgarbage(self):
		print(self.garbage)

	def isempty(self):
		if(len(self.shoe) == 0): return True

	def get(self,hand):
		"""
		For collecting up used cards in garbage
		"""
		for elem in hand:
			self.garbage.append(elem)

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



def deal(player,shoe):
	mybuffer = shoe.spit()
	if(mybuffer in [2,3,4,5,6,7]):
		shoe.count += 1
	if(mybuffer == 10):
		shoe.count -= 1
	if(mybuffer == "A"):
		shoe.count -= 1
	player.get(mybuffer)

def runtests(numplayers,shoesize,magicnumber,bankroll,lowbet,highbet):
	players = [player(bankroll,lowbet,highbet) for z in range(numplayers)]
	table = player(1000000,5,25)
	shoe = decks(shoesize,standard)
	shoe.count = 0
	rounds = 0
	while(rounds < 1000):
		#Counter
		rounds += 1

		#Players placing their bets
		for person in players:
			if(shoe.count > 0): 
				person.bet = person.high
			else: 
				person.bet = person.low 
			person.bank -= person.bet
			#person.bet = person.high if person.betbig else person.low
			#person.bank -= person.bet

		#Dealing the cards
		for z in range(2):
			for x in range(len(players)):
				deal(players[x],shoe)
			deal(table,shoe)
		

		#Check if a player got blackjack 
		for person in players: 
			if person.eval() == 21: person.bank += person.bet + person.bet*2.5
			person.bet = 0
			person.done = True
		
		#Players turn to hit/stand
		for person in players:
			if(wizard):
				while(True):
					if person.eval >= 17: break;
					if person.eval() < 12: deal(player,shoe)
					elif person.eval() < 17 and table.eval() < 12: deal(player,shoe)
					

			else:
				while(person.eval() < 12 and shoe.count < magicnumber):
					deal(person,shoe)
					if(person.eval() > 21):
						person.lost()
						shoe.get(person.rem())
				if(person.eval() > 11 and shoe.count > magicnumber):
					deal(person,shoe)
					if(person.eval() > 21):
						person.lost()
						shoe.get(person.rem())
			
		#If dealer has 21, everyone automatically loses (for now)
		if(table.eval() == 21):
			for person in players:
				person.lost()

		#Dealer's turn to get cards
		while(table.eval() < 18 and "A" in table.hand):
			#Arbitrary hit at soft 17 and lower
			deal(table,shoe)
		
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

		for person in players:
			shoe.get(person.rem())
			shoe.get(table.rem())
			person.done = False
	return players[0].bank

last = 5
results = []

PLAYERS = 1
DECKS = 5
SPECIAL = 10
INITIAL = 2500
MINBET = 5
MAXBET = 25

for i in range(100):
	while last < 2500 and last > 0:
		last = runtests(PLAYERS,DECKS,SPECIAL,INITIAL,MINBET,MAXBET)
		results.append(last)
	if results < INITIAL: SPECIAL -= 1
	if results > INITIAL: SPECIAL += 1
	last = 5
print results
