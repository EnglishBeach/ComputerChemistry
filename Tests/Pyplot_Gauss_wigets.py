import numpy as np

import pylab

# !!! Импортируем класс кнопки и слайдера
from matplotlib.widgets import Button, Slider


def gauss(sigma, mu, x):
    '''Отображаемая фукнция'''
    return (1.0 / (sigma * np.sqrt(2.0 * np.pi)) *
            np.exp(-((x - mu)**2) / (2 * sigma * sigma)))


def addPlot(graph_axes, sigma, mu):
    '''Добавить график к осям'''
    x = np.arange(-5.0, 5.0, 0.01)
    y = gauss(sigma, mu, x)
    graph_axes.plot(x, y)

    # Нужно для обновления графика
    pylab.draw()


if __name__ == '__main__':

    def onButtonAddClicked(event):
        '''Обработчик события для кнопки "Добавить"'''
        # !!! Будем использовать sigma и mu, установленные с помощью слайдеров
        global slider_sigma
        global slider_mu
        global graph_axes

        # !!! Используем атрибут val, чтобы получить значение слайдеров
        addPlot(graph_axes, slider_sigma.val, slider_mu.val)

    # Создадим окно с графиком
    fig, graph_axes = pylab.subplots()
    graph_axes.grid()

    # Оставим снизу от графика место для виджетов
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    # Создание кнопки
    axes_button_add = pylab.axes([0.7, 0.05, 0.25, 0.075])
    button_add = Button(axes_button_add, 'Добавить')
    button_add.on_clicked(onButtonAddClicked)

    # !!! Создание слайдера для задания sigma
    axes_slider_sigma = pylab.axes([0.05, 0.25, 0.85, 0.04])
    slider_sigma = Slider(axes_slider_sigma,
                          label='σ',
                          valmin=0.1,
                          valmax=1.0,
                          valinit=0.5,
                          valfmt='%1.2f')

    # !!! Создание слайдера для задания mu
    axes_slider_mu = pylab.axes([0.05, 0.17, 0.85, 0.04])
    slider_mu = Slider(axes_slider_mu,
                       label='μ',
                       valmin=-4.0,
                       valmax=4.0,
                       valinit=0.0,
                       valfmt='%1.2f')

    pylab.show()