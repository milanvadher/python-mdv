#file operation in python


#write operation

mdv = open("new.txt","w") #open file in write mode
mdv.write("this is my file\n") #add some data in new file
mdv.write("this is my second line\n")
mdv.close()


#print edited file
mdv = open("new.txt","r")
md = mdv.read()
print (md)
mdv.close()


#if we write in same file in write mode so ther is delete whole data and write new data in file

# so we can use append to keep our data
mdv = open("new.txt","w")
the = ["this added now\n","and this also\n"]
mdv.writelines(the)
mdv.close()

mdv=open("new.txt","r")
md =mdv.read()
print (md)
mdv.close()

mdv = open("new.txt","r")

try:
    mdv.write("python is great")
    mdv.write("python is easy")
except Exception, e:
    print 'an error occures'
mdv.close()
