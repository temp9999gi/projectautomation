# -*- coding: utf-8 -*-
# start
import xml.dom.minidom
import handyxml
from ClassAttribute import *

class XmlParser :
	def parseXml(self, aClassInfo, inXmlFile):
		# self.parseClassInfo(aClassInfo, inXmlFile)
		self.parseClassAttribute(inXmlFile)

	def parseClassInfo(self, aClassInfo, inXmlFile):
		doc = xml.dom.minidom.parse(inXmlFile)
		className	= doc.getElementsByTagName("classInfo")[0].getAttribute('className')
		packagePath	= doc.getElementsByTagName("classInfo")[0].getAttribute('packagePath')
		aClassInfo.setAttributes(className, packagePath)
		
	def parseClassAttribute(self, inXmlFile):
		classInfoList = []		
		for attr in handyxml.xpath(inXmlFile, '//XMI.content'):
			#print dir(attr)
			print 'attr.node', attr.node
			print 'attr.childElements', attr.childElements
			for ce in attr.childElements:
				print 'ce.nodeName', ce.nodeName
				#print 'dir(ce.node)', dir(ce.node)
				print 'dir(ce)',dir(ce)
				for xx in ce.childElements:
					print 'xx.nodeName', xx.nodeName

			
# 			aClassAttribute = ClassAttribute()
# 			aClassAttribute.setClassAttribute(attr.name , attr.type)
# 			aClassInfo.addClassAttributeList(aClassAttribute)			
