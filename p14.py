'''
*
**
***
****
*****
****
***
**
*
'''


for i in range(0,10):
    if i > 5:
        for j in range(4,0,-1):
            print j*"*"
        break
    else:
        print i*"*"
