#open file in python

fopn = open("file.txt", "r")

#read file line by line
for line in fopn:
    if "hello" in line:
        print line
fopn.close()     #for close the open file
