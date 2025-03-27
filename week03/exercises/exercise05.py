import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([[50, 40, 70, 80, 20], [80, 20, 20, 50, 60], [70, 20, 60, 40, 60], [40, 20, 30, 70, 60]])

plt.figure(figsize=(10, 8))

for i in range(4):
    j = i + 1
    plt.subplot(2, 2, j)
    plt.plot(x, y[i])
    plt.xlabel('Days')
    plt.ylabel('Distance Covered')

plt.show()
