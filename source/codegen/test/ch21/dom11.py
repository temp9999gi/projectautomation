# dom11.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
firstUser = doc.getElementsByTagNameNS(None, 'user')[0] 
clonedUser = firstUser.cloneNode(1) 
 
doc.documentElement.appendChild(clonedUser) 
PrettyPrint(doc) 
