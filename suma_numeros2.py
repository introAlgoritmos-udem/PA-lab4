# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:08:31 2022

@author: Usuario
"""

# Inicializacion de variables
i = 0
cntNeg = 0
cntPos = 0
sumNeg = 0
sumPos = 0

# Entrada de datos
N = int(input("Indique la cantidad de numeros positivos a leer: "))

# Entrada de cada uno de los numeros
while(i < N):
    num = int(input("Digite el numero: "))
    i = i + 1
    if (num >= 0):
        # Numero positivo
        cntPos = cntPos + 1
        sumPos = sumPos + num
    else:
        # Numero negativo
        cntNeg = cntNeg + 1
        sumNeg = sumNeg + num

# Calculo de los porcentajes y los promedios
pNeg = (cntNeg/N)*100
pPos = (cntPos/N)*100
promNeg = sumNeg/cntNeg
promPos = sumPos/cntPos

# Despliegue de los resultados
print("Estadisticas")
print("Porcentaje de numeros negativos: ", pNeg, sep="")
print("Promedio de numeros negativos: ", promNeg, sep="")
print("Porcentaje de numeros positivos: ", pPos, sep="")
print("Promedio de numeros negativos: ", promPos, sep="")