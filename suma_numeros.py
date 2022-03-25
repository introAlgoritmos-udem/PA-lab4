# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:41:39 2022

@author: Usuario
"""

# Inicialización de variables
sum = 0
num = 1

# Entrada de datos
N = int(input("Digite el numero final: ")) 

# Calculo de la suma
while(num <= N):
    sum = sum + num
    num = num + 1
    
# Despliegue del resultado
print("La suma es: ", sum, sep="")

