import numpy as np
import math as mt
import matplotlib.pyplot as plt

En = lambda x: x**2*D

def f(E):
    return 1/mt.tan(C*mt.sqrt(E)) - (2*E-V)/(2*mt.sqrt(E*(V-E)))

def dyhotomy (a, b, quality=0.0001):
    root=0
    stop=0
    max_stop = 1000
    if f(a)*f(b)>0:
        return 'error'
    while abs((b-a)/a)>quality and stop<max_stop:
        mid=(a+b)/2
        if f(a)*f(mid)<0:
            b=mid
        else:
            a=mid
        stop += 1
        root = (a+b)/2
        if stop == max_stop:
            return 'bad {0}'.format(root)
    return mid

V = 10
m = 9.10953E-28
N = 10
E0 =  1E-5
a = 10

D= 6.6262**2*1E-26/(8*m*a**2*1.60219)
C=2*mt.pi*a*mt.sqrt(2*m*1.60219)*1E+13/6.6262
E1=En(1)*0.9995

energy=[]
number=[]
i = 1
print('Number \t Конечный \t Бесконечный ящик')
while E0 < V and i < 10:
    root = dyhotomy(E0, E1)
    energy.append(root)
    number.append(i)
    i += 1
    E0 = En(i-1)*1.0005
    E1 = En(i)*0.9995
    if V <= E1: E1 = V*0.9995

energy8 = []
for i in range(1,len(energy)+1):
    energy8.append(En(i))
    print('{0: <4} | {1: >7.3f}     | {2: >7.3f}'.format(i, energy[i-1], energy8[i-1]))
         
plt.scatter(number, energy, color = 'Red',marker = '*') 
plt.scatter (number, energy8, color = 'Blue')
plt.show()