import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [3, 4, 5, 6, 7, 1, 9, 2, 5]
# plt.plot(x,y)
plt.scatter(x, y, color='red', marker='^')
x1 = [1, 5, 6, 8, 12]
y1 = [2, 6, 7, 11, 13]
plt.scatter(x1, y1, color='blue', marker='s')
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title("Scatter plot")
plt.show()
