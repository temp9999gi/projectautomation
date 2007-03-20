# dom03.py 
from xml.dom.ext.reader.Sax2 import * 
 
f = open('sample01.xml') 
reader = Reader()  # Reader 객체를 생성한다. 
dom1 = reader.fromStream(f)  # 파일 객체로 부터 읽어 DOM 트리를 생성한다. 
 
dom2 = reader.fromUri('sample01.xml')  # URI에서 DOM 트리를 생성한다. 
 
dom3 = reader.fromString('<value><int>1</int></value>')  # 문자열에서 DOM 트리를 생성한다. 
