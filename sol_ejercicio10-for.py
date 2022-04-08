# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:29:01 2022

@author: aulas-tic
"""

"""
Dados N valores, diseñe un algoritmo que haga el siguiente proceso:
- Si el valor es menor que cero, calcular su cubo.
- Si el valor esta entre 0 y 100, calcular su cuadrado.
- Si el valor esta entre 101 y 1000 calcular su raíz cuadrada.
"""

N = int(input("Digite la cantidad de numeros: "))
for i in range(N):
    num = int(input("Digite el numero: "))
    if(num < 0):
        print("-> Rta: ", num**3)
    elif (num <= 100):
        print("-> Rta: ", num**2)
    elif (num <= 1000):
        print("-> Rta: ", num**(1/2))
    else:
        print("-> Rta: Numero fuera de rango")
        
print("Gracias por usar nuestros servicios")