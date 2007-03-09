# -*- coding: utf-8 -*-
import sys
# start
import handyxml

class DbAndJavaTypeMapper:
	def __init__(self, CONS):
		#CONS = Constants()
		self.dbAndJavaTypeDict = {}
		self.parseXml(CONS.DB_JAVA_TYPE_MAPPING)
		
	def parseXml(self, inXmlFile):
		for attr in handyxml.xpath(inXmlFile, '//property'):
			self.dbAndJavaTypeDict[attr.dataType] = attr.javaType
	def getJavaType(self, dataType):
		
		try:
			out = self.dbAndJavaTypeDict[dataType]
		except KeyError:
			out = dataType
			
		return out
	
if __name__ == "__main__":
	aDbAndJavaTypeMapper = DbAndJavaTypeMapper()
	print aDbAndJavaTypeMapper.getJavaType('C')
