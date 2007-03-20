# -*- coding: utf-8 -*-
# xpath01.py 
# 4XPath from PyXML 
# or 4XPath from 4Suite < version 0.12 
from xml.xpath import Evaluate 
from xml.dom.ext.reader.Sax2 import Reader  
from xml.dom.ext import PrettyPrint
inFile ='C:/_kldp/codegen/test/input/Party.xmi'
#inFile = './input/Party.xmi'              
reader = Reader()  # Reader ��ü�� �����Ѵ�.  
dom = reader.fromUri(inFile)  # URI�� �����Ѵ�.  
                          
#xpath0 = 'user/name'
#xpath0 = 'XMI/XMI.content/UML:Model/UML:Namespace.ownedElement'
xpath0 = 'XMI.content'
# XMI.content
# <UML:Model xmi.id="UMLProject.1">
#   <UML:Namespace.ownedElement>  
  
nodeList = Evaluate(xpath0, dom.documentElement)  # ǥ����, ���� ��带 �μ��� �����ϰ� ��� ������ ��´�.

for nodes in nodeList:
	for node in nodes.childNodes:
		if node.nodeType == node.ELEMENT_NODE:
			if node.__nodeName == 'UML:Model':
				print 'node.__nodeName: [',node.__nodeName,']'
				#print 'node: [',node,']'
				print 'node: [',dir(node),']'





# 			print "Found it!"
	
	
	

	#print 'node.get_nodeName(): [',node.get_nodeName(),']'

	#PrettyPrint(node)  # �� ��带 ����Ѵ�. 
	
	