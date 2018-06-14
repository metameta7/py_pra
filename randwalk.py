import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000

seed = 1354


random.seed(seed)

x = 0.0
y = 0.0

xlist = [x]
ylist = [y]

for i in range(n):
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    print("{:.7f} {:.7f}".format(x,y))
    xlist.append(x)
    ylist.append(y)

plt.plot(xlist,ylist)
plt.show()
