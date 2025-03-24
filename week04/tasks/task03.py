import matplotlib.pyplot as plt

fruits = ['Mango', 'Orange', 'Plum', 'Pineapple', 'Melon']
data = [45, 30, 15, 30, 30]
plt.figure(figsize=(8, 8))
plt.pie(data, labels=fruits)
plt.title("Favorite Fruits")
plt.show()
