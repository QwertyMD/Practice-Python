import matplotlib.pyplot as plt

x = []
y = []
for i in range(1, 11):
    x.append(i)
for i in range(1, 51):
    if i % 5 == 0:
        y.append(i)
colors = ["red", "green", "blue", "yellow", "pink", "orange", "purple", "brown", "cyan", "magenta"]
plt.scatter(x, y, c=colors)
plt.show()
