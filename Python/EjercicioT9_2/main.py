from functools import reduce
def main():
    lista=[]
    for i in range (1,30):
        lista.append(i)
    a=filter(lambda x: x%2!=0 , lista)
    a=reduce(lambda a,b:a+b,lista)
    print(a)
if __name__=='__main__':
    main()