import usuario_script as us
def main():
    listaPaises=list(us.pedirUsuario());
    listaPaises.sort()
    print(listaPaises);

if __name__=='__main__':
    main()