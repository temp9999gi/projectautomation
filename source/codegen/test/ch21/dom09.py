# dom09.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
email = doc.getElementsByTagName('email')[0]   # ù ��° email ������Ʈ�� ��´� 
oldtext = email.firstChild    # �ؽ�Ʈ ������Ʈ�� ��´�. 
 
email.replaceChild(doc.createTextNode('gslee@pymail.net'), oldtext)  # ��ġ�Ѵ�. 
 
PrettyPrint(doc) 
