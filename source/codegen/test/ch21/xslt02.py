# xslt02.py 
from Ft.Xml.Xslt import Processor 
from Ft.Xml import InputSource 
 
xslt = open('sample04.xsl').read()  # 스타일시트를 문자열로 읽어들인다 
xml = open('sample04.xml').read()   # xml 문서를 문자열로 읽어들인다 
 
processor = Processor.Processor() 
transform = InputSource.DefaultFactory.fromString(xslt)  # 스타일시트 객체를 만든다 
processor.appendStylesheet(transform)  # 처리기에 등록한다 
 
source = InputSource.DefaultFactory.fromString(xml)  # XML 문서 객체를 만든다 
result = processor.run(source)    # 처리한다. 
print result 
