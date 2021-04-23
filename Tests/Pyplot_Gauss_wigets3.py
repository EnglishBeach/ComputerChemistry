# -*- coding: utf-8 -*-

import time

import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy


def gaussian(x, delay, sigma):
    '''
    Функция, график которой будет отображаться процессе анимации
    '''
    return numpy.exp(-((x - delay) / sigma) ** 2)


if __name__ == '__main__':
    # Параметры отображаемой функции
    maxSize = 200
    sigma = 10.0

    # Диапазон точек для расчета графика функции
    x = numpy.arange(maxSize)

    # Значения графика функции
    y = numpy.zeros(maxSize)

    # Создание окна для графика
    fig, ax = plt.subplots()

    # Установка отображаемых интервалов по осям
    ax.set_xlim(0, maxSize)
    ax.set_ylim(-1.1, 1.1)

    # !!! Создание списка линий, которые будут последовательно
    # переключаться при изменении номера кадра
    frames = []
    for delay in numpy.arange(-50.0, 200.0, 1.0):
        y = gaussian(x, delay, sigma)
        line, = ax.plot(x, y, '-b')

        # !!! Поскольку на каждом кадре может меняться несколько объектов,
        # каждый элемент списка - это список изменяемых объектов
        frames.append([line])

    # Задержка между кадрами в мс
    interval = 30

    # Использовать ли буферизацию для устранения мерцания
    blit = True

    # Будет ли анимация циклической
    repeat = False

    # !!! Создание анимации
    animation = ArtistAnimation(
            fig,
            frames,
            interval=interval,
            blit=blit,
            repeat=repeat)

    plt.show()