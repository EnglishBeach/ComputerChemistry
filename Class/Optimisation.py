import sympy as sym
import sympy.matrices as mat
from sympy.plotting import plot3d

x, y = sym.symbols('x y')
# f = sym.sin(sym.sqrt(x**2 + y**2))
f = x**2 + y**2
feval = sym.lambdify([x, y], f)

X0, Y0 = 3.5, 3.5

MAXI = 500
STEP = 1

XDIAP = [-10, 10]
YDIAP = [-10, 10]


def create_gauss(f):
    H = mat.zeros(2, 2)
    fx = f.diff(x)
    fy = f.diff(y)
    H[0, 0] = fx.diff(x)
    H[0, 1] = fx.diff(y)
    H[1, 0] = fy.diff(x)
    H[1, 1] = fy.diff(y)
    return H


def main(f):
    x0 = X0
    y0 = Y0

    H = create_gauss(f)
    s = sym.lambdify([x, y], -H.det())

    P = mat.Matrix(1, 2, [x0, y0])

    i = 0

    while True:
        i += 1
        x1 = x0 + STEP * s(x0, y0)
        y1 = y0 + STEP * s(x1, y0)
        X1 = mat.Matrix(1, 2, [x1, y1])
        if (feval(x0,y0) - feval(x1,y1)) < STEP or i > MAXI: break
        P = P.row_insert(99999, X1)
        x0,y0=x1,y1

    sym.pprint(P)
    print('Steps: %s'%i)
    plot3d(f, (x, XDIAP[0], XDIAP[1]), (y, YDIAP[0], YDIAP[1]))


main(f)
