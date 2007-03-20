# -*- coding: utf-8 -*-
import sys
from ClassInfo import *
from XMLParser import *
import commonUtil
import constants as CON

class Run :
	
	aXMLParser = XMLParser()
	xmlFile = CON.INPUT_DIR + sys.argv[1]
	aClassInfo = aXMLParser.doParse(xmlFile)
	# ValueObject 
	file_name = CON.OUT_DIR + aClassInfo.className + '.java'
	aTemplate = commonUtil.getTemplate(aClassInfo, CON.VO_TEMPLATE)
	commonUtil.writeFile(file_name, aTemplate)

	# interface AccountDao
# 	VO_TEMPLATE = "./input/InterfaceDao.tmpl"
# 	file_name = './output/' + aClassInfo.className + 'Dao.java'	
# 	aTemplate = commonUtil.getTemplate(aClassInfo, VO_TEMPLATE)
# 	commonUtil.writeFile(file_name, aTemplate)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: python gen.py Class.xml"
		sys.exit()	

	Run()






