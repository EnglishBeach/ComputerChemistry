import numpy as np
import random as rnd


def f(x):
    """
    Уравнение для нахождения корня его f(x) = 0
    """
    return x**2 + 2 * x - 3


def dyhotomy(a, b, quality=0.01, max_steps=1000):
    """
    Нахождение корня уравнения методом Дихотомии

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


def simple_iterrtion(root, quality=0.0004, max_steps=1000):
    """
    Вычисление корня методом простых итерраций. Очень плохой почти никогда не сходится, 
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
    """
    Решение уравнение методом Ньютона - Рафсона

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


def monte_kristo(a, b, quality=0.001, max_steps=100):

    row_answer = []

    for i in range(max_steps):
        x = a + (b - a) * rnd.random()
        row_answer.append([x, abs(f(x))])
    answer =sorted(row_answer,key=lambda x: x[1])
    answer.reverse()

    for i in range(max_steps):
        x = a + (b - a) * rnd.random()
        fr = abs(f(x))
        # for n in range(len(answer)):
        #     if fr< answer[n][1]:
        #         answer[n][0]= x
        #         answer[n][1]=fr

        n=0
        while fr<answer[n][1]:
            answer[n][0]= x
            answer[n][1]=fr





