#Metodo de newton para sistemas não lineares
#By Goto
from __future__ import division
import math
import numpy as np


def f(x):
    y = np.zeros(3)
    y[0] = 3*x[0] - math.cos(x[1]*x[2]) - (1/2)
    y[1] = ((x[0])**2) - 81*(x[1] + 0.1)**2 + math.sin(x[2]) + 1.06
    y[2] = math.e**(-x[0]*x[1]) + 20*x[2] + ((10*math.pi - 3)/3)
    return y


def jf(x, h):
    J = np.zeros((3, 3))
    for j in range(3):
        for k in range(3):
            J[j][k] = (f(x + h * np.eye(3)[:, j])[k] - f(x)[k]) / h

    return J

x_old = 0 #vai aguarda o antigo valor da raiz
x = np.array([0.1, 0.1, -0.1]) #começo do chute e o valor a ser testado

h = 10**(-7)
k = 0 #contador de iteracoes
max_int  = 50 #numero maximo de interacoes
E1 = 10**(-9) #erro
while k < 50:
    k += 1
    delta = np.dot(np.linalg.inv(jf(x, h)), f(x))
    x_old = x
    x = x - delta
    if math.fabs(np.linalg.norm(x_old) - np.linalg.norm(x)) <= E1:
        print("Método de Newton Discreto por diferenças finitas para Sistema não lineares")
        print(x)
        print("numero de iterações: ", k)
        break
