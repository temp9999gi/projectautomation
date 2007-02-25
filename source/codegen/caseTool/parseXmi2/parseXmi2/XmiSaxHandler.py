# -*- coding: utf-8 -*-

from xml.sax import make_parser, handler
import xmiCommonUtil as xmiUtil
from Constants import *
from XMI import *

# log = logging.getLogger('XmiSaxHandler')
class XmiSaxHandler(handler.ContentHandler):
	def __init__(self, aModelInfo):
		self.setModelInfo(aModelInfo)
		self.XMI = aModelInfo.getXMI()

	def setModelInfo(self, aModelInfo):
		self.aModelInfo = aModelInfo
	def getModelInfo(self):
		return self.aModelInfo

	def startDocument(self):  # 문서의 시작에서 호출된다
		pass # print 'Start of Document'
	def endDocument(self):	# 문서의 끝에서 호출된다
		pass # print 'End of Document'
	def startElement(self, name, attrs): # 새로운 태그를 만날 때 호출된다
		
		# print 'Start Tag:', name
		if name == self.XMI.CLASS: #'UML:Class'
			self.aModelInfo.setClassDict(xmiUtil.getClass(attrs))

		if name == self.XMI.ATTRIBUTE: #'UML:Attribute'
			self.aModelInfo.addClassAttributeList(xmiUtil.getAttribute(attrs))
			
		if name == self.XMI.ATTRIBUTE_EXPRESSION: # UML:Attribute.initialValue #UML:Expression
			self.aModelInfo.addAttributeInitialValue(xmiUtil.getAttributeInitialValue(attrs))

		if name == self.XMI.OPERATION: #'UML:Operation'
			self.aModelInfo.addClassOperation(xmiUtil.getOperation(attrs))

		if name == self.XMI.METHOD_PARAMETER: #UML:Parameter
			self.aModelInfo.addOperationParameter(xmiUtil.getParameter(attrs))

		if name == self.XMI.DATATYPE: #'UML:DataType'
			self.aModelInfo.addDataType(xmiUtil.getDataType(attrs))

		if name == self.XMI.TAGGED_VALUE: # 'UML:TaggedValue'
			if xmiUtil.isDocumentationOfTag(attrs):
				self.aModelInfo.addTaggedValueList(xmiUtil.getTaggedValue(attrs))
				
				

	def endElement(self, name):   # 태그가 끝날 때 호출된다
		pass # print 'End Tag:', name
	def characters(self, content):  # 텍스트가 읽혀질 때 호출된다. 텍스트의 위치와 내용을 출력한다.
		pass
	def setDocumentLocator(self, locator):  # 전달되는 Locator 객체를 저장해둔다.
		self.locator = locator
