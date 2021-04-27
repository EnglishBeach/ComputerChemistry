from re import X
import sympy as sym
import sympy.matrices as mat
from sympy.plotting import plot3d

import pandas as pd

x, y = sym.symbols('x y')


def create_gauss(f):
    H = mat.zeros(2, 2)
    fx = f.diff(x)
    fy = f.diff(y)
    fxy = fx.diff(y)
    fyx = fy.diff(x)
    H[0, 0] = fx.diff(x)
    H[0, 1] = fxy
    H[1, 0] = fyx
    H[1, 1] = fy.diff(y)
    return H


def main():
    f = sym.sin(sym.sqrt(x**2 + y**2)) / x 
    quality = 0.1
    x0 = 1
    y0 = 1
    step = quality

    H = create_gauss(f)
    s = sym.lambdify([x, y], -H.det())

    P = mat.Matrix(1, 2, [x0, y0])

    i = 0

    while True:
        i += 1
        x1 = x0 + step * s(x0, y0)
        y1 = y0 + step * s(x0, y0)
        X1 = mat.Matrix(1, 2, [x1, y1])
        P = P.row_insert(99999, X1)

        if abs((x1 - x0)**2 + (y1 - y0)**2) > quality or i > 100: break
    sym.pprint(P)
    plot3d(f, (x, 0, 50), (y, 0, 50))


main()
