# -*- coding: utf-8 -*-

from classDefinition import *
from iBaitsXMLParser import *
# from commonUtil import *
import commonUtil
from Constants import *


import sys
 
class Run :

	aIBatisXMLParser = IBatisXMLParser()

	aSqlMaster = aIBatisXMLParser.doParse()

	##DAO소스생성
	#file_name = DAO_OUT_DIR + aSqlMaster.className + DAO_SUFFIX
	#aSourceCdoe = commonUtil.generateCode(aSqlMaster, DAO_TEMPLATE)
	#writeFile(file_name, aSourceCdoe)

	##IDAO소스생성
	# file_name = IDAO_OUT_DIR + aSqlMaster.className + IDAO_SUFFIX
	# aSourceCdoe = commonUtil.generateCode(aSqlMaster, IDAO_TEMPLATE)
	# writeFile(file_name, aSourceCdoe)

	#Service 소스생성
	file_name = SERVICE_OUT_DIR + aSqlMaster.className + SERVICE_SUFFIX
	aSourceCdoe = commonUtil.generateCode(aSqlMaster, SERVICE_TEMPLATE)
	writeFile(file_name, aSourceCdoe)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python genMain.py Class.xml"
		sys.exit()

	Run()