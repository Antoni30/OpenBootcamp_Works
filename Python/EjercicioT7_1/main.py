def escribirArchivo(dirArchivo,texto):
    try:
        open(dirArchivo)
    except FileNotFoundError:
        print("No existe Archivo")
        exit()
    a=open(dirArchivo,'a')
    texto+='\n'
    a.write(texto)
    a.close()

def main():
   escribirArchivo('./EjercicioT7_1/archivo.txt',"siuuuuu mas facil que c++ y c")
 
if __name__=='__main__':
    main()
