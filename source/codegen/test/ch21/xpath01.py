# xpath01.py 
# 4XPath from PyXML 
# or 4XPath from 4Suite < version 0.12 
from xml.xpath import Evaluate 
from xml.dom.ext.reader.Sax2 import Reader  
from xml.dom.ext import PrettyPrint  
 
reader = Reader()  # Reader ��ü�� �����Ѵ�.  
dom = reader.fromUri('sample04.xml')  # URI�� �����Ѵ�.  
 
xpath0 = 'user/name' 
nodeList = Evaluate(xpath0, dom.documentElement)  # ǥ����, ���� ��带 �μ��� �����ϰ� ��� ������ ��´�. 
for node in nodeList: 
        PrettyPrint(node)  # �� ��带 ����Ѵ�. 
