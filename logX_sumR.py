#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 22:23:59 2020

@author: xanderSolis
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt

f = lambda x : 1/x
a = 1; b = 3; N=5;
n=4;
dt = (b-a)/N

x = np.linspace(a,b,N+1)
#print(x)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.figure(figsize=(15,5))

# figura 1
plt.subplot(1,3,1) # Contenedor del primer graf
plt.plot(X,Y,'b') # graf de la función
x_sup = x[:-1] # crea un arreglo con los ext izq de cada sub-interv
y_sup = y[:-1] # crea un arreglo con los supremos
plt.plot(x_sup,y_sup,'b.',markersize=10) # grafica los sup
plt.bar(x_sup,y_sup,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('Suma superior de Riemann, N = {}'.format(N))

# figura 2
plt.subplot(1,3,2) # Contenedor del segundo graf
plt.plot(X,Y,'b') # graf de la función
xi_mid = (x[:-1] + x[1:])/2  # crea un arreglo con los ptos med de cada sub-interv
y_mid = f(xi_mid) # crea un arrego con los f(xi)
plt.plot(xi_mid,y_mid, 'g.',markersize=10) # grafica los f(xi)
plt.bar(xi_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
plt.title('Sumas de Riemann punto medio, N = {}'.format(N))

# Figura 3
plt.subplot(1,3,3) # Contenedor del tercer graf
plt.plot(X,Y,'b') # graf de la función
x_inf = x[1:]  # crea un arreglo con los ext der de cada sub-interv
y_inf = y[1:] # crea un arreglo con los infimos
plt.plot(x_inf, y_inf, 'r.',markersize=10) # grafica los inf
plt.bar(x_inf,y_inf,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('Suma inferior de Riemann, N = {}'.format(N))
# muestra la fig
plt.show()

S_sup = sum(y_sup*dt)
S_Riemann = sum(y_mid*dt)
S_inf = sum(y_inf*dt)
error = abs(b-m.e)
Serror = abs(1-S_Riemann)

print("Función f(x) = 1/x, definida sobre el intervalo: [",a,",",b,"]\n")
print("Partición con N = ",N,", intervalos\n")
print("Suma superior de Riemann: ", S_sup)
print("Suma intermedia de Riemann: ", S_Riemann)
print("Suma inferior de Riemann: ", S_inf, "\n")
print("Error = |",b,"- e | = ",error, "\n")
print("El error en la suma de Riemann es:\n | 1 - S_R | = ",Serror)
