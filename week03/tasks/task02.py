import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([[50, 40, 70, 80, 20], [80, 20, 20, 50, 60], [70, 20, 60, 40, 60], [40, 20, 30, 70, 60]])

plt.title('Bike Details')
plt.xlabel('Days')
plt.ylabel('Distance Covered')
plt.plot(x, y.T)
plt.show()
