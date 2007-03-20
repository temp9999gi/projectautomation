# dom10.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
users = doc.getElementsByTagName('user') 
parent = users[0].parentNode 
parent.removeChild(users[0]) 
parent.appendChild(users[0]) 
 
PrettyPrint(doc) 
