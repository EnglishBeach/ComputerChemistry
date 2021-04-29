import math as mt
import pandas as pd
import matplotlib.pyplot as plt

# Константы
KB = 8.6165E-5
E = 1
VALUME_CHANGE_T = 1
C0 = 1
K = 1

# Входные данные
TSTART = 300
TEND = 400
NUMBER_T = 10
QUALITY = 0.1

TIME = 100
MAXTIMEPOINTS = 200


def f(t, T0, T1, c0):
    temp = lambda t: T0 + (T1 - T0) * (1 - mt.exp(-t / VALUME_CHANGE_T))
    k = lambda t: K*mt.exp(-E / (KB * temp(t)))
    c = lambda t: c0 * mt.exp(-k(t) * t)
    return c(t)


def kotes(f, a, b, n=3, **kwargs):
    """Вычисляет интеграл методом Котеса

    Args:
        a (float): Левая граница
        b (float): Правая граница
        n (int, optional): Число Котеса.
    Returns:
        (float): Значение интеграла
    """
    dx = (b - a) / n
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
        suma += A[i] * f(t=a + dx * i, **kwargs)
    return n * dx * suma / N


def kotes_quality(f, llim, rlim, quality=0.1, n=3, **kwargs):
    s0 = kotes(f, a=llim, b=rlim, n=n, **kwargs)
    i = 0
    while True:
        npoints = 4 * 2**i
        step = (llim - rlim) / npoints
        s = 0
        for point in range(npoints):
            s += kotes(f,
                       a=llim + step * point,
                       b=llim + step * (point + 1),
                       n=n,
                       **kwargs)
        if abs((s - s0) / s0) < quality and npoints > MAXTIMEPOINTS: return s
        i += 1


def main(f):
    # Перебор температур
    dT = (TEND - TSTART) / NUMBER_T
    c = C0
    data = pd.DataFrame({'Concentration:': [C0], 'Temperature:': [TSTART]})
    for Temp in range(NUMBER_T):
        Temp0 = TSTART + dT * Temp
        Temp1 = TSTART + dT * (Temp + 1)

        c = kotes_quality(f,
                          llim=0,
                          rlim=TIME,
                          quality=QUALITY,
                          n=2,
                          T0=Temp0,
                          T1=Temp1,
                          c0=c)
        data = data.append({'Concentrations': [c], 'Temperatures': [Temp1]})

        # # Цикл сходимости
        # i = 0
        # while True:
        #     ntime = 4 * 2**i
        #     dtime = TIME / ntime

        #     # Цикл разбиений
        #     s0 = 1
        #     summa = 0

        #     for ntime in range(ntime):
        #         summa += kotes(f, n=2, a=dtime * ntime, b=dtime * (ntime + 1),T0=T0,T1=T1,C0=)
        #     if abs(summa - s0) / s0 < quality and ntime> MAXTIMEPOINTS : break
        #     i += 1

    print(data)
    # plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
    # plt.plot(T, C)
    # plt.grid(True)
    # plt.show()


main(f)
