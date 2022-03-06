import matplotlib.pyplot as plt

X = []
Y = []

for i in range(10):
    X.append(i)
    Y.append(3 * i**2)


plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(X, Y)
plt.grid(True)
plt.show()