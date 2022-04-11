 # -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:32:07 2022

@author: b12s306e30
"""


# Inicializacion de variables
term1 = 0
term2 = 1

# Ingreso de datos
N = int(input("Digite numero de terminos de la seria Fibonacci que desea ver: "))

# Despliegue de la serie Fibonacci
if N <= 0:
    print("No se imprime ningun termino de la serie")
elif N == 1:
    print(term1)
elif N == 2:
    print(term1)
    print(term2)
else:
    print(term1)
    print(term2)
    for i in range(3,N + 1):
        term3 = term2 + term1
        print(term3)
        term1 = term2
        term2 = term3