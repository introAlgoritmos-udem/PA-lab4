# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:32:07 2022

@author: b12s306e30
"""

cntAccidentes = 0 
cnt25 = 0
cntF = 0
cntM12_30 = 0
cntOutMed = 0    
ACTUAL_YEAR = 2022

# Ingreso de datos (año de nacimiento)
nacYear = int(input("-> Año de nacimiento del accidentado (o -1 para terminar): "))

# Procesamiento de cada uno de las consignaciones
while nacYear != -1:
    # Ingreso de datos (sexo y ciudad de registro)
    sexo = int(input("-> Sexo (1: Femenino - 2: Masculino): "))
    registro = int(input("-> Registro del carro (1: Medellin - 2: Fuera de Medellin)"))
    edad = ACTUAL_YEAR - nacYear
    
    # Actualizacion de los contadores  
    cntAccidentes = cntAccidentes + 1
    if (edad < 25):
        # Conductores con menos de 25 años
        cnt25 = cnt25 + 1
        
     
    if (sexo == 1):
        # Conductores de sexo femenino
        cntF = cntF + 1
    else:
        # Conductores de sexo masculino
        if ((edad >= 12) and (edad <= 30)):
            # Conductores hombres entre los 12 y 30 años
            cntM12_30 = cntM12_30 + 1
            
    if (registro != 1):
        # Vehiculos registrados fuera de medellinn
        cntOutMed = cntOutMed + 1
    
    
    nacYear = int(input("-> Año de nacimiento del accidentado (o -1 para terminar): "))
    # Ingreso de datos (año de nacimiento)
   
# Calculo los porcentajes
if (cntAccidentes == 0):
    # No hubo accidentes
    print("No hubo accidentes")
else:
    # Calculo de los porcentajes
    p25 = (cnt25/cntAccidentes)*100
    pF = (cntF/cntAccidentes)*100
    pM12_30 = (cntM12_30/cntAccidentes)*100
    pOutMed = (cntOutMed/cntAccidentes)*100
    # Resumen de estadisticas
    print("------------------------------------------- ESTADISTICAS -------------------------------------------")
    print("- Porcentaje de conductores menores de 25 años: ", p25, sep = "")
    print("- Porcentaje de conductores de sexo femenino: ", pF, sep = "")
    print("- Porcentaje de conductores masculinos con edades entre los 12 y 30 años: ", pM12_30, sep = "")
    print("- Porcentaje de conductores cuyos carros están registrados fuera de Medellín : ", pOutMed, sep = "")
    print("----------------------------------------------------------------------------------------------------")

