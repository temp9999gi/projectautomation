# -*- coding: utf-8 -*-
import CommonUtil as ComUtil1
ComUtil = ComUtil1.CommonUtil()

# start
class ReaderAppEnvXml:
	def saveWriterInfo(self, aClassInfo, inAppEnvXml):
		doc = ComUtil1.getDomEncodeUtf8(inAppEnvXml)
		
		#메소드를 만든다.
		objectName='aClassInfo'
		for attrName in ['writer','writeDate','subSystemName']:
			exec getStringDefineMethod(objectName, attrName)
			
			# writer = doc.getElementsByTagName("appEnv")[0].getAttribute('writer')
			outValue = doc.getElementsByTagName("appEnv")[0].getAttribute(attrName)
			value1 = ComUtil1.encodeCp949(outValue)
			exec getStringSetterMethod(objectName, attrName, value1)

#-------------------------------------------------------------------------------
# def getStringDefineMethod(objectName, methodName):
#
# 아래와 예시와 같은 함수 및 문장을 동적으로 정의한다
#--- 예시 ---
# def setWriter(aClassInfo,writer):
#         aClassInfo.writer = writer
# def getWriter(aClassInfo):
#         return aClassInfo.writer
#
# aClassInfo.setWriter=setWriter
# aClassInfo.getWriter=getWriter

def getStringDefineMethod(objectName, methodName):
	defineMethodString = '''
def set%(MethodNameUpperIndex0)s(%(objectName)s,%(methodName)s):
	%(objectName)s.%(methodName)s = %(methodName)s
def get%(MethodNameUpperIndex0)s(%(objectName)s):
	return %(objectName)s.%(methodName)s

%(objectName)s.set%(MethodNameUpperIndex0)s=set%(MethodNameUpperIndex0)s
%(objectName)s.get%(MethodNameUpperIndex0)s=get%(MethodNameUpperIndex0)s
''' % {'methodName': methodName, \
		'MethodNameUpperIndex0': ComUtil.getUpperNameIndex0(methodName), \
		'objectName': objectName }
	return defineMethodString
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#아래와 예시와 같은 문장을 동적으로 정의한다
#--- 예시 ---
# aClassInfo.setWriter(aClassInfo, '작성자 : 홍길동')
# aClassInfo.setWriteDate(aClassInfo, '작성일 : 2000.10.01')
# aClassInfo.setSubSystemName(aClassInfo, '서브시스템명 : 자재관리시스템')

def getStringSetterMethod(objectName, attrName, value1):
	defineMethodString = '''%(objectName)s.set%(MethodNameUpperIndex0)s(%(objectName)s, '%(value1)s')''' \
	% {'MethodNameUpperIndex0': ComUtil.getUpperNameIndex0(attrName),\
	'objectName': objectName,'attrName': attrName, 'value1': value1}
	#print defineMethodString
	return defineMethodString
#-------------------------------------------------------------------------------

