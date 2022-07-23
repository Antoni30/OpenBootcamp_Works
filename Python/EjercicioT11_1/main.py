import sqlite3

def existUsuario(nombre):
    query=f'SELECT * FROM alumnos WHERE nombre="{nombre}"'
    conn= sqlite3.connect('miaplicacion.db')
    cursor= conn.cursor()
    row=cursor.execute(query)
    busqueda=row.fetchone()
    cursor.close()
    conn.close()
    return busqueda
def main():
    nombre=input("Ingrese el usuario que quiere buscar: ")
    user=existUsuario(nombre)
    if(user==None):
        print("Usuario no encontrado en BD alumnos")
    else:
        print(f'Existe {nombre}, se encuenta en la posicion {user[0]} de la BD alumnos')
if __name__=='__main__':
    main()