import matplotlib.pyplot as plt

y = [100, 205, 307, 409, 200]
groups = ['Pulsar', 'Duke', 'Enfield', 'Honda', 'Hero']
plt.pie(y, labels=groups)
plt.show()
