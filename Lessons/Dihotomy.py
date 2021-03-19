import numpy as np


def f(x):
    """Уравнение для нахождения корня его f(x) = 0

    Args:
        x

    Returns:
        значение функции в точке
    """
    return (x + 5)**3


def dyhotomy(a, b, quality=0.0004, max_steps=1000):
    root = 0
    step = 0
    if f(a) * f(b) > 0:
        return ('Error')
    while abs(f(b) - f(a) / f(a)) > quality and step < max_steps:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif (f(a) * f(mid)) < 0:
            b = mid
        else:
            a = mid
        step += 1
    root = (a + b) / 2
    if step == max_steps:
        return ('{0} Bad'.format(root))
    return root


inp = input('a,b ')
i = inp.split(',')
answer = dyhotomy(float(i[0]), float(i[1]))
print(answer)
