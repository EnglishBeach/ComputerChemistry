import random as rnd
import math as m
import pandas as pd
import matplotlib.pyplot as plt

# Начальные параметры
XMIN = 1
XMAX = 10
YMIN = 0
YMAX = 10
# Лямбда
H = 1

# Задание вероятнойстей ядерной реакции
#   [0;rlim1] - ничего не происходит
#   (rlim1;rlim2] - поглощение нейтрона, пропадание частицы
#   (rlim2,1] - деление ядра и появление 2 новых нейронов
RLIM1 = 0.3
RLIM2 = 0.7

#N - начальное число частиц
N = 20
TIME = 600

#Контроль стержней
NTARGET = 10
K = 1

def creating_reactor(nnumber: int = 5):
    A = pd.DataFrame({'X': [], 'Y': []})
    for i in range(nnumber):
        x = XMIN + (XMAX - XMIN) * rnd.random()
        y = YMIN + (YMAX - YMIN) * rnd.random()
        A = A.append({'X': x, 'Y': y}, ignore_index=True)
    return A


def main():
    """Основной код программы
    """
    # Базовые функции контроля
    l = lambda h, r: -h * m.log(1 - r)
    control = lambda n: (RLIM2- RLIM1)*(1+K*(n-NTARGET)/NTARGET)

    control_RLIM2 = RLIM2
    # Создание реактора
    Reactor = creating_reactor(N)

    # Запуск деления
    tick = 0
    Rlen = N
    total_n = [Rlen]

    #Количество тиков, каждый тик - 1 дейтсвие всех нейтронов
    while tick < TIME and Rlen != 0 and len(
            Reactor.index) < 1000:

        # Перебор с конца
        nt = Rlen - 1

        # Проверка на включение и выключение системы контроля
        if Rlen< NTARGET: control_RLIM2 = control(Rlen)
        elif Rlen> NTARGET*2:control_RLIM2 = RLIM2

        #Перебор всех нейтронов
        while nt >= 0:

            x0 = Reactor.loc[nt].X
            y0 = Reactor.loc[nt].Y

            # Случайное направление движения
            fi = 0 + 2 * m.pi * rnd.random()
            r = rnd.random()
            x1 = x0 + l(H, r) * m.cos(fi)
            y1 = y0 + l(H, r) * m.sin(fi)

            # Выбираем случайный исход взаимодействия
            result = rnd.random()

            if x1 > XMAX or x1 < XMIN or y1 < YMIN or y1 > YMAX:
                Reactor = Reactor.drop(index=nt)

            elif result <= RLIM1:
                Reactor.loc[nt].X = x1
                Reactor.loc[nt].Y = y1

            elif RLIM1 < result <= control_RLIM2:
                Reactor = Reactor.drop(index=nt)

            elif control_RLIM2 < result:
                Reactor.loc[nt].X = x1
                Reactor.loc[nt].Y = y1
                Reactor = Reactor.append({'X': x1, 'Y': y1}, ignore_index=True)
                nt -= 1
            nt -= 1

        Rlen = len(Reactor.index)
        Reactor.reset_index(drop=True, inplace=True)
        total_n.append(Rlen)
        tick += 1

    plt.figure(figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(total_n, label="$f(x)$")
    plt.show()


main()