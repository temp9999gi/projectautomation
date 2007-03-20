# xpath02.py 
# 4XPath from 4Suite >= version 0.12 
from xml.xpath import Compile 
from xml.xpath.Context import Context 
from xml.dom.ext.reader.Sax2 import Reader  
from xml.dom.ext import PrettyPrint  
 
reader = Reader()  # Reader ��ü�� �����Ѵ�.  
dom = reader.fromUri('sample04.xml')  # URI�� �����Ѵ�.  
 
expression = Compile('user/email')    # ǥ������ �������ϰ� 
context = Context(dom.documentElement) # ���� ��嵵 ��´�. 
nodeList = expression.evaluate(context) # ����.. 
for node in nodeList: 
        PrettyPrint(node) 
