 # -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:32:07 2022

@author: b12s306e30
"""

numEst = 0

# Ingreso de datos (codigo)
cod = int(input("Digite el codigo del estudiante (o -1 para terminar): "))

while cod != -1:
    numEst = numEst + 1
    # Ingreso de datos (notas)
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    prom = (nota1 + nota2 + nota3 + nota4)/4
    
    # Despliegue de la información del estudiante
    print("------- Estudiante ", numEst, " -------", sep = "")
    print("- Codigo: ", cod, sep = "")
    print("- Promedio: ", prom, sep = "")
    
    # Ingreso de datos (codigo) 
    cod = int(input("Digite el codigo del estudiante (o -1 para terminar): "))
