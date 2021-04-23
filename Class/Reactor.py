import pandas as pd
# from sympy import *
import random as rnd
from math import *

xmin = 0
xmax = 10
ymin = 0
ymax =10

def active_kernel(n,k):
    r = (rlim2-rlim1)*(1+k*(n-nv)/nv)
    return r

l = lambda h,r: -h*log(1-r)
# Задание вероятнойстей ядерной реакции
#   [0;rlim1] - ничего не происходит
#   (rlim1;rlim2] - поглощение нейтрона, пропадание частицы
#   (rlim2,1] - деление ярда и появление 2 новых нейронов
rlim1 = 0.3
rlim2 =0.7
i = 0

while i <=1000 & True:

    # Случайная позиция и движение
    x0 =xmin + (xmax-xmin)*rnd.random()
    y0 = ymin + (ymax-ymin)*rnd.random()
    fi = 0+2*pi*rnd.random()

    x1 = x0 + l*cos(fi)
    y1 = y0 + l*sin(fi)

    r = rnd.random()

    if x1>xmax or x1<xnim or y1<ymin or y1>ymax: pass
    elif r< :

    elif :
