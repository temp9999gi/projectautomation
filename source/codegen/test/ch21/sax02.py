# sax02.py 
from xml.sax import make_parser, handler  
 
class MyHandler(handler.ContentHandler): 
    def startDocument(self):  # 문서의 시작에서 호출된다 
        print 'Start of Document' 
    def endDocument(self):    # 문서의 끝에서 호출된다 
        print 'End of Document' 
    def startElement(self, name, attrs): # 새로운 태그를 만날 때 호출된다 
        print 'Start Tag:', name  
        # attrs : AttributesImpl instance   
        for name in attrs.getNames():    # 속성 정보를 출력한다 (속성 이름, 속성 값) 
            print '\t', name, attrs.getValue(name) 
    def endElement(self, name):   # 태그가 끝날 때 호출된다 
        print 'End Tag:', name 
    def characters(self, content):  # 텍스트가 읽혀질 때 호출된다. 텍스트의 위치와 내용을 출력한다. 
        print 'Location : (%s, %s)' % (self.locator.getLineNumber(), self.locator.getColumnNumber()) 
        print '\tText :', content.replace('\n', '\\n') 
    def setDocumentLocator(self, locator):  # 전달되는 Locator 객체를 저장해둔다. 
        self.locator = locator 
     
h = MyHandler()  
parser = make_parser()  
parser.setContentHandler(h)  
parser.parse('names.xml')  
