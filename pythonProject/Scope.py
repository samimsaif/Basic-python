a = 30  #global scope
b = 50

def saif():
    x = 100  #local Scope
    print(x)
    print(a)
    print(a,b)
    print(a+b)
saif()

