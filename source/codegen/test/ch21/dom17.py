# dom17.py 
from xml.dom.NodeFilter import NodeFilter 
from xml.dom.ext.reader.Sax2 import Reader 
 
def doSomething(node): 
   if node.nodeName in ('email', 'name'): 
       print node.nodeName, ':', node.firstChild.data 
   else: 
      print node.nodeName 
 
def processMe(tw): 
   n = tw.currentNode 
   doSomething(n) 
   child = tw.firstChild() 
   while child: 
       processMe(tw) 
       child = tw.nextSibling() 
   tw.currentNode = n 
 
reader = Reader() 
doc = reader.fromUri('sample02.xml') 
 
tw = doc.createTreeWalker(doc, NodeFilter.SHOW_ELEMENT, None, 1) 
processMe(tw) 
