# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:08:35 2022

@author: aulas-tic
"""
"""
Realizar un algoritmo que muestre los primeros 
N términos de la siguiente serie: 0, - 2, 4, -6, 8, -10, 12, ...
"""

k = 0
ban = 0 


N = int(input("Digite la cantidad de numeros: "))
while(k < N):
    num = 2*k
    if (ban == 0):
        print(num)
        ban = 1
    else:
        print(-num)
        ban = 0
    
    k = k + 1