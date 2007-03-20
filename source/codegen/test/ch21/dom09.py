# dom09.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
email = doc.getElementsByTagName('email')[0]   # 첫 번째 email 엘리먼트를 얻는다 
oldtext = email.firstChild    # 텍스트 엘리먼트를 얻는다. 
 
email.replaceChild(doc.createTextNode('gslee@pymail.net'), oldtext)  # 대치한다. 
 
PrettyPrint(doc) 
