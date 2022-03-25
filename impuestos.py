# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:31:15 2022

@author: Usuario
"""

# Inicializacion de variables
total = 0

# Preguntar si hay cliente en la fila
ban = int(input("Hay fila (1: si - 0: No): "))

# Entrada de los impuestos de cada cliente
while(ban == 1):
    recaudo = int(input("Digite el monto a pagar: "))
    total = total + recaudo
    
    # Preguntar si hay cliente en la fila
    ban = int(input("Hay fila (1: si - 0: No): "))

# Despliegue del total recogido en el dia
print("El total recogido durante el dia fue de: $", total, sep = "")
