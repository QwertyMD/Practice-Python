import matplotlib.pyplot as plt

years = {
    "2017": [8, 150, 80],
    "2018": [54, 77, 54],
    "2019": [93, 32, 100],
    "2020": [116, 11, 76],
    "2021": [137, 6, 93],
    "2022": [184, 1, 72],
}
plt.figure(figsize=(8, 8))
animals = ["Bears", "Dolphins", "Whales"]
for i, (key, val) in enumerate(years.items(), start=1):
    plt.subplot(3, 2, i)
    plt.title(key)
    plt.pie(val, labels=animals)
plt.tight_layout()
plt.show()
