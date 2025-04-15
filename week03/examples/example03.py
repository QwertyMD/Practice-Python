import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 3, 4, 5])
y = np.array([3, 4, 5, 6])
plt.plot(x, y, marker='o', color='red', linewidth=3)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('The Graph')
plt.show()
