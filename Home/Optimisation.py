import sympy as sym
import sympy.matrices as mat
from sympy.plotting import plot3d

(x,y,z)=sym.symbols('x:z')
h = sym.symbols('h')

# Сама функция:
# f = sym.sin(sym.sqrt(x**2 + y**2))
f = x**2 + y**2

# Условие для ограничения:
g = 4-x-y

# Начальные параметры:
X0, Y0 = 3.5, 3.5

# Технические параметры
MAXI = 500
STEP = 1

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
    H = [[f.diff(x).diff(y) for x in (x,y,z)] for y in (x,y,z)]
    H = mat.Matrix(H)
    return H


def optimise_FastDown(f):
    """Вычисляет min мметодом наискорейшего спуска

    Args:
        f (sympy.function): Функция
    """
    feval = sym.lambdify([x, y], f)
    # Начальная точка
    r0 = mat.Matrix((X0,Y0))

    # Создание градиента 
    g= mat.Matrix([f.diff(x) for x in (x,y)])

    p = mat.Matrix()

    i = 0
    r1 =mat.Matrix()
    while True:
        i += 1

        r1 = r0 - STEP * g.subs({x:})

        X1 = mat.Matrix(1, 2, [x1, y1])
        if (feval(x0,y0) - feval(x1,y1)) < STEP or i > MAXI: break

        p = p.row_insert(99999, r1.transpose())
        r0 = r1

    sym.pprint(P)
    print('Steps: %s'%i)
    plot3d(f, (x, XDIAP[0], XDIAP[1]), (y, YDIAP[0], YDIAP[1]))

# def optimise_Monte_karlo(f):

def optimase_if(f):
    F = f - h* g

optimise_FastDown(f)





# optimise_FastDown(f)
