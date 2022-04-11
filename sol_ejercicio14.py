# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:32:07 2022

@author: b12s306e30
"""

# Inicializacion da variables
j = 0
signo = -1 
# Entrada de datos
N = int(input("Digite el numero de terminos: "))

for i in range(N):
    num = 2*i
    # Condicional para controlar el signo
    if(j <= signo - 1):
        j = j + 1
        print(num)
    else:
        signo = signo + 1
        j = 0
        print(-num)
        
    
    
    
    
