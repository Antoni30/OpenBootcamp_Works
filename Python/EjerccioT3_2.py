lista=[]
inicio=int(input("Ingrese el Inicio: "))
final=int(input("Ingrese el Final: "))
for i in range(inicio,final):
    if i%2!=0:
        lista.append(i)
print(lista)