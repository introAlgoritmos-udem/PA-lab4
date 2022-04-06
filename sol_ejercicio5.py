# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:55:35 2022

@author: aulas-tic
"""


# Inicializacion de variables
i = 0

# Ingreso de datos
M = int(input("Digite el mayor: "))
N = int(input("Digite el menor: "))

opc = input("Elija si va ver pares (p) o impares (i): ")

# Verificar e intercambiar
if(M < N):
    aux = M
    M = N
    N = aux
    print("Se intercambian los numeros")

# Se imprime la secuencia    
i = N
print("Salida:")
while(i <= M):
    
    if(opc == 'i'):
        if (i%2 != 0):
            print(i)                 
    else:
        if (i%2 == 0):
            print(i)  
     
    i = i + 1