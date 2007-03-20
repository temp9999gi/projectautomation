# xslt01.py 
from Ft.Xml.Xslt import Processor 
from Ft.Xml import InputSource 
 
processor = Processor.Processor()  # 처리기 객체를 생성한다. 
transform = InputSource.DefaultFactory.fromUri("sample04.xsl") # 스타일시트 객체를 만든다 
processor.appendStylesheet(transform)  # 처리기에 등록한다. 
 
source = InputSource.DefaultFactory.fromUri("sample04.xml")  # XML 문서 객체를 만든다 
result = processor.run(source)    # 처리한다. 
print result 
