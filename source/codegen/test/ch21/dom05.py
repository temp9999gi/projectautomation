# dom05.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader()  # Reader ��ü�� �����Ѵ�. 
dom = reader.fromUri('sample01.xml')  # URI�� �����Ѵ�. 
f = open('test.xml', 'w') 
PrettyPrint(dom, f)     # dom �� ���� ��ü�� ����Ѵ�. 
f.close() 
