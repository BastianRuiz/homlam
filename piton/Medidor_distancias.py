import math

def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# Coordenadas del primer acantilado
x1 = float(input("Ingrese la coordenada x del primer acantilado: "))
y1 = float(input("Ingrese la coordenada y del primer acantilado: "))

# Coordenadas del segundo acantilado
x2 = float(input("Ingrese la coordenada x del segundo acantilado: "))
y2 = float(input("Ingrese la coordenada y del segundo acantilado: "))

# Calcular la distancia
distancia = round(calcular_distancia(x1, y1, x2, y2), 2)

print(f"La distancia entre los dos acantilados es: {distancia} metros")