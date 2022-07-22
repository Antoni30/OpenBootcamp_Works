class Alumno:
    _nombre=""
    _nota=0
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota
    def aprobado(self):
        if(self._nota>=14):
            return True
        else:
            return False
    def getNombre(self):
        return self._nombre
    def getNota(self):
        return self._nota
    def setNombre(self,nombre):
        self._nombre=nombre
    def setNota(self,nota):
        self._nota=nota

objAlumno = Alumno("Antoni",15.52)
if(objAlumno.aprobado()):
    print("{} esta Aprobado".format(objAlumno.getNombre()))
else:
    print("{} esta Reprobado".format(objAlumno.getNombre()))