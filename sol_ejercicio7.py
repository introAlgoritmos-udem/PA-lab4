# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:48:11 2022

@author: aulas-tic
"""

# Inicializacion de variables
i = 1

# Ingreso de datos
n = int(input("Digite el numero: "))

# Generacion de la secuencia
mul3 = 3*i
print("Secuencia:")
while(mul3 <= n):
    print(mul3)
    i = i + 1
    mul3 = 3*i