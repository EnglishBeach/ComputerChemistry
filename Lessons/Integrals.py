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
    return x**2 + 2 * x - 3


def monte_krist_graph (a, b,maxf, quality=1, max_steps=100):
    area = maxf*(b-a)
    for i in range(max_steps):
        xr = a+(b-a)*rnd.random()
        yr = maxf * rnd.random()
        f 

