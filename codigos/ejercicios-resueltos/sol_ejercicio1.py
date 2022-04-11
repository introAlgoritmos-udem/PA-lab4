# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:24:27 2022

@author: aulas-tic
"""

# Inicializacion de variables
i = 0

# Ingreso de datos
N = int(input("Digite el numero: "))
if (N < 0):
    N = N*(-1)

# Muestro la secuencia
print("Secuencia:")
while(i <= N):
    print(i)
    i = i + 1
