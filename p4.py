#calculater

x = float(input("Enter the value of x : ")) #first variable
y = float(input("ENter the value of y : ")) #second variable

#print statment to choose for user
print "1 for addition"
print "2 for substractor"
print "3 for multiplication"
print "4 for division"
a = float(input("enter your choice"))


if a==1:
    print x+y  #addition
elif a==2:
    print x-y   #substractor
elif a==3:
    print x*y   #multiplication
elif a==4:
    print x/y   #division
else:
    print "enter proper choice"
