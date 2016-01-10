#read image from internet

import urllib  #import library of urllib
f = open('logo.png','wb')
f.write(urllib.urlopen('abc.com/1.png').read())   #go to perticuler url and download pic as logo.png
f.close()
