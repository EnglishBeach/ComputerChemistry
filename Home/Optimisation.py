import sympy as sym
import sympy.matrices as mat
from sympy.plotting import plot3d

(x, y, z) = sym.symbols('x:z')
h = sym.symbols('h')

# Сама функция:
f = sym.sin(sym.sqrt(x**2 + y**2))
# f = x**2 + y**2

# Условие для ограничения:
glim = 4 - x - y

# Начальные параметры:
X0, Y0 = 3.5, 3.5

# Технические параметры
MAXI = 100
STEP = 0.1
QUALITY = 1E-3

# Диапазон вывода графика
XDIAP = [-10, 10]
YDIAP = [-10, 10]


def create_gauss(f):
    """Вычисляет матрицу Якоби для f 2 переменных

    Args:
        f (sympy.function): Функиця

    Returns:
        Якобиан
    """
    H = [[f.diff(x).diff(y) for x in (x, y, z)] for y in (x, y, z)]
    H = mat.Matrix(H)
    return H


def optimise_FastDown(f):
    """Вычисляет min мметодом наискорейшего спуска

    Args:
        f (sympy.function): Функция
    """

    feval = sym.lambdify([x, y], f)

    # Начальная точка
    r0 = mat.Matrix((X0, Y0))

    # Создание градиента
    g = mat.Matrix([f.diff(x) for x in (x, y)])

    points = mat.Matrix()

    i = 0
    r1 = mat.Matrix()
    points = r0.transpose()

    while True:
        i += 1

        r1 = r0 - STEP * g.subs({x: r0[0], y: r0[1]})
        #
        if abs(
            (feval(r1[0], r1[1]) - feval(r0[0], r0[1]))
            ) < QUALITY or i > MAXI:
            break

        points = points.row_insert(99999, r1.transpose())
        r0 = r1

    sym.pprint(points)
    print('Steps: %s' % i)
    plot3d(f, (x, XDIAP[0], XDIAP[1]), (y, YDIAP[0], YDIAP[1]))


# def optimise_Monte_karlo(f):


def optimase_if(f):
    F = f - h * glim


optimise_FastDown(f)

# optimise_FastDown(f)
