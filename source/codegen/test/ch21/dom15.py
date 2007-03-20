# dom15.py 
from xml.dom.NodeFilter import NodeFilter 
from xml.dom.ext.reader.Sax2 import Reader 
 
class emailFilter(NodeFilter): 
    def acceptNode(self, node): 
        if node.localName == 'email': 
            return self.FILTER_ACCEPT 
        else: 
            return self.FILTER_REJECT 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
iterator = doc.createNodeIterator(doc, NodeFilter.SHOW_ELEMENT, emailFilter(), 0) 
elem = iterator.nextNode() 
while elem: 
    print elem.firstChild.data 
    elem = iterator.nextNode() 
