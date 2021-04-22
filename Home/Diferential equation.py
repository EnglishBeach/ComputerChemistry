import matplotlib.pyplot as plt
import pandas as pd

def f(x, y):
    return x


def eiler(f, x0, y0, steps, dx=0.1):
    """ Решает методом Эйлера уравнения типа:
    dy/dx = f(x,y)
    
    Args:
        f(function): Функиця от ч х, у.
        x0,y0 (int): Начальные значения х,у.
        steps (int): Количество шагов.
        dx (int, optional): Шаг х.
 
    """
    X = [x0]
    Y = [y0]
    x = x0
    y = y0

    for i in range(steps):
        ynext = y + dx * f(x, y)
        x += dx
        Y.append(ynext)
        X.append(x)
        y = ynext

        # print('X: {0: >5.2f} Y: {1: >5.2f}'.format(x, y))
    return [X, Y]

def runge(f, x0, y0, steps, dx=0.1,type = 1):
    def k1(f,x,y,dx):
        return dx*f(x,y)

    def k2(f,x,y,dx):
        return dx*f(x+dx/2,y+k1(f,x,y,dx)/2)

    def k3(f,x,y,dx):
        return dx*f(x+dx,y+2*k2(f,x,y,dx) - k1(f,x,y,dx))

    def k4(f,x,y,dx):
        return dx*f(x+dx,)

    if type == 1:
        return eiler(f, x0, y0, steps, dx=0.1)
    elif type == 2:
        A[0] = 1/2*f
    elif type == 3:

    ynext = y + dx * AF(x, y)
    x += dx
    Y.append(ynext)
    X.append(x)
    y = ynext



# Решение уравнения dy/dx = f(x,y)
x0 = 0
y0 = 1
answer = eiler(f, x0=x0, y0=y0, steps=10, dx=-1)
X = answer[0]
Y = answer[1]
X.reverse()
Y.reverse()

answer = eiler(f, x0=x0, y0=y0, steps=10, dx=1)
X.extend(answer[0])
Y.extend(answer[1])

f = pd.DataFrame({'X': X, 'Y': Y})
plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(X, Y)
plt.grid(True)
plt.show()

print(f)
