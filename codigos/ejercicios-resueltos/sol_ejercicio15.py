# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:57:19 2022

@author: b12s306e30
"""

# Inicializacion da variables
f = 1
expo = 3
num1 = 1
num2 = 2

# Entrada de datos
x = float(input("x = "))
N = int(input("Digite la candidad terminos: "))


for i in range(1,N):
    #ter = x**expo
    signo = (-1)**i
    # print("signo = ",signo)
    term = (signo*x**expo)/(num1*num2)
    # print("term = ",term)
    expo = expo + 2
    num1 = num1 + 2
    num2 = num2 + 2
    # print("--------------")
    f = f + term
    
print("f = ", f, sep="")
    
    
    
    
    
    
