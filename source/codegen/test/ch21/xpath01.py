# xpath01.py 
# 4XPath from PyXML 
# or 4XPath from 4Suite < version 0.12 
from xml.xpath import Evaluate 
from xml.dom.ext.reader.Sax2 import Reader  
from xml.dom.ext import PrettyPrint  
 
reader = Reader()  # Reader 객체를 생성한다.  
dom = reader.fromUri('sample04.xml')  # URI를 지정한다.  
 
xpath0 = 'user/name' 
nodeList = Evaluate(xpath0, dom.documentElement)  # 표현식, 문맥 노드를 인수로 전달하고 노드 집합을 얻는다. 
for node in nodeList: 
        PrettyPrint(node)  # 각 노드를 출력한다. 
