# -*- coding: utf-8 -*-
#
# generates xml files from Word
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start

from WordSuperType import *

from Constants import Constants
CONS = Constants()

from path import path
import sys;sys.path.append("C://_projectautomation/source/common")

def main():
	CONS.setConstant(sys.argv[0])
	
	import ReaderAppEnv
	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)

	if aReaderAppEnv.appEnvData["isClassDefinition"]=='True':
		deliverableType = 'Class'
		tmplFileName = CONS.INPUT_CLASS_WRD_TOTAL_TEMPLATE
		outputfile = CONS.OUTPUT_CLASS_WRD_TOTAL


	if aReaderAppEnv.appEnvData["isInterfaceDefinition"]=='True':
		deliverableType = 'Interface'
		tmplFileName = CONS.INPUT_INTERFACE_WRD_TOTAL_TEMPLATE
		outputfile = CONS.OUTPUT_INTERFACE_WRD_TOTAL
		
	
	#print tmplFileName, outputfile
	ComUtil.copyTemplate(tmplFileName, outputfile)
		
	aWordHelper=WordSuperType()

	aWordHelper.openWord(outputfile)
	
	app = aWordHelper.getApp()

	aWordHelper.setVisible(True)

	activeDoc=app.ActiveDocument
	activeDoc.Select()

	aSelection = app.Selection
	aSelection.EndKey()
	insertFileAction(aSelection)
	
def insertFileAction(aSelection):
	docList = []
	inPath = CONS.OUT_DIR_TEMP + '/'
	p = path(inPath)
	for aFile in os.listdir(p):
	    if aFile.endswith('.doc'):
	        docList.append(aFile)
	        aSelection.InsertFile(inPath + aFile)
	        aSelection.InsertBreak()
	#print docList
        
if __name__ == '__main__':
	main()

	import message.message as message
	inMessage ="산출물 생성 완료!\ngood luck!"
	inTitle='정보'
	message.showInfo(inTitle, inMessage)

