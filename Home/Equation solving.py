import numpy as np
import random as rnd


def f(x):
    """Уравнение для нахождения корня его f(x) = 0
    """
    return x**2 + 2 * x - 3


def dyhotomy(a, b, quality=0.01, max_steps=1000):
    """Нахождение корня уравнения методом Дихотомии

    Args:
        a (float): Левая граница
        b (float): Првая граница
        quality (float, optional): Предел отклонения 2 значений близких к истинному корню. Defaults to 0.01.
        max_steps (int, optional): Максимальое число шагов. Defaults to 1000.
    Returns:
        Error: не сходится вообще
        Valume :Bad :сходится плохо
        Valume: значение если сходится хорошо
    """
    step = 0
    if f(a) * f(b) > 0:
        return ('Error')
    # Критерий сходимости может быть любой, я выбрал именно относительную ошибку
    while abs((b - a) / a) > quality and step < max_steps:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif (f(a) * f(mid)) < 0:
            b = mid
        else:
            a = mid
        step += 1
    if step == max_steps:
        bad_root = '{0} :Bad'.format(mid)
        return bad_root
    return mid


def simple_iteration(root, quality=0.0004, max_steps=1000):
    """Вычисление корня методом простых итерраций. Очень плохой почти никогда не сходится, 
    а чтобы по-хорошему го использовать нужно знать вид самой функции и алгебраически ее преобразовать, что 
    невозможно 

    Args:
        root ([type]): [description]
        quality (float, optional): [description]. Defaults to 0.0004.
        max_steps (int, optional): [description]. Defaults to 1000.
    """
    def fi(x):
        y = f(x) + x
        return y

    for step in range(max_steps):
        past_fi = fi(root)
        root = fi(root)
        if abs(past_fi - fi(root) / fi(root)) < quality:
            return root
        elif abs(past_fi - fi(root) / fi(root)) > 1000:
            return 'error'
    if step == max_steps:
        bad_root = '{0} :Bad'.format(root)
        return bad_root


def newton(x, quality=0.001, max_steps=20):
    """Решение уравнение методом Ньютона - Рафсона

    Args:
        x (float): Начальное приблежение корня
        quality (float, optional): Предел отклонения 2 значений близких к истинному корню. Defaults to 0.01.
        max_steps (int, optional): Максимальое число шагов. Defaults to 1000.
    Returns:
        Error: не сходится вообще
        Valume: значение если сходится хорошо
    """
    x1 = x * 2

    step = 0
    dx = quality
    while abs((x1 - x) / x) > quality and step < max_steps:
        x = x1
        # Вычисляем производную в х0 по среднему из коэффициентов секущих через х0 и хсправа, х0 и хслева. По теореме Лагранжа о конечных приращениях
        k = (f(x + dx) - f(x - dx)) / dx
        x1 = -f(x) / k + x
        step += 1
    if step == max_steps:
        return 'Error'
    return x1


def monte_kristo(a, b, quality=1, max_steps=100):
    """Решение уравнения методом Монте-Карло. 
    Args:
        a (float): Левая граница
        b (float): правая граница
        quality (int, optional): Максимальная ошибка |Y-y|, где Y- значение в корне уравнения, y - значение в приближеннном корне на выводе. 
        Defaults to 1.
        max_steps (int, optional): Максимаольное число шагов. Defaults to 100.
    Возвращает массив вида:
            x1(float) |Y-y1|(float)
            x2(float) |Y-y2|(float)
    """

    root = []

    for i in range(max_steps):
        xr = a + (b - a) * rnd.random()
        root.append([xr, abs(f(xr))])

    for i in range(max_steps):
        root = sorted(root, key=lambda x: x[1])
        root.reverse()
        x = a + (b - a) * rnd.random()
        fr = abs(f(x))
        # for n in range(len(answer)):
        #     if fr< answer[n][1]:
        #         answer[n][0]= x
        #         answer[n][1]=fr

        if fr < root[0][1]:
            root[0][0] = x
            root[0][1] = fr
        root = sorted(root, key=lambda x: x[1])

        while root[len(root) - 1][1] > quality and len(root) > 1:
            root.pop()
        root = sorted(root, key=lambda x: x[1])
        root.reverse()
        return root


def print2D(f):
    """
    Выводит на экран значения всего массива
    """

    for y in range(len(f)):
        output = ''
        for x in range(len(f[0])):
            if type(f[y][x]) == str:
                output += ' |{0: <14}|'.format(f[y][x])

            else:
                output += ' {0: >8.2f}'.format(f[y][x])
        print(output)

x0 = -9
x1 = 15
print('         Solving equation x**2 + 2 * x - 3 from %s to %s:    ' % (x0,x1))
print('    Dyhotomy:')
a = dyhotomy(x0, x1)
print(a)
print()

print('    Newton:')
b = newton(x0)
print(b)
print()

print('    Monte-Karlo: ')
print('{0: >8} {1: >8}'.format('x', 'y'))
c = monte_kristo(x0, x1, max_steps=1000,quality=0.2)
print2D(c)
print()




