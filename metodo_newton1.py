import math
import numpy as np


def f(x):
    y = np.zeros(3)
    y[0] = 3*x[0] - math.cos(x[1]*x[2]) - (1/2)
    y[1] = ((x[0])**2) - 81*(x[1] + 0.1)**2 + math.sin(x[2]) + 1.06
    y[2] = math.e**(-x[0]*x[1]) + 20*x[2] + ((10*math.pi - 3)/3)
    return y

def jf(x):
    j = np.zeros((3, 3))

    j[0, 0] = 3
    j[0, 1] = x[2]*math.sin(x[1]*x[2])
    j[0, 2] = x[1] * math.sin(x[1] * x[2])

    j[1, 0] = 2*x[0]
    j[1, 1] = -162*x[1] - 16.2
    j[1, 2] = math.cos(x[2])

    j[2, 0] = -x[1]*(math.e**(-x[0] * x[1]))
    j[2, 1] = -x[0] * (math.e ** (-x[0] * x[1]))
    j[2, 2] = 20

    return j



