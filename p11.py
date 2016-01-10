#function

def printfunc():  #function declaration
    print 'Hello'


def calfunc(a,b):
    c = a+b
    return c

def deffunc(a,b,c=5): #pass defolt argument
    return a+b+c

printfunc()   #print function
print calfunc(2,4)
print deffunc(2,4)
