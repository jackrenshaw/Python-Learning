from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as image
from numpy import linalg
import numpy
import math

img = image.imread("bliss.png")
plt.imshow(img)
plt.show()

scaleFactor = 0.333
## Linear Interpolation
newImg = numpy.empty((scaleFactor*img.shape[0],scaleFactor*img.shape[1],img.shape[2]))

for i,x in enumerate(newImg):
    for j,y in enumerate(x):
        newImg[i,j] = img[int(math.floor(i/scaleFactor-1)),int(math.floor(j/scaleFactor-1))]

plt.imshow(newImg)
plt.show()
