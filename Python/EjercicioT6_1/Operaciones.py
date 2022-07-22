from unittest import result


def suma(*args):
    result=0
    for arg in args:
        result+=arg
    return result

def resta(*args):
    result=0;
    for arg in args:
        result-=arg
    return result

def multiplicar(*args):
    result=1
    for arg in args:
        result*=arg
    return result
def dividir(a,b):
    return a/b

