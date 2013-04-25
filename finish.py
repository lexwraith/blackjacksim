import numpy as np 
import matplotlib.pyplot as plt

with open("noncounting.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(500)])
	print sum(results)/500

with open("counting.txt","r") as f:
	results = np.array([float(f.readline().strip()) for x in range(500)])
	print sum(results)/500