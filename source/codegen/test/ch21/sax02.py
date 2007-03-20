# sax02.py 
from xml.sax import make_parser, handler  
 
class MyHandler(handler.ContentHandler): 
    def startDocument(self):  # ������ ���ۿ��� ȣ��ȴ� 
        print 'Start of Document' 
    def endDocument(self):    # ������ ������ ȣ��ȴ� 
        print 'End of Document' 
    def startElement(self, name, attrs): # ���ο� �±׸� ���� �� ȣ��ȴ� 
        print 'Start Tag:', name  
        # attrs : AttributesImpl instance   
        for name in attrs.getNames():    # �Ӽ� ������ ����Ѵ� (�Ӽ� �̸�, �Ӽ� ��) 
            print '\t', name, attrs.getValue(name) 
    def endElement(self, name):   # �±װ� ���� �� ȣ��ȴ� 
        print 'End Tag:', name 
    def characters(self, content):  # �ؽ�Ʈ�� ������ �� ȣ��ȴ�. �ؽ�Ʈ�� ��ġ�� ������ ����Ѵ�. 
        print 'Location : (%s, %s)' % (self.locator.getLineNumber(), self.locator.getColumnNumber()) 
        print '\tText :', content.replace('\n', '\\n') 
    def setDocumentLocator(self, locator):  # ���޵Ǵ� Locator ��ü�� �����صд�. 
        self.locator = locator 
     
h = MyHandler()  
parser = make_parser()  
parser.setContentHandler(h)  
parser.parse('names.xml')  
