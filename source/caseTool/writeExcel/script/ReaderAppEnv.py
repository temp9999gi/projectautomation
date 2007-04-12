# -*- coding: utf-8 -*-
import CommonUtil as ComUtil1
ComUtil = ComUtil1.CommonUtil()

# start
class ReaderAppEnv:
	def __init__(self):
		self.appEnvData={}
		self.classTemplateEnv={}
		

	def saveAppEnvInfo(self, inAppEnvXml):
		doc = ComUtil1.getDomEncodeUtf8(inAppEnvXml)
		for attrName in ['writer','writeDate','subSystemName', \
		  'isClassList','isClassDefinition',\
		  'isInterfaceList', 'isInterfaceDefinition', \
		  'isUseCaseList',\
		  'isClassExport', 'isInterfaceExport']:
			outValue = doc.getElementsByTagName("appEnv")[0].getAttribute(attrName)
			value1 = ComUtil1.encodeCp949(outValue)
			self.setAppEnvData(attrName, value1)
			#apply(
	
	def setAppEnvData(self, key, item):
		self.appEnvData[key] = item
	def getAppEnvData(self, key):
		return self.appEnvData[key]
	
	#---------------------------------------------------------------------------
	def saveClassTemplateEnv(self, inClassTemplateEnvXml):
		doc = ComUtil1.getDomEncodeUtf8(inClassTemplateEnvXml)
		for attrName in ['rowPhase', \
			'colPhase', \
			'rowTask', \
			'colTask', \
			'rowWriter', \
			'colWriter', \
			'rowWriteDate', \
			'colWriteDate', \
			'rowSubSystemName', \
			'colSubSystemName', \
			'rowClass', \
			'colClass', \
			'rowPackage', \
			'colPackage', \
			'rowDesc', \
			'colDesc', 'AttrStartPosition']:
			outValue = doc.getElementsByTagName("appEnv")[0].getAttribute(attrName)
			value1 = ComUtil1.encodeCp949(outValue)
			self.setClassTemplateEnvData(attrName, value1)
			#apply(

	def setClassTemplateEnvData(self, key, item):
		self.classTemplateEnv[key] = int(item)
	def getClassTemplateEnvData(self, key):
		return self.classTemplateEnv[key]

if __name__ == '__main__':
	from path import path
	inPath = path('C:\_kldp\codegen\caseTool\parseXmi3\input\etc')
	inPath = inPath / 'appEnv.xml'
	aReaderAppEnv = ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(inPath)
		
