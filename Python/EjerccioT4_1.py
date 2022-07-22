import math
def areaTriangulo(altura,base):
    return base*altura
def areaCirculo(radio):
    return round(math.pi*(radio**2),2)

print("El area del Circulo es {}".format(areaCirculo(6)))
print("El area del Triangulo es {}".format(areaTriangulo(6,7)))