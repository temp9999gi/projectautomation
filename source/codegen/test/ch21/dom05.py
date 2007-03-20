# dom05.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader()  # Reader 객체를 생성한다. 
dom = reader.fromUri('sample01.xml')  # URI를 지정한다. 
f = open('test.xml', 'w') 
PrettyPrint(dom, f)     # dom 을 파일 객체로 출력한다. 
f.close() 
