import matplotlib.pyplot as plt
from math import pi

x = []
y1 = []
y2 = []
y3 = []
for i in range(1, 21):
    x.append(i)
    j1 = 5 * i ** 3 + 2 * i - 1
    j2 = -2 * i ** 3 + i ** 2 + 100
    j3 = 2 * pi * i + 20
    y1.append(j1)
    y2.append(j2)
    y3.append(j3)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
plt.show()
