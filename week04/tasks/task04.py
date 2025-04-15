import matplotlib.pyplot as plt

x = ["red", "silver", "blue", "white", "green"]
y = [123, 230, 78, 193, 12]
myExplode = [0.3, 0, 0, 0, 0]

plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.title("Car")
plt.bar(x, y, width=0.3, color=x)
plt.subplot(2, 2, 2)
plt.title("Car")
plt.barh(x, y, color=x)
plt.subplot(2, 2, 3)
plt.title("Car")
plt.pie(y, labels=x, colors=x, explode=myExplode, shadow=True)
plt.legend(title="Car Colors")
plt.tight_layout()
plt.show()
