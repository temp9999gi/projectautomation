# -*- coding: utf-8 -*- 

from  string import *
import re
#<UML:Attribute xmi.id="UMLAttribute.7" name="name" visibility="public" isSpecification="false" ownerScope="instance" changeability="changeable" targetScope="instance" type="X.32" owner="UMLClass.6">
#  <UML:Attribute.initialValue>
#	<UML:Expression xmi.id="X.35" body="'default1'"/>
#  </UML:Attribute.initialValue>
#</UML:Attribute>
def parseTableInfo():
	inFile = './input/Party.xmi'        
	#p = re.compile('(<UML:Attribute.*?</UML:Attribute>)', re.I | re.S | re.UNICODE)
	#
	#p = re.compile('(<UML:Attribute xmi.id=*?>\s*<UML:Attribute.initialValue>*?</UML:Attribute.initialValue>\s*</UML:Attribute>)', re.I | re.S | re.UNICODE)
	#p = re.compile('(<UML:Attribute xmi.id=.*(?!<UML:Attribute xmi.id=).</UML:Attribute.initialValue>)', re.I | re.S | re.UNICODE)
# 	p = re.compile(r"""
# 	<UML:Attribute xmi.id=((?!<UML:Attribute xmi.id=).)*?</UML:Attribute.initialValue>"""
# 	, re.VERBOSE | re.I | re.S | re.UNICODE)		
	
# 	p = re.compile(r"""(<UML:Attribute xmi.id=.*?<UML:Attribute.initialValue>)"""
# 	, re.I | re.S | re.UNICODE)		

	p = re.compile(r"""^((?!<UML:Attribute.initialValue>).)*"""
	, re.I | re.S | re.UNICODE)		

	
# </UML:Attribute.initialValue>
#                 </UML:Attribute>	
	s = open(inFile).read()
	findedList = p.findall(s)    # 매치되는 애들을 추출하여 리스트로 리턴한다
	return findedList

findedList = parseTableInfo()

import xml.dom.minidom as minidom
import StringIO

for xx in findedList:
	head = """<XMI xmi.version = "1.1" xmlns:UML="href://org.omg/UML/1.3">\n"""
	tail = "\n</XMI>"
	xmlFile = head + str(xx) + tail
	print 'xmlfile', xmlFile
# 	doc_node = minidom.parseString(xmlFile)
# 	print doc_node
	

# 	print 'xx: [',xx,']'
	#xmlFile = StringIO.StringIO(xx)
	#doc = xml.dom.minidom.parse(xmlFile)

# DOC = """
# <XMI xmi.version = "1.1" xmlns:UML="href://org.omg/UML/1.3" timestamp = "Sat Dec 30 19:31:3 2006">
# <UML:Attribute xmi.id="UMLAttribute.7" name="name" visibility="public" isSpecification="false" ownerScope="instance" changeability="changeable" targetScope="instance" type="X.32" owner="UMLClass.6">
#                   <UML:Attribute.initialValue>
#                     <UML:Expression xmi.id="X.35" body="'default1'"/>
#                   </UML:Attribute.initialValue>
#                 </UML:Attribute>
# </XMI>
# """
# doc_node = minidom.parseString(DOC)	
# print doc_node
