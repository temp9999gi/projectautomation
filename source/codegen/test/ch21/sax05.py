# sax05.py 
from xml.sax.sax2exts import XMLValParserFactory 
from xml.sax import make_parser, handler 
 
class ErrHandler(handler.ErrorHandler): 
    def error(self, exception): 
        print 'Error occured' 
        print exception 
    def fatalError(self, exception): 
        print 'FatalError occured' 
        print exception 
    def warning(self, exception): 
        print 'Warning occured' 
        print exception 
 
class MyHandler(handler.ContentHandler): 
    def startElement(self, name, attrs): 
        print 'Start Tag:', name 
    def ignorableWhitespace(self, content): 
        pass 
 
if __name__ == '__main__': 
    parser = XMLValParserFactory.make_parser() 
    parser.setContentHandler(MyHandler()) 
    parser.setErrorHandler(ErrHandler()) 
    parser.parse('sample03.xml') 
