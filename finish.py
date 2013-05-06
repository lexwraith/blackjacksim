import numpy as np 
import matplotlib.pyplot as plt

print "Base"
with open("COUNTING.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(5000)])
	print sum(results)/5000

with open("NOT_COUNTING.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(5000)])
	print sum(results)/5000

print "Multi Deck"

with open("2DECKS100.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("3DECKS100.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("4DECKS100.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("5DECKS100.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

print "Multi Deck 50 Count"
with open("1DECKS50.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("2DECKS50.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("3DECKS50.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("4DECKS50.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("5DECKS50.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

print "Multi Deck 25 Count"

with open("1DECKS25.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("2DECKS25.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("3DECKS25.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100
with open("4DECKS25.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100

with open("5DECKS25.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(100)])
	print sum(results)/100


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')