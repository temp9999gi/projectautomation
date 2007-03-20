# dom12.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml')      # ���� �б� 
doc2 = reader.fromString('<userlist/>')   # ���ڿ����� �⺻ ���� ��ü ���� 
 
node = doc2.importNode(doc.documentElement.childNodes[1], 1)  # doc2�� user ������Ʈ �ϳ��� ����Ʈ�Ѵ� 
doc2.documentElement.appendChild(node)    # ���ϵ� ��带 doc2�� ��򰡿� �߰��� �� �ִ�. 
 
PrettyPrint(doc2) 
