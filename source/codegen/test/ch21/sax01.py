# sax01.py 
from xml.sax import handler, make_parser 
 
class MyHandler(handler.ContentHandler): 
    def startElement(self, name, attrs): 
        print 'Start Tag:', name 
 
parser = make_parser() 
h = MyHandler() 
parser.setContentHandler(h) 
parser.parse('names.xml')    # url을 넘겨준다 
