#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:49:51 2020

@author: xander
"""
import numpy as np # importa la libreria numpy
import matplotlib.pyplot as plt # importa la libreria plt del módulo pyplot
###########################
## INSRUCCIONES ###########
###########################
# 1. PARA CAMBIAR EL TAMAÑO n O LOS EXTREMOS [a,b] DE LA PARTICIÓN
f = lambda x : 1/x # define la función 
a = 1; b = 4; N =4 # define los extremos de la partición y el rango 
n = 10 # Usa n*N+1 puntos para graficar la función suavemente

# datos para generar las gráficas
x = np.linspace(a,b,N+1) # datos X para el dominio de la función
y = f(x) # datos Y para la imagen

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.figure(figsize=(15,5)) # crea el contenedor de las 3 graficas ...FIGURA

plt.subplot(1,3,1) # crea la primera sub-graf(renglon, columna, indice)
plt.plot(X,Y,'b') # genera la gráfica con el conjunto X, y de datos
x_left = x[:-1] # Extremos izquierdos de cada sub-intervalo X
y_left = y[:-1] # Extremos izquierdos de cada sub-intervalo Y
plt.plot(x_left,y_left,'b.',markersize=10) # grafica los supremos con un marcador tamaño 10
plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')# crea grafico de barras 
plt.title('Suma Superior, N = {}'.format(N)) # pone titulo al gráfico

plt.subplot(1,3,2) # crea la segunda sub-graf(renglon, columna, indice)
plt.plot(X,Y,'b')# curva de la función
x_mid = (x[:-1] + x[1:])/2 # Puntos medios de cada sub-intervalo X
y_mid = f(x_mid) # evalula los puntos medios en la función
plt.plot(x_mid,y_mid,'b.',markersize=10)# grafica los puntos medios 
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')# grafico de barras
plt.title('Suma de Riemann, N = {}'.format(N))# titulo del gráfico

plt.subplot(1,3,3) # crea la tercera sub-graf(renglon, columna, indice)
plt.plot(X,Y,'b') # genera curva de la función con el conjunto de datos X, Y
x_right = x[1:] # Extremos derechos de cada sub-intervalo X
y_right = y[1:] # Extremos derechos de cada sub-intervalo X
plt.plot(x_right,y_right,'b.',markersize=10)# grafica los infimos de la función
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')# genera gráfico de barras
plt.title('Suma Inferior, N = {}'.format(N))# titulo

plt.show()# muestra la figura: FIGURA
#######################################
# Parámetros de la suma################
#######################################
dx = (b-a)/N # define la norma de la partición
x_left = np.linspace(a,b-dx,N) # arreglo con los extremos izquierdos
x_midpoint = np.linspace(dx/2,b - dx/2,N) # arreglo con los puntos medios
x_right = np.linspace(dx,b,N) # arreglo con los extremos derechos

print("Partición con",N,"sub-intervalos.") # imprime etiqueta
left_riemann_sum = np.sum(f(x_left) * dx) # genera la suma f(x_izq)*dx
print("Sumas Superiores:",left_riemann_sum) # imprime etiqueta

midpoint_riemann_sum = np.sum(f(x_midpoint) * dx) # genera la suma con los puntos medios
print("Sumas de Riemann:",midpoint_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx) # genera la suma con los ext der
print("Sumas Inferiores:",right_riemann_sum)
