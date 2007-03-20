# dom08.py 
from xml.dom.ext.reader.Sax2 import Reader 
from xml.dom.ext import PrettyPrint 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
def removeNode(name, node): 
    for childNode in node.childNodes: 
        if childNode.nodeName == name: 
            node.removeChild(childNode) 
        else: 
            removeNode(name, childNode) 
             
removeNode('email', doc) 
PrettyPrint(doc) 
