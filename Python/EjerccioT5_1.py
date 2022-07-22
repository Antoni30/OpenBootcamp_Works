class Vehiculo:
    _color=""
    _ruedas=0
    _puertas=0
    def __init__(self,color,ruedas,puertas):
        self._color=color
        self._ruedas=ruedas
        self._puertas=puertas
    def getColor(self):
        return self._color
    def getRuedas(self):
        return self._ruedas
    def getPuertas(self):
        return self._puertas
    def setColor(self,color):
        self._color=color
    def setRuedas(self,ruedas):
        self._ruedas=ruedas
    def setPuertas(self,puertas):
        self._puertas=puertas
class Coche(Vehiculo):
    _velocidad=0
    _cilindraje=0
    def __init__(self, color, ruedas, puertas,velocidad,cilindraje):
        super().__init__(color, ruedas, puertas)
        self._velocidad=velocidad
        self._cilindraje=cilindraje
    def getVelocidad(self):
        return self._velocidad
    def getCilindraje(self):
        return self._cilindraje
    def setVelocidad(self,velocidad):
        self._velocidad=velocidad
    def setCilindraje(self,cilindraje):
        self._cilindraje=cilindraje

miCoche = Coche("Rojo",4,2,130,4)

print("Mi cache de color {} de {} ruedas, {} puetas, alcanza una velocidad de {}km/s y tiene {} cilindros".format(miCoche.getColor(),miCoche.getRuedas(),miCoche.getPuertas(),miCoche.getVelocidad(),miCoche.getCilindraje()))
    