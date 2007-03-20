# sax07.py 
from xml.sax import handler, parseString 
 
class MyHandler(handler.ContentHandler): 
    def characters(self, content):   
        print content.encode('euc-kr') 
 
myhandler = MyHandler() 
s = open('names3.xml').read() 
u = unicode(s, 'euc-kr') 
parseString(u, myhandler) 
