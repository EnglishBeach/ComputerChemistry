import math as mt
import pandas as pnd
import matplotlib.pyplot as plt

Kb = 8.6165E-5
def fC (t):
    T = lambda t: T0 + (Tk-T0)*(1-exp(-t/q))
    k = lambda t: (-E/Kb-T(t))
    c= lambda t: c0*exo(-k*t)
    return c

# def simpa (a,b,n):
#     dx = (b-a)/n
#     x= lambda i: a+dx*i
#     summ = 0.0
#     for i in range( int((n/2)//1)):
#         s = f(x (2*i) )+4*f(x (2*i+1) )+ f( x(2*i) )
#         summ += s
#     return summ*dx/3.0

def kotes(f,llim, rlim, n=3):
    """Вычисляет интеграл методом Котеса

    Args:
        a (float): Левая граница
        b (float): Правая граница
        n (int, optional): Число Котеса.
    Returns:
        (float): Значение интеграла
    """
    dx = (rlim - llim) / n
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
        suma += A[i] * f(llim + dx * i)

    return n * dx * suma / N

def restrict_of_integral(f,left_gen_lim,right_gen_lim,points):
    dx = (right_gen_lim-left_gen_lim)/points
    def infunc (*args, **kwargs):
        i = 0
        s0=0
        s=0
        for i in range(points):
            s+=f(left_limit=left_gen_lim+dx*i,right_limit = left_gen_lim+dx*(i+1) , *args,**kwargs)
            i+=1       
        return [S,I]
    return infunc

# Входные данные
left_limit=0
right_limit=158
stop = 0
T0 = 300
Tk= 900
E = 1
q = 1
steps= 10
quality

dt = (right_limit-left_limit)/steps
j=1
    # out =  simpa (left_limit,right_limit,n)
    # n1 = n*2


while temp< max-temp:
    temp = T0
    out0=0
    C=[]
    T=[]
    i=0
    while True:
        i+=1
        out =  restrict_of_integral( kotes(fC,n=2), left_gen_lim=left_limit, right_gen_lim = right_limit, points=4*2**steps)
        if abs(out-out)/out<quality:
            break
        out0 = out
    C.append('{0: > 5.2} M' .format(out))
    T.append('{0: > 5.2} K' .format(temp))




f = pd.DataFrame({'Concentrations': C, 'Temperatures': T})
plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(X, Y)
plt.grid(True)
plt.show()

print(f)
