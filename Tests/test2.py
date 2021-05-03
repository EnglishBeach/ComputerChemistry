# %
import math as mt
KB = 8.6165E-5
E = 0.175
VALUME_CHANGE_T = 60
C0 = 1
K = 1
# %
class Time_function:
    def __init__(self,T0, T1, c0) -> None:
        """Constructor"""
        self.T0 =T0
        self.T1 =T1
        self.c0 =c0

    def __call__(self,t):
        temp = lambda t: self.T0 + (self.T1 - self.T0) * (1 - mt.exp(-t / VALUME_CHANGE_T))
        k = lambda t: K*mt.exp(-E / (KB * temp(t)))
        c = lambda t: self.c0 * mt.exp(-k(t) * t)
        return c(t)

# %
f=Time_function(100,120,1)
# %
f(100)

# %
