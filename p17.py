#Exception


a = int(input("enter any value: "))


try:
    b = a + 2
    print b
except TypeError:
    print "Enter only integer"
