# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:36:00 2022

@author: b12s306e30
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Se pide el numero
num = int(input("Digite el numero positivo o -1 para terminar: "))
mayor = num
while(num  >= 0):
    # Se busca el mmayor
    if(num >= mayor):
        mayor = num
    # Se pide el numero
    num = int(input("Digite el numero positivo o -1 para terminar: "))

# Se muestra el mayor
print("El mayor es: ", mayor, sep="")
