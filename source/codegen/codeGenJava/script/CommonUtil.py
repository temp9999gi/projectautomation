# -*- coding: utf-8 -*-
import string
from xml.dom.minidom import *
try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
def capitalize1(inText):
	return string.capitalize(inText)
def utf8ToEucKr(inUtf8):
	return unicode(inUtf8, 'utf-8').encode('euc-kr')   # utf-8 --> euc-kr
def getDomEncodeUtf8(xmlFile):
	s = open(xmlFile).read()  # 전체 문자열을 읽어낸다.
	s = unicode(s, 'euc-kr').encode('utf-8')  # euc-kr ---> utf-8 변환
	doc = parseString(s)         # 문자열을 이용한 파싱
	return doc

# start
import re
class CommonUtil:
	def getJavaFieldName(self, inStr):
		out = re.sub( r'_(\w)', self.subRepl, inStr.lower() ) # sub( pattern, repl, string[, count])
		return out.replace('_', '')

	def getClassName(self, inStr):
		ss = re.sub( r'_(\w)', self.subRepl, inStr.lower() ) # sub( pattern, repl, string[, count])
		out = ss[0].upper() + ss[1:]
		return out.replace('_', '')

	def subRepl(self, match1):
		# print 'match1: [',match1,']\n'
		# print 'match1.group(0): [', match1.group(0),']\n'
		s1 = match1.group(0)
		return '%s' % s1.upper()

	def generateCode(self, objectArray, templateFileName):
		from Cheetah.Template import Template
		outSource = Template(file = templateFileName, searchList = [objectArray])
		return outSource

	def writeFile(self, fileName, aTemplate):
		new_file = file(fileName, 'w+')
		new_file.write('%s' % aTemplate)
		new_file.close()
		print '(MSG) file %s created' % fileName

	def printPythonComError(self,hr, msg, exc, arg):
		print "The Excel call failed with code %d: %s" % (hr, msg)
		if exc is None:
			print "There is no extended error information"
		else:
			wcode, source, text, helpFile, helpId, scode = exc
			print "The source of the error is", source
			print "The error message is", text
			print "More info can be found in %s (id=%d)" % (helpFile, helpId)

	def getUpperNameIndex0(self, inString):
		return string.upper(inString[0]) + inString[1:]

	def getLowerNameIndex0(self, inString):
		return string.lower(inString[0]) + inString[1:]
