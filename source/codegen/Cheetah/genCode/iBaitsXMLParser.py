#*- coding: utf-8 -*-
import string
import sys
import xml.dom.minidom

from classDefinition import *
from callMethodInfo import *

from xml.parsers.xmlproc import xmlval

class IBatisXMLParser :

	def __init__(self):
		pass

	def doParse(self):

		xmlFile = './input/'+sys.argv[1]

		doc = xml.dom.minidom.parse(xmlFile)

		# getElementsByTagName("name")[0].firstChild.data 의 리턴은 유니코드임
		# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc0 in position 0: ordinal not in range(128)
		# str(className)
		#className = temp.encode('cp949') #Korean

		namespace 	= doc.getElementsByTagName("sqlMap")[0].getAttribute('namespace')
		alias 		= doc.getElementsByTagName("typeAlias")[0].getAttribute('alias')
		type1 		= doc.getElementsByTagName("typeAlias")[0].getAttribute('type')

		aSqlMaster = SqlMaster(namespace,alias,type1)

		aCallMethodInfoList = self.getCallMethodInfo(aSqlMaster,doc)

		aSqlMaster.setCallMethodInfoList(aCallMethodInfoList)
		self.parseDefinitionXml(aSqlMaster)

		return aSqlMaster

	def parseDefinitionXml(self, aSqlMaster):
		doc = xml.dom.minidom.parse(DEFINITION_XML)
		packagePath	= doc.getElementsByTagName("package")[0].getAttribute('path')
		aSqlMaster.setPackagePath(packagePath)

	def getCallMethodInfo(self,aSqlMaster,doc):
		aCallMethodInfo = []
		aCallMethodInfo = loadCallMethodInfoFromXml(aSqlMaster,doc,aCallMethodInfo,'select')
		aCallMethodInfo = loadCallMethodInfoFromXml(aSqlMaster,doc,aCallMethodInfo,'insert')
		aCallMethodInfo = loadCallMethodInfoFromXml(aSqlMaster,doc,aCallMethodInfo,'update')
		aCallMethodInfo = loadCallMethodInfoFromXml(aSqlMaster,doc,aCallMethodInfo,'delete')

		return aCallMethodInfo

def loadCallMethodInfoFromXml(aSqlMaster,doc,aCallMethodInfo,crud):
	sqlList = doc.getElementsByTagName(crud)
	callMethodList=[]
	for sql in sqlList:
		sqlId           = sql.getAttribute('id')
		resultClass 	= sql.getAttribute('resultClass')
		parameterClass	= sql.getAttribute('parameterClass')
		sqlText		    = sql.firstChild.data

		theCallMethodInfo = CallMethodInfo(sqlId,resultClass,parameterClass,sqlText, crud)
		aCallMethodInfo.append(theCallMethodInfo)

		methodBody = theCallMethodInfo.getMethodBody(aSqlMaster,theCallMethodInfo, crud)
		theCallMethodInfo.setMethodBody(methodBody)
		theCallMethodInfo.appendMethodBody(aSqlMaster)

		if crud == 'select':
			callMethodList.append(theCallMethodInfo) # sel인경우 sel sql당 하나씩의 메소드 생성
			aMethodInfo = MethodInfo(aSqlMaster,getMainMethodName(aSqlMaster,crud), callMethodList)
			aSqlMaster.setMethodInfoList(aMethodInfo)

			callMethodList=[] # 왜 널을 대입하나? select 메소드당 call메소드를 세팅하기 위함

		else:
			callMethodList.append(theCallMethodInfo)

	if crud <> 'select':
		aMethodInfo = MethodInfo(aSqlMaster,getMainMethodName(aSqlMaster,crud), callMethodList)
		aSqlMaster.setMethodInfoList(aMethodInfo)

	return aCallMethodInfo


def getMainMethodName(aSqlMaster,crud):
	aMethodName=''
	if crud == 'select':
		aMethodName = 'get' + aSqlMaster.className
	elif crud == 'insert':
		aMethodName = 'insert' + aSqlMaster.className
	elif crud == 'update':
		aMethodName = 'update' + aSqlMaster.className
	else:
		aMethodName = 'delete' + aSqlMaster.className

	return aMethodName


def getInputArgumentMethodBody______111(aCallMethodInfo):
  inputArgument = ''
  for x in aCallMethodInfo.whereArgList:
    print len(x),'len(x)'
    if len(x) > 0:
      inputArgument = inputArgument + x + ', '
  if len(inputArgument) > 0:
    s = inputArgument[:len(inputArgument)-2]
    inputArgument = s

  #print inputArgument
  return inputArgument