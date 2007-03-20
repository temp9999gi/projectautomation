# -*- coding: utf-8 -*-
# start
import sys
from ClassInfo import *
from XmlParser import *
from CommonUtil import *
from Constants import *

class GeneratorMgr :
	def Run(self):
		aClassInfo = ClassInfo()
		aCommonUtil = CommonUtil()
		aXmlParser = XmlParser()
		CONS = Constants()
		
		inXmlFile = CONS.INPUT_DIR + sys.argv[1]
		aXmlParser.parseXml(aClassInfo, inXmlFile)
		outSource = aCommonUtil.generateCode(aClassInfo, CONS.VO_TEMPLATE)
		outFileName = CONS.OUT_DIR + aClassInfo.className + '.java'
		aCommonUtil.writeFile(outFileName, outSource)
		print '(END) file %s created' % outFileName
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python voMain.py Account.xml"
		sys.exit()
	GeneratorMgr().Run()
	