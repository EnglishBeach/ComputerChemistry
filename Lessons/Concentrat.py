import math as mt
import pandas as pnd
import matplotlib.pyplot as plt

Kb = 8.6165E-5


def fC(t):
    T = lambda t: T0 + (Tk - T0) * (1 - exp(-t / q))
    k = lambda t: (-E / Kb - T(t))
    c = lambda t: c0 * exo(-k * t)
    return c


def kotes(f, llim, rlim, kotes_number=3):
    """Вычисляет интеграл методом Котеса

    Args:
        a (float): Левая граница
        b (float): Правая граница
        n (int, optional): Число Котеса.
    Returns:
        (float): Значение интеграла
    """
    dx = (rlim - llim) / kotes_number
    s = 0
    A = []
    for i in range(8):
        A.append(0)

    if kotes_number == 1:
        A[0] = 1
        A[1] = 1
        N = 2
    elif kotes_number == 2:
        A[0] = 1
        A[1] = 4
        A[2] = 1
        N = 6
    elif kotes_number == 3:
        A[0] = 1
        A[1] = 3
        A[2] = 3
        A[3] = 1
        N = 8
    suma = 0
    for i in range(kotes_number):
        suma += A[i] * f(llim + dx * i)

    return kotes_number * dx * suma / N


# Входные данные
E = 1
q = 1

time_end = 100

Tstart = 300
Tend = 900

numberT = 6
dT = (Tstart - Tend) / numberT

quality = 0.1

C = []
T = []
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

            s += kotes(fC,
                       kotes_number=2,
                       llim=dtime * ntime,
                       rlim=dtime * (ntime + 1))

        if abs(s - s0) / s < quality: break
        i += 1
        s0 = s
    print(s)
    C.append('{0: > 5.2} M'.format(s))
    T.append('{0: > 5.2} K'.format(T0))

f = pd.DataFrame({'Concentrations': C, 'Temperatures': T})
plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(T, C)
plt.grid(True)
plt.show()

print(f)
