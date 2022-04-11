# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:57:19 2022

@author: b12s306e30
"""

# Inicializacion da variables
f = 0

# Entrada de datos
x = float(input("x = "))
N = int(input("Digite la candidad terminos: "))

for i in range(N):    
    # Calculo del factorial
    fac = 1
    for j in range(1,i + 1):
        fac = fac*j
    # Calculo del termino
    term = x**i/fac
    f = f + term

print("expo(",x,") = ",f, sep="")
   
    

    
    
    
    
    
    
