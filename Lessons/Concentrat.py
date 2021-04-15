import math as mt
import pandas as pd
import matplotlib.pyplot as plt

Kb = 8.6165E-5


def fC(t):
    T = lambda t: T0 + (T1 - T0) * (1 - mt.exp(-t / q))
    k = lambda t: (-E / Kb - T(t))
import numpy as np
    c = lambda t: c0 * mt.exp(-Kb * t)
    return c(t)

def kotes(f,a, b, n=3):
    """Вычисляет интеграл методом Котеса

    Args:
        a (float): Левая граница
        b (float): Правая граница
        n (int, optional): Число Котеса.
    Returns:
        (float): Значение интеграла
    """
    dx = (b - a) / n
    s = 0
    A = []
    for i in range(8):
        A.append(0)

    if n == 1:
        A[0] = 1
        A[1] = 1
        N = 2
    elif n == 2:
        A[0] = 1
        A[1] = 4
        A[2] = 1
        N = 6
    elif n == 3:
        A[0] = 1
        A[1] = 3
        A[2] = 3
        A[3] = 1
        N = 8
    suma = 0
    for i in range(8):
        suma += A[i] * f(a + dx * i)

    return n * dx * suma / N

# Входные данные
E = 1
q = 1
c0 = 0.0
k= 1

time_end = 100

Tstart = 300
Tend = 900

numberT = 6
dT = (Tend - Tstart) / numberT

quality = 0.1

C = []
T = []
C.append('{0: > 5.2} M'.format(c0))
T.append('{0: > 5.1f} K'.format(Tstart))
for nT in range(numberT):
    T0 = Tstart + dT * nT
    T1 = Tstart + dT * (nT + 1)
    # Цикл сходимости
    i = 0
    while True:
        number_time = 4 * 2**i

        dtime = time_end / number_time

        # Цикл разбиений
        s0 = 0
        s = 0
        for ntime in range(number_time):
            s += kotes(f = fC,
                       n=2,
                       a=dtime * ntime,
                       b=dtime * (ntime + 1))
        
        try:
            koef = abs(s - s0) / s0 
        except ZeroDivisionError:
            koef = 0
        if koef < quality: break

        i += 1

        s0 = s
    C.append('{0: > 5.2} M'.format(s))
    T.append('{0: > 5.1f} K'.format(T1))

f = pd.DataFrame({'Concentrations': C, 'Temperatures': T})
# plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
# plt.plot(T, C)
# plt.grid(True)
plt.show()

print(f)
