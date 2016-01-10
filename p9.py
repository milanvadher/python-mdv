'''
1. ask user input
2. save in list & tupple
3. when input 'H' stop input and print tuple and list
'''

l = [] #Declare a list
val = 0

while(val!='H'): #Terminate condition
    val = raw_input('Enter the value: ')
    l.append(val) #insert value
l.remove('H') #for remove H
t = tuple(l) #list to tuple

print t #print tuple
print l #print list
