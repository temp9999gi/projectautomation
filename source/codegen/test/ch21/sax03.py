# sax03.py  
# Using Name Space 
from xml.sax import make_parser, handler   
from xml.sax.handler import feature_namespaces 
 
class MyHandler(handler.ContentHandler):  
    def startElementNS(self, name, qname, attrs):  
        print 'Start Tag:', name, qname 
        # attrs : AttributesImpl instance    
        for name in attrs.getNames():    # 속성 정보를 출력한다 (속성 이름, 속성 값)  
            print '\t', name, attrs.getValue(name)  
    def endElementNS(self, name, qname):   # 태그가 끝날 때 호출된다  
        print 'End Tag:', name, qname 
    def characters(self, content):  # 텍스트가 읽혀질 때 호출된다. 
        print '\tText :', content.replace('\n', '\\n') 
      
h = MyHandler()   
parser = make_parser()   
parser.setFeature(feature_namespaces, 1)        # 이름 공간 처리 on 
parser.setContentHandler(h)   
parser.parse('adr.xml') 
