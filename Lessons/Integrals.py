import random as rnd


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


def f(x):
    """Уравнение для нахождения корня его f(x) = 0
    """
    return x**2


def monte_krist_graph(a, b, maxf, max_steps=10000):
    """Вычисляет интеграл методом Монте-Карло. Графический алгорим: основан на вероятности попадания случайного чила в область под графиком

    Args:
        a (float): Левая граница
        b (float): Правая граница
        maxf (float): верхняя граница
        max_steps (int, optional): Максимальное число шагов. Defaults to 10000.

    Returns:
        float: Значение интеграла
    """
    area = maxf * (b - a)
    nsucces = 0
    for i in range(max_steps):
        xr = a + (b - a) * rnd.random()
        yr = maxf * rnd.random()
        if f(xr) > yr: nsucces += 1
    return area * nsucces / max_steps


def monte_krist_analyse(a, b, max_steps=10000):
    """Вычисляет интеграл методом Монте-Карло. Аналитический алгорим: основан на свойстве определенного интеграла 
    (I = (b-a)f(e), е- некоторое число на промежутке)

    Args:
        a (float): Левая граница
        b (float): Правая граница
        max_steps (int, optional): Максимальное число шагов. Defaults to 10000.

    Returns:
        float: Значение интеграла
    """
    s = 0
    for i in range(max_steps):
        xr = a + (b - a) * rnd.random()
        s += f(xr)
    return s / max_steps*(b-a)

def trap (a, b, quality=1, max_steps=10000)



a = monte_krist_analyse(0, 2)
b = monte_krist_graph(0, 2, 10)
print(a,b)

