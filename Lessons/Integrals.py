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


def monte_krist_analyse(a, b, max_steps=10):
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
    return s / max_steps * (b - a)


def trap(a, b, max_steps=10000):
    dx = (b - a) / max_steps
    s = 0
    for i in range(max_steps):
        s += (f(a + dx * i) + f(a + dx * (i + 1)))
    return s / 2 * dx


def kotes(a, b, n=3):
    dx = (b - a) / n
    s = 0
    A = []
    for i in range(8):
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
    for i in range(8):
        suma += A[i] * f(a + dx * i)

    return n * dx * suma / N


a = monte_krist_analyse(0, 2, max_steps=10000)
b = monte_krist_graph(0, 2, 10)
c = trap(0, 2)
d = kotes(0,2)
print(a, b, c, d)
