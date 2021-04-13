import random as rnd


def monte_krist_graph(f, a, b, maxf, max_steps=10000):
    """Вычисляет интеграл методом Монте-Карло. Графический алгорим: основан на вероятности попадания случайного чила в область под графиком

    Args:
        a (float): Левая граница
        b (float): Правая граница
        maxf (float): верхняя граница
        max_steps (int, optional): Максимальное число шагов. Defaults to 10000.
    Returns:
        (float): Значение интеграла
    """
    area = maxf * (b - a)
    nsucces = 0
    for i in range(max_steps):
        xr = a + (b - a) * rnd.random()
        yr = maxf * rnd.random()
        if f(xr) > yr: nsucces += 1
    return area * nsucces / max_steps


def monte_krist_analytical(f,a, b, max_steps=10):
    """Вычисляет интеграл методом Монте-Карло. Аналитический алгорим: основан на свойстве определенного интеграла
        I = (b-a)f(e),
        е - некоторое число на промежутке [a;b], f(e) - среднее значение f(x)

    Args:
        a (float): Левая граница
        b (float): Правая граница
        max_steps (int, optional): Максимальное число шагов. Defaults to 10000.
    Returns:
        (float): Значение интеграла
    """
    s = 0
    for i in range(max_steps):
        xr = a + (b - a) * rnd.random()
        s += f(xr)
    return s / max_steps * (b - a)


def trap(f,a, b, max_steps=10000):
    """Вычисляет интеграл методом трапеций

    Args:
        a (float): Левая граница
        b (float): Правая граница
        max_steps (int, optional): Максимальное число шагов. Defaults to 10000.
    Returns:
        (float): Значение интеграла
    """
    dx = (b - a) / max_steps
    s = 0
    for i in range(max_steps):
        s += (f(a + dx * i) + f(a + dx * (i + 1)))
    return s / 2 * dx


def kotes(f,a, b, n=3):
    """Вычисляет интеграл методом Котеса

    Args:
        a (float): Левая граница
        b (float): Правая граница
        n (int, optional): Число Котеса.
    Returns:
        (float): Значение интеграла
    """
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

if __name__ == '__main__':
    f = lambda x: x ** 2
    x0 = -9
    x1 = 15
    print('         Integrals %s to %s:    ' % (x0,x1))
    print('    Monte-Karlo, analytical:')
    a = monte_krist_analytical(x0, x1, max_steps=10000)
    print(a)
    print()

    print('    Monte-Karlo, graphical:')
    b = monte_krist_graph(x0, x1, 100)
    print(b)
    print()

    print('    Trapezoids: ')
    c = trap(x0, x1)
    print(c)
    print()

    print('    Kotes: ')
    d = kotes(x0, x1)
    print(d)
    print()
    print()
