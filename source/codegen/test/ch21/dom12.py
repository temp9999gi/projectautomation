# dom12.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml')      # 문서 읽기 
doc2 = reader.fromString('<userlist/>')   # 문자열에서 기본 문서 객체 생생 
 
node = doc2.importNode(doc.documentElement.childNodes[1], 1)  # doc2로 user 엘리먼트 하나를 임포트한다 
doc2.documentElement.appendChild(node)    # 리턴된 노드를 doc2의 어딘가에 추가할 수 있다. 
 
PrettyPrint(doc2) 
