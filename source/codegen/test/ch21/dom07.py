# dom07.py 
from xml.dom.ext.reader.Sax2 import Reader 
 
def getAllText(node): 
    s = '' 
    for node in node.childNodes: 
        if node.nodeType == node.TEXT_NODE: 
            s += node.nodeValue 
        elif node.nodeType == node.ELEMENT_NODE: 
            s += getAllText(node) 
    return s 
 
if __name__ == '__main__': 
    reader = Reader() 
    dom = reader.fromUri('sample02.xml') 
    print getAllText(dom) 
