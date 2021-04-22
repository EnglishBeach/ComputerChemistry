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


X = np.array([1,2,3,4,5,6,7,8,9,10])
Ypr = np.array([2,3,1,4,5,7,6,10,11,13])
length = len(X)

extend = 4

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
A=[]
for i in range(extend):
    Mi = M.copy()
    Mi[:,i] = B
    # print('M %s'% i)
    # print(pd.DataFrame(Mi))
    detMi = lin.det(Mi)
    ai = detMi/detM
    A.append(ai)
A =np.array(A)
print('     Решения:')
print(pd.DataFrame(A))

M2 = lin.solve(M,B)
print('     Решения Numpy:')
print(pd.DataFrame(M2))

Y=[]
for i in X:
    s=0
    for n in range(len(A)):
        s+=i**n*A[n]
    Y.append(s)


plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(X, Ypr,color='Black')
plt.plot(X, Y)
plt.grid(True)
plt.show()
