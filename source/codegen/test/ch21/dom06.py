# dom06.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
from StringIO import StringIO 
 
reader = Reader()  # Reader ��ü�� �����Ѵ�. 
dom = reader.fromUri('sample01.xml')  # URI�� �����Ѵ�. 
strio = StringIO()   # ���ڿ� ��ü�� �����. 
PrettyPrint(dom, strio) # ���ڿ� ��ü�� ��µȴ� 
xmlstr = strio.get_value() # ����� ���ڿ��� ����. 
