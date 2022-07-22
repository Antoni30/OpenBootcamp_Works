from Hora import Hora
def main():
    time=Hora.getTime()
    hora=time[3]
    if int(hora.split(':')[0])>=19 or int(hora.split(':')[0])==0:
        print("Es hora de regresar a Casa")
    else:
        print("Te falta {}:{} horas para salir del trabajo".format(19-int(hora.split(':')[0]),59-int(hora.split(':')[1])))

if __name__ =='__main__':
    main()