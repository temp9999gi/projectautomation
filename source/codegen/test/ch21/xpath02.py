# xpath02.py 
# 4XPath from 4Suite >= version 0.12 
from xml.xpath import Compile 
from xml.xpath.Context import Context 
from xml.dom.ext.reader.Sax2 import Reader  
from xml.dom.ext import PrettyPrint  
 
reader = Reader()  # Reader 객체를 생성한다.  
dom = reader.fromUri('sample04.xml')  # URI를 지정한다.  
 
expression = Compile('user/email')    # 표현식을 컴파일하고 
context = Context(dom.documentElement) # 문맥 노드도 얻는다. 
nodeList = expression.evaluate(context) # 실행.. 
for node in nodeList: 
        PrettyPrint(node) 
