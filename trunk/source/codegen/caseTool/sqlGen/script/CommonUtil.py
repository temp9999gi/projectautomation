﻿# -*- coding: utf-8 -*-
# start
import string
from Cheetah.Template import Template
from xml.dom.minidom import *
import re

def getDomEncodeUtf8(xmlFile):
	s = open(xmlFile).read()  # 전체 문자열을 읽어낸다.
	s = unicode(s, 'euc-kr').encode('utf-8')  # euc-kr ---> utf-8 변환
	doc = parseString(s)         # 문자열을 이용한 파싱
	return doc

def encodeCp949(inStr):
	return inStr.encode('cp949')

		
class CommonUtil :

	def generateCode(self, objectArray, templateFileName):
		aTemplate = Template(file = templateFileName, searchList = [objectArray])
		return aTemplate	
	
	def writeFile(self, fileName, aTemplate):
		new_file = file(fileName, 'w+')
		new_file.write('%s' % aTemplate)
		new_file.close()

	def copyTemplate(self, srcfile, targetfile):
		import shutil
		#import sys
		shutil.copyfile(srcfile, targetfile)

	#---------------------------------------------------------------------------
	def getJavaFieldName(self, inStr):
		# sub( pattern, repl, string[, count])
		out = re.sub( r'_(\w)', self.subRepl, inStr.lower() ) 
		return out.replace('_', '')

	def getClassName(self, inStr):
		# sub( pattern, repl, string[, count])
		ss = re.sub( r'_(\w)', self.subRepl, inStr.lower() )
		out = ss[0].upper() + ss[1:]
		return out.replace('_', '')
	def subRepl(self, match1):
		# print 'match1: [',match1,']\n'
		# print 'match1.group(0): [', match1.group(0),']\n'
		s1 = match1.group(0)
		return '%s' % s1.upper()
	#---------------------------------------------------------------------------


	def getUpperNameIndex0(self, inString):
		return string.upper(inString[0]) + inString[1:]		
		
	def getLowerNameIndex0(self, inString):
		return string.lower(inString[0]) + inString[1:]
		
	def printPythonComError(self,hr, msg, exc, arg):
		print "The Excel call failed with code %d: %s" % (hr, msg)
		if exc is None:
			print "There is no extended error information"
		else:
			wcode, source, text, helpFile, helpId, scode = exc
			print "The source of the error is", source
			print "The error message is", text
			print "More info can be found in %s (id=%d)" % (helpFile, helpId)
		