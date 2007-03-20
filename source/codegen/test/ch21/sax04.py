# sax04.py  
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
      
if __name__ == '__main__': 
    h = MyHandler()   
    parser = make_parser()   
    parser.setContentHandler(h)   
    parser.setErrorHandler(ErrHandler()) 
    parser.parse('names2.xml') 
