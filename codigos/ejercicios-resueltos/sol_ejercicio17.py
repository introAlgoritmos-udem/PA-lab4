# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:32:07 2022

@author: b12s306e30
"""

totalCorriente = 0
numDepCorriente = 0
totalAhorros = 0    
numDepAhorros = 0

# Ingreso de datos
N = int(input("Digite el numero de clientes: "))

# Procesamiento de cada uno de las consignaciones
for i in range(1, N + 1):
    deposito = int(input("Ingrese el valor a consignar: "))
    if (deposito >= 0):
        tipoCuenta = int(input("Ingrese el tipo de cuenta [1: Ahorros - 2: Corriente]: "))
        if (tipoCuenta == 1):
            # Cuenta de ahorros
            totalAhorros = totalAhorros + deposito
            numDepAhorros = numDepAhorros + 1
        else:
            # Cuenta corriente
            totalCorriente = totalCorriente + deposito
            numDepCorriente = numDepCorriente + 1
    else:
        print("Valor de consignación inválido")

# Calculo del numero de consignaciones negativas
numDepNeg = N - numDepAhorros - numDepCorriente

# Calculo de los porcentajes
pAhorro = (numDepAhorros/N)*100
pCorriente = (numDepCorriente/N)*100 
pNeg = (numDepNeg/N)*100

# Resumen de las transacciones hechas
print("---------------------------- ESTADISTICAS ----------------------------")
print("- Total consignaciones en cuentas de ahorro: ", totalAhorros, sep = "")
print("- Porcentaje de consignaciones de ahorro realizadas: ", pAhorro, sep = "")
print("- Total consignaciones en cuentas corrientes: ", totalCorriente, sep = "")
print("- Porcentaje de consignaciones en cuenta corriente realizadas: ", pCorriente, sep = "")
print("- Porcentaje de consignaciones invalidas: ", pNeg, sep = "")
print("----------------------------------------------------------------------")

