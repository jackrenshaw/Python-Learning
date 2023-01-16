# Travelling Salesman Problem
import numpy as np
import math
n = 5
x = np.random.randint(0, 50, n)
y = np.random.randint(0, 50, n)

dist = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        dist[i][j] = math.sqrt((y[j]-y[i])**2+(x[j]-x[i])**2)

dp = np.zeros(n,2^n,n)

print (x,y)
print (dist)