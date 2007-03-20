# dom16.py 
from xml.dom.NodeFilter import NodeFilter 
from xml.dom.ext.reader.Sax2 import Reader 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
tw = doc.createTreeWalker(doc, NodeFilter.SHOW_ELEMENT, None, 1) 
 
elem = tw.nextNode() 
while elem: 
    print elem.nodeName 
    elem = tw.nextNode() 
