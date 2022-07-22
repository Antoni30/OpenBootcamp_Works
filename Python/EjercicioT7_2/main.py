import pickle
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
    def __str__(self):
        return f'Vehiculo {self._color}\nPuertas {self._puertas}\nRuedas {self._ruedas}'

def escribirArchivo(dirArchivo,objeto):
    f=open(dirArchivo,'wb')
    pickle.dump(objeto,f)
    f.close()
def leerArchivo(dirArchivo):
    f=open(dirArchivo,'rb')
    obj=pickle.load(f)
    f.close()
    return obj
def main():
    obj1=Vehiculo("Rojo",4,2)
    escribirArchivo('./EjercicioT7_2/archivo.bin',obj1)
    objB=leerArchivo('./EjercicioT7_2/archivo.bin')
    print(objB)
if __name__=='__main__':
    main()