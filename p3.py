#nested If-Else

a=1 #first variable
b=2 #second variable
c=3 #third variable

#first method
if a>b:
    #nested If-Else
    if a>c: #compair bitween a nd c
        print "a is grater"
    else:
        print "c is grater"
else:
    #nested If-Else
    if b>c: #compair bitween b and c
        print "b is grater"
    else:
        print "c is grater"


#second method (redusing the code using and operator)
'''
if a>b and a>c:
    print "a is grater"
elif b>a and b>c:
    print "b is grater"
else:
    print "c is grater"
'''

#third method using max
'''
max(a,b,c)
'''
