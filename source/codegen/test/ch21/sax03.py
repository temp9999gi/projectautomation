# sax03.py  
# Using Name Space 
from xml.sax import make_parser, handler   
from xml.sax.handler import feature_namespaces 
 
class MyHandler(handler.ContentHandler):  
    def startElementNS(self, name, qname, attrs):  
        print 'Start Tag:', name, qname 
        # attrs : AttributesImpl instance    
        for name in attrs.getNames():    # �Ӽ� ������ ����Ѵ� (�Ӽ� �̸�, �Ӽ� ��)  
            print '\t', name, attrs.getValue(name)  
    def endElementNS(self, name, qname):   # �±װ� ���� �� ȣ��ȴ�  
        print 'End Tag:', name, qname 
    def characters(self, content):  # �ؽ�Ʈ�� ������ �� ȣ��ȴ�. 
        print '\tText :', content.replace('\n', '\\n') 
      
h = MyHandler()   
parser = make_parser()   
parser.setFeature(feature_namespaces, 1)        # �̸� ���� ó�� on 
parser.setContentHandler(h)   
parser.parse('adr.xml') 
