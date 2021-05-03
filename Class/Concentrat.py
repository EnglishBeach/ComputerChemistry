# %%
import math as mt
import pandas as pd
import matplotlib.pyplot as plt

# Константы
KB = 8.6165E-5
E = 0.175
SPEED_CHANGE_T = 60
C0 = 1
K = 1

# Входные данные
T0 = 300
T1 = 450

QUALITY = 0.01

TIME0 = 0
TIME1 = 600
TIME_N = 10
MAXTIMEPOINTS = 32

# %%
class Time_function:
    """Функция от 1 переменной с параметрами
    """
    def __init__(self, T0, T1,k0) -> None:
        """Constructor"""
        self.T0 = T0
        self.T1 = T1
        self.k0=k0

    def __call__(self, t):
        temp = lambda t: self.T0 + (self.T1 - self.T0) * (1 - mt.exp(
            -t / SPEED_CHANGE_T))
        k = lambda t: self.k0 * mt.exp(-E / (KB * temp(t)))
        return k(t)

# %%
def kotes(f, a, b, n=3):
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
    for i in range(4):
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
    for i in range(4):
        # Изменить вызов функции в случае другой функции!!!
        suma += A[i] * f(a + dx * i)
    return n * dx * suma / N


def kotes_quality(f, a, b, quality=0.1, n=3):
    s0 = kotes(f, a=a, b=b, n=n)
    i = 0
    while True:
        x_n = 4 * 2**i
        dx = (b - a) / x_n
        s = 0
        for nx in range(x_n):
            s += kotes(f, a=a + dx * nx, b=a + dx * (nx + 1), n=n)
        if abs((s - s0) / s0) < quality or x_n > MAXTIMEPOINTS: return s
        i += 1

# %%
def main():
    func_k = Time_function(T0, T1,K)
    data = pd.DataFrame({'Time:': [TIME0], 'Concentration:': [C0]})

    # Перебор времени
    dtime = (TIME1 - TIME0) / TIME_N
    for ntime in range(TIME_N):
        a_time = TIME0 + dtime * ntime
        b_time = TIME0 + dtime * (ntime + 1)
        summ_k = kotes_quality(func_k, a=a_time, b=b_time, quality=QUALITY, n=2)
        # func_k.k0=k
        data = data.append(
            {
                'Concentration:': C0 * mt.exp(-summ_k),
                'Time:': b_time
            },
            ignore_index=True)

    print(data)
    # plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
    # plt.plot(T, C)
    # plt.grid(True)
    # plt.show()

# %%
main()
