import numpy as np


def f(x):
    """Уравнение для нахождения корня его f(x) = 0

    Args:
        x

    Returns:
        значение функции в точке
    """
    return x**2 + 2 * x - 3


def dyhotomy(a, b, quality=0.0004, max_steps=1000):
    root = 0
    step = 0
    if f(a) * f(b) > 0:
        return ('Error')

    # Критерий сходимости может быть любой, я выбрал именно относительную ошибку
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
        # Если плохая сходимость, но все же есть
        in_answer = '{0} :Bad'.format(root)
        return in_answer
    return root


def simple_iterrtion(root, quality=0.0004, max_steps=1000):
    """Вычисление корня методом простых итерраций. Очень плохой почти никогда не сходится, 
    а чтобы по-хорошему го использовать нужно знать вид самой функции и алгебраически ее преобразовать, что 
    неудобно 

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
        in_answer = '{0} :Bad'.format(root)
        return in_answer


inp = input('a,b ')
i = inp.split(',')
for n in range(len(i)):
    i[n] = float(i[n])

# answer = dyhotomy(float(i[0]), float(i[1]))
answer = simple_iterrtion(i[0])
print(answer)
