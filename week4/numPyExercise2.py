import numpy as np
from numpy import genfromtxt

arr = np.genfromtxt('week4/RandomeValues.csv', delimiter=',')
arrs = arr[[4, 6, 8]]
print(arrs)
