import numpy
from numpy import random
piEstimates = []
for i in range(1000):
    pointset = random.random_sample((1000,3))*2-1
    insideCircle = [p for p in pointset if numpy.sqrt(p[0]*p[0]+p[1]*p[1]+p[2]*p[2])<1]
    piEstimates.append(len(insideCircle)/len(pointset)*6)

print(numpy.average(piEstimates))