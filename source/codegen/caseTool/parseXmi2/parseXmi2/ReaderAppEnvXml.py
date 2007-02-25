# -*- coding: utf-8 -*-
import CommonUtil as comUtil
# start
class ReaderAppEnvXml:
	def saveWriterInfo(self, aClassInfo, inAppEnvXml):
		doc = comUtil.getDomEncodeUtf8(inAppEnvXml)	
		writer			= doc.getElementsByTagName("appEnv")[0].getAttribute('writer')
		writeDate		= doc.getElementsByTagName("appEnv")[0].getAttribute('writeDate')
		subSystemName	= doc.getElementsByTagName("appEnv")[0].getAttribute('subSystemName')
		aClassInfo.setWriter(writer)
		aClassInfo.setWriteDate(writeDate)	   
		aClassInfo.setSubSystemName(subSystemName)		

