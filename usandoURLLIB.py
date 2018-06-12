#usandoURLLIB.py

from urllib import *
import urllib.request 

x= urllib.request.urlopen("https://ss64.com")
xr= x.read()
#ss64= 

print(xr)




