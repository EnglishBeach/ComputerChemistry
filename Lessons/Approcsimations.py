import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
import numpy.linalg as lin


def summ(degree, X):
    s = 0
    for i in range(length):
        s += X[i]**degree
    return s


def summXY(degree, X, Y):
    s = 0
    for i in range(length):
        s += X[i]**degree * Y[i]
    return s


X = np.arange(0, 1.1, 0.1)
Ypr = np.array([
    0.53284, 0.632592, 0.951817, 1.071767, 1.366545, 1.455831, 1.65461,
    1.895859, 2.146855, 2.207135, 2.57399
])
length = len(X)

extend = 2

INPUT = np.vstack((X, Ypr))
INPUT = INPUT.transpose()
# Вввод
print('     Ввод:')
INPUT = pd.DataFrame(INPUT, columns=['X', 'Y'])
print(INPUT)
print()

# Матрица невязки
M = np.zeros((extend, extend))
for x in range(extend):
    for y in range(extend):
        M[x][y] = summ(x + y, X)

print('     Матрица невязки:')
print(pd.DataFrame(M))
print('     Определитель:')
detM = lin.det(M)
print('{0: >5.2f}'.format(detM))
print()

# Матрица правой части
B = np.zeros((extend))
for y in range(extend):
    B[y] = summXY(y, X, Ypr)

print('     Правая часть:')
print(pd.DataFrame(B))

# Решение методом крамера
A = []
for i in range(extend):
    Mi = M.copy()
    Mi[:, i] = B
    # print('M %s'% i)
    # print(pd.DataFrame(Mi))
    detMi = lin.det(Mi)
    ai = detMi / detM
    A.append(ai)
A = np.array(A)
print('     Решения:')
print(pd.DataFrame(A))

M2 = lin.solve(M, B)
print('     Решения Numpy:')
print(pd.DataFrame(M2))

Yteor = []
Xteor = []
nstep = 20
Xmin = np.min(X)
Xmax = np.max(X)
step = (Xmax- Xmin)/nstep

for i in np.arange(Xmin,Xmax,step):
    s = 0
    Xteor.append(i)
    for n in range(len(A)):
        s += i**n * A[n]
    Yteor.append(s)

plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(X, Ypr, color='Black')
plt.plot(Xteor, Yteor)
plt.grid(True)
plt.show()
