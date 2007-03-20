# dom06.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
from StringIO import StringIO 
 
reader = Reader()  # Reader 객체를 생성한다. 
dom = reader.fromUri('sample01.xml')  # URI를 지정한다. 
strio = StringIO()   # 문자열 객체를 만든다. 
PrettyPrint(dom, strio) # 문자열 객체로 출력된다 
xmlstr = strio.get_value() # 저장된 문자열을 얻어낸다. 
