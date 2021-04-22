import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
import numpy.linalg as lin

def summ (degree,X):
    s=0
    for i in range(length):
        s += X[i]**degree
    return s

def summXY(degree,X,Y):
    s=0 
    for i in range(length):
        s+= X[i]**degree*Y[i]
    return s



X = np.arange(0, 1, 0.2)
Ypr= np.arange(2, 3, 0.2)
length = len(X)

INPUT = np.vstack((X,Ypr))
INPUT = INPUT.transpose()
# Вввод
print('     Ввод:')
INPUT= pd.DataFrame(INPUT,columns=['X','Y'])
print(INPUT)
print()

# Матрица невязки
M = np.zeros((length,length))
for x in range (length):
    for y in range (length):
        M[x][y]= summ(x+y,X)

# Вывод матрицы невязки
data= pd.DataFrame(M)
print('     Матрица невязки:')
print(data)
print('     Определитель:')
print('{0: >5.2f}'.format(lin.det(M)))
print()

B=M = np.zeros((length))
for y in range(length):
    B[y] = summXY(y,X,Ypr)

be = pd.DataFrame(B)
print('     Правая часть:')
print(be)
# plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
# plt.plot(X, Ypr)
# plt.grid(True)
