# xslt02.py 
from Ft.Xml.Xslt import Processor 
from Ft.Xml import InputSource 
 
xslt = open('sample04.xsl').read()  # ��Ÿ�Ͻ�Ʈ�� ���ڿ��� �о���δ� 
xml = open('sample04.xml').read()   # xml ������ ���ڿ��� �о���δ� 
 
processor = Processor.Processor() 
transform = InputSource.DefaultFactory.fromString(xslt)  # ��Ÿ�Ͻ�Ʈ ��ü�� ����� 
processor.appendStylesheet(transform)  # ó���⿡ ����Ѵ� 
 
source = InputSource.DefaultFactory.fromString(xml)  # XML ���� ��ü�� ����� 
result = processor.run(source)    # ó���Ѵ�. 
print result 
