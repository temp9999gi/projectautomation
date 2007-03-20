# -*- coding: utf-8 -*-
# start
import xml.dom.minidom
import handyxml
from ClassAttribute import *

class XmlParser :
	def parseXml(self, aClassInfo, inXmlFile):
		self.parseClassInfo(aClassInfo, inXmlFile)
		self.parseClassAttribute(aClassInfo, inXmlFile)

	def parseClassInfo(self, aClassInfo, inXmlFile):
		doc = xml.dom.minidom.parse(inXmlFile)
		className	= doc.getElementsByTagName("classInfo")[0].getAttribute('className')
		packagePath	= doc.getElementsByTagName("classInfo")[0].getAttribute('packagePath')
		aClassInfo.setAttributes(className, packagePath)
		
	def parseClassAttribute(self, aClassInfo, inXmlFile):
		classInfoList = []		
		for attr in handyxml.xpath(inXmlFile, '//attribute'):
			aClassAttribute = ClassAttribute()
			aClassAttribute.setClassAttribute(attr.name , attr.type)
			aClassInfo.addClassAttributeList(aClassAttribute)			
