# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:32:07 2022

@author: b12s306e30
"""

# Inicializacion da variables
fac = 1

n = int(input("Digite el numero: "))

for i in range(1,n + 1):
    fac = fac*i
    
print(n,"! = ",fac,sep = "")