import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
data = [23, 45, 56, 78, 213]
plt.bar(x, data, width=0.5, color='maroon')
plt.title("A bar plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.show()
