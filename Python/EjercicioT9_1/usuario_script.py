def pedirUsuario():
    usuario=input("Ingresa n paises separados por un coma ',': ")
    return set(usuario.lower().split(','))

