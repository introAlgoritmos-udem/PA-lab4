# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:53:04 2022

@author: aulas-tic
"""

# Inicializacion de variables
i = 0

# Ingreso de datos

M = int(input("Digite el mayor: "))
N = int(input("Digite el menor: "))

if(M < N):
    print("Metiste los numeros al reves")
else:
    i = N
    print("Salida:")
    while(i <= M):
        if (i%2 == 0):
            print(i)        
        i = i + 1

    