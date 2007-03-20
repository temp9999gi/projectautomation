# -*- coding: utf-8 -*-
from voCommonUtil import *
from ClassInfo import *
import constants as CON
import sys

def Run():
	
	inXmlFile = CON.INPUT_DIR + sys.argv[1]
	
	aClassInfo = ClassInfo()
	aClassInfo = parseXml(aClassInfo, inXmlFile)

	fileName = CON.OUT_DIR + aClassInfo.className + '.java'
	
	aTemplate = generateCode(aClassInfo, CON.VO_TEMPLATE)
	
	writeFile(fileName, aTemplate)

if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		print "python ValueObjectMain.py Properties.xml"
		sys.exit()	
	
	Run()
	