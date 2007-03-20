#! /usr/local/bin/python
# xslt04.py
from Ft.Xml.Xslt import Processor
from Ft.Xml import InputSource
import cgi

print 'Content-Type: text/html\n'
form = cgi.FieldStorage()
fname = form.getvalue('source', 'sample04.xml')  # source�� �־������� �� ���� ���, �ƴϸ� sample04.xml�� ����Ѵ�.

processor = Processor.Processor()  
transform = InputSource.DefaultFactory.fromUri("sample04.xsl") 
processor.appendStylesheet(transform)  # ó���⿡ ����Ѵ�.

source = InputSource.DefaultFactory.fromUri(fname)  # XML ���� ��ü�� �����
result = processor.run(source)    # ó���Ѵ�.
print result
