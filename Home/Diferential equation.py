import matplotlib.pyplot as plt
import pandas as pd
import math as mt

X0 = 0
Y0 = 0
STEPS = 10
DX = 0.2

def eiler(f, x, y, steps, dx=0.1):
    """ Решает методом Эйлера уравнения типа:
    dy/dx = F(x,y)

    Args:
        F (function): Функиця от ч х, у.
        x0,y0 (int): Начальные значения х,у.
        steps (int): Количество шагов.
        dx (int, optional): Шаг х.

    """
    Xlist = [x]
    Ylist = [y]

    for i in range(steps):
        y = y + dx * f(x, y)
        x += dx
        Xlist.append(x)
        Ylist.append(y)

        # print('X: {0: >5.2f} Y: {1: >5.2f}'.format(x, y))
    return [Xlist, Ylist]

def runge(f, x, y, steps, dx=0.1,type = 1):

    # k1= dx*f(x,y)
    # k2= dx*f(x+dx/2,y+k1/2)
    # k3 = dx*f(x+dx,y+2*k2 - k1)
    # k4= dx*f(x+dx,y+k3)

    Xlist = [x]
    Ylist = [y]
    
    if type == 1:
        return eiler(f,x,y, steps, dx)
        
    elif type == 2:
        for i in range(steps):
            y1 = y+dx*f(x,y)/2
            y = y+dx*f(x+dx/2,y1) 
            x+=dx

            Xlist.append(x)
            Ylist.append(y)    
        return [Xlist,Ylist]
      
    elif type == 3:
        for i in range(steps):
            k1= dx*f(x,y)
            k2= dx*f(x+dx/2,y+k1/2)
            k3 = dx*f(x+dx,y+2*k2 - k1)
            y =y+ dx*(k1+4*k2+k3)
            x+=dx

            Xlist.append(x)
            Ylist.append(y)    
        return [Xlist,Ylist]
        
    elif type == 4:
        for i in range(steps):
            k1= dx*f(x,y)
            k2= dx*f(x+dx/2,y+k1/2)
            k3 = dx*f(x+dx,y+k2/2)
            k4= dx*f(x+dx,y+k3)

            y =y+ dx*(k1+2*k2+2*k3+k4)/6
            x+=dx

            Xlist.append(x)
            Ylist.append(y)    
        return [Xlist,Ylist]        
        
def main_one_equation():
    f=  lambda x,y:  x
    # Решение уравнения dy/dx = F(x,y)

    answer = runge(f, x=X0, y=Y0, steps=STEPS, dx=-DX)
    X = answer[0]
    Y = answer[1]
    X.reverse()
    Y.reverse()

    answer = runge(f, x=X0, y=Y0, steps=STEPS, dx=DX)
    X.extend(answer[0])
    Y.extend(answer[1])

    data = pd.DataFrame({'X': X, 'Y': Y})
    plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(X, Y)
    plt.grid(True)
    plt.show()

def main_system_equation(f):
    def numf(s):
        numf = lambda x: x**s
        return numf
    number_eq = 3
    systemf = [ numf(i) for i in range(number_eq)]

    for i in range(number_eq):
        y0 = eiler(systemf[i], x=X0, y=Y0, steps=STEPS, dx=DX)
        



main_one_equation()