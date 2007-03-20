#! /usr/local/bin/python
# xslt04.py
from Ft.Xml.Xslt import Processor
from Ft.Xml import InputSource
import cgi

print 'Content-Type: text/html\n'
form = cgi.FieldStorage()
fname = form.getvalue('source', 'sample04.xml')  # source가 주어졌으면 그 값을 얻고, 아니면 sample04.xml을 사용한다.

processor = Processor.Processor()  
transform = InputSource.DefaultFactory.fromUri("sample04.xsl") 
processor.appendStylesheet(transform)  # 처리기에 등록한다.

source = InputSource.DefaultFactory.fromUri(fname)  # XML 문서 객체를 만든다
result = processor.run(source)    # 처리한다.
print result
