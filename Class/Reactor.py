import random as rnd
import math as m
import pandas as pd

XMIN = 1
XMAX = 10
YMIN = 0
YMAX = 10
K = 1

# Задание вероятнойстей ядерной реакции
#   [0;rlim1] - ничего не происходит
#   (rlim1;rlim2] - поглощение нейтрона, пропадание частицы
#   (rlim2,1] - деление ядра и появление 2 новых нейронов
RLIM1 = 0.3
RLIM2 = 0.7


def creating_reactor(nnumber: int):
    A = pd.DataFrame({'X0': [], 'Y0': [], 'X1': [], 'Y1': []})
    for i in range(nnumber):
        x = XMIN + (XMAX - XMIN) * rnd.random()
        y = YMIN + (YMAX - YMIN) * rnd.random()
        A = A.append({'X0': x, 'Y0': y, 'X1': 0, 'Y1': 0}, ignore_index=True)
    return A


def insert_row(row_number, df, row_value):
    copy_df = df.copy()

    start_upper = 0
    end_upper = row_number
    start_lower = row_number
    end_lower = df.shape[0]
    upper_half = [*range(start_upper, end_upper, 1)]

    lower_half = [*range(start_lower, end_lower, 1)]
    lower_half = [x.__add__(1) for x in lower_half]
    index_ = upper_half + lower_half

    copy_df.index = index_
    copy_df.loc[row_number] = row_value
    copy_df = copy_df.sort_index()
    return copy_df


# def active_kernel(n):
#     r = RlIM1 + (RLIM2 - RlIM1) * (1 + K * (n - nv) / nv)
#     return r


def main():
    """Основной код программы
    """

    # l = lambda h, r: -h * m.log(1 - r)
    l = 1
    nt = 0
    # Создание реактора
    Reactor = creating_reactor(nnumber=20)

    # Запуск деления
    tick = 0
    total_n = pd.Series()
    while tick <= 3 & True:  #Количество тиков, каждый тик - 1 дейтсвие всех нейтронов

       for nt in Reactor.index:  #Перебор всех нейтронов
            x0 = Reactor.loc[nt].X0
            y0 = Reactor.loc[nt].Y0

            # Случайное направление движения
            fi = 0 + 2 * m.pi() * rnd.random()
            x1 = x0 + l * m.cos(fi)
            y1 = y0 + l * m.sin(fi)
            Reactor.loc[nt].X1 = x1
            Reactor.loc[nt].Y1 = y1

            # Выбираем случайный исход взаимодействия
            result = rnd.random()

            if x1 > XMAX or x1 < XMIN or y1 < YMIN or y1 > YMAX:
                Reactor = Reactor.drop(index=nt)

            elif result <= RLIM1:
                Reactor.loc[nt].X0 = x1
                Reactor.loc[nt].Y0 = y1

            elif RLIM1 < result <= RLIM2:
                Reactor = Reactor.drop(index=nt)

            elif RLIM2 < result:
                Reactor.loc[nt].X0 = x1
                Reactor.loc[nt].Y0 = y1
                Reactor = insert_row(nt + 1, Reactor, [x1, y1, x1, y1])

        Reactor = Reactor.reset_index()
        total_n = total_n.append(pd.Series(nt), ignore_index=True)
        tick += 1
    print(total_n)


main()