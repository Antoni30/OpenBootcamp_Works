def anioBisiesto(anio):
    if(anio%4==0 and anio%100!=0):
        return "es año bisiesto"
    return "no es año bisiesto"
anio=2002
print("El año {} {}".format(anio,anioBisiesto(anio)))
