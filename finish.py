import numpy as np 
import matplotlib.pyplot as plt
with open("counting3.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(500)])
	print sum(results)/500
with open("notcounting3.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(500)])
	print sum(results)/500

