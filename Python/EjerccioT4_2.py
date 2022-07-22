def contDivisores(num):
    cont=0
    for i in range(1,num):
        if(num%i==0):
            cont+=1
    return cont
def esPrimo(num):
    if(contDivisores(num)>2):
        return "no es Primo"
    else:
        return "es Primo"
num=7
print("El numero {} {}".format(num,esPrimo(num)))