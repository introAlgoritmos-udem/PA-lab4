# Inicializacion de variables - Votos
vA = 0 
vB = 0 
vC = 0 
vNulos = 0

# Preguntar si hay votantes
fin = input("Cerrar mesa (y/n): ")
while (fin == 'n'):
    # Despliegue de los candidatos
    print("Candidatos")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")
    # Solicitud del voto
    voto = int(input("Elija el numero del candidato de su preferencia: "))
    # Conteo de votos
    if(voto == 1):
        # Voto para A
        vA = vA + 1
    elif (voto == 2):
        # Voto para B
        vB = vB + 1
    elif (voto == 3):
        # Voto para C
        vC = vC + 1
    else:
        # Voto nulo
        vNulos = vNulos + 1
    # Preguntar si hay votantes
    fin = input("Cerrar mesa (y/n): ")

# Despliegue de los votos al cerrar la jornada de votacion
totalValidos = vA + vB + vC
totalVotos = totalValidos + vNulos

# Despliegue de los votos
print("Resultados de las votaciones")
print("-> Votos del candidato A: ", vA, sep = "")
print("-> Votos del candidato B: ", vB, sep = "")
print("-> Votos del candidato C: ", vC, sep = "")
print("-> Votos nulos: ", vNulos, sep = "")
print("-> Votos de votos: ", totalVotos, sep = "")

# Despliegue de los ganadores
if (vNulos >= totalValidos):
    # Repeticion por la cantidad de votos nulos
    print("Se deben repetir las elecciones")
else: 
    if ((vA == vB)and(vB == vC)):
        # Repeticion por igual numero de votos para todos los candidatos
        print("Se deben repetir las elecciones")
    else:
        if ((vA > vB)and(vA > vC)):
            print("El ganador es el candidato A")
        elif ((vB > vA)and(vB > vC)):
            print("El ganador es el candidato B")
        elif ((vC > vB)and(vC > vA)):
            print("El ganador es el candidato C")
        else:
            print("Se deben repetir las elecciones")


        
    



    

