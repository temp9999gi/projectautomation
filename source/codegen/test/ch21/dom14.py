# dom14.py 
from xml.dom.NodeFilter import NodeFilter 
from xml.dom.ext.reader.Sax2 import Reader 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
iterator = doc.createNodeIterator(doc, NodeFilter.SHOW_TEXT, None, 0) 
elem = iterator.nextNode() 
while elem: 
    print elem.data, 
    elem = iterator.nextNode() 
