# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:44:34 2022

@author: Usuario
"""

# Inicializacion de variables
cnt = 0
suma = 0

# Preguntar si dato
dato = int(input("Digite el numero positivo a sumar (o un negativo para acabar): "))

# Entrada de los impuestos de cada cliente
while(dato >= 0):
    suma = suma + dato
    cnt = cnt + 1
    
    # Preguntar si dato
    dato = int(input("Digite el numero positivo a sumar (o un negativo para acabar): "))

# Despliegue de los resultados generales
if(cnt == 0):
    print("Promedio: 0")
else:
    prom = suma/cnt
    print("Promedio", prom, sep = "")