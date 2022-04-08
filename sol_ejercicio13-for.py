# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:27:16 2022

@author: aulas-tic
"""



ban = 0 

N = int(input("Digite la cantidad de numeros: "))
for k in range(N):
    num = 2*k
    if (ban == 0):
        print(num)
        ban = 1
    else:
        print(-num)
        ban = 0
    
    