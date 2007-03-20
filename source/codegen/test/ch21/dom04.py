# dom04.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader()  # Reader 객체를 생성한다. 
dom = reader.fromUri('sample01.xml')  # URI를 지정한다. 
PrettyPrint(dom)        # dom 을 화면으로 출력한다. 
