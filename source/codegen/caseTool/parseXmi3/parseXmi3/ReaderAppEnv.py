# -*- coding: utf-8 -*-
import CommonUtil as ComUtil1
ComUtil = ComUtil1.CommonUtil()

# start
class ReaderAppEnv:
	def __init__(self):
		self.AppEnvData={}

	def saveAppEnvInfo(self, inAppEnvXml):
		doc = ComUtil1.getDomEncodeUtf8(inAppEnvXml)
		for attrName in ['writer','writeDate','subSystemName', \
		  'isClassList','isClassDefinition',\
		  'isInterfaceList', 'isInterfaceDefinition', \
		  'isUseCaseList',\
		  'isClassExport', 'isInterfaceExport']:
			outValue = doc.getElementsByTagName("appEnv")[0].getAttribute(attrName)
			value1 = ComUtil1.encodeCp949(outValue)
			self.__setitem__(attrName, value1)
			#apply(
	
	def __setitem__(self, key, item): 
		self.AppEnvData[key] = item
	def __getitem__(self, key):
		return self.AppEnvData[key]
	
##	def setWriter(self, writer):
##		self.writer = writer
##	def getWriter(self):
##		return self.writer
##
##	def setWriteDate(self, writeDate):
##		self.writeDate = writeDate
##	def getWriteDate(self):
##		return self.writeDate
##
##	def setSubSystemName(self, subSystemName):
##		self.subSystemName = subSystemName
##	def getSubSystemName(self):
##		return self.subSystemName

if __name__ == '__main__':
	from path import path
	inPath = path('C:\_kldp\codegen\caseTool\parseXmi3\input\etc')
	inPath = inPath / 'appEnv.xml'
	aReaderAppEnv = ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(inPath)
		
