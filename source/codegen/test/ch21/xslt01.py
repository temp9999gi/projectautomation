# xslt01.py 
from Ft.Xml.Xslt import Processor 
from Ft.Xml import InputSource 
 
processor = Processor.Processor()  # ó���� ��ü�� �����Ѵ�. 
transform = InputSource.DefaultFactory.fromUri("sample04.xsl") # ��Ÿ�Ͻ�Ʈ ��ü�� ����� 
processor.appendStylesheet(transform)  # ó���⿡ ����Ѵ�. 
 
source = InputSource.DefaultFactory.fromUri("sample04.xml")  # XML ���� ��ü�� ����� 
result = processor.run(source)    # ó���Ѵ�. 
print result 
