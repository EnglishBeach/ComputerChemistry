import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
import numpy.linalg as lin
import pylab


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
# Ввод
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
step = (Xmax - Xmin) / nstep

# Построение линии
for i in np.arange(Xmin, Xmax + step, step):
    s = 0
    Xteor.append(i)
    for n in range(len(A)):
        s += i**n * A[n]
    Yteor.append(s)
pylab.xkcd()
plt.figure(figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.title('Аппроксимация')

plt.scatter(X, Ypr, color='Black')

plt.plot(Xteor, Yteor, "b-", label="$f(x)$")

plt.grid(False)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks([i for i in np.arange(0, 1.1, 0.2)],
           ['{0: >1.1f} ед'.format(i) for i in np.arange(0, 1.2, 0.2)])
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0.5))

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_color('none')
# ax.spines['left'].set_position(('data',0))

plt.xlim(0, 1.1)

# plt.annotate(r'$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$',
#              xy=[0.5, 1],
#              xycoords='data',
#              xytext=[60, 30],
#              fontsize=20,
#              textcoords='offset points',
#              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.9"))
plt.show()
