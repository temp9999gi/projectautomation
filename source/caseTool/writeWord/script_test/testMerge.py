# -*- coding: utf-8 -*-
#
# generates xml files from Word
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import sys;sys.path.append("C://_projectautomation/source/caseTool/writeWord/script")
from WordSuperType import *




#-----------------------------------
def getCopy(wh2):
	#wh2=WordSuperType()
	xx='C://_projectautomation/source/caseTool/writeWord/script_test/outputClassDefinition1.doc'
	wh2.openWord(xx)
	app2 = wh2.getApp()

	wh2.setVisible(True)

	activeDoc2=app2.ActiveDocument

	activeDoc2.Select()
	#app2.Selection.InsertBreak()
	#app2.Selection.WholeStory
	out = app2.Selection.Copy()
	


def main():
	xx='C://_projectautomation/source/caseTool/writeWord/script_test/main.doc'
	aWordHelper=WordSuperType()
	aWordHelper.openWord(xx)
	app = aWordHelper.getApp()

	aWordHelper.setVisible(True)

	activeDoc=app.ActiveDocument

	activeDoc.Select()

	#out = getCopy(aWordHelper)
	aSelection = app.Selection
	aSelection.EndKey()
	insertFileAction(aSelection)

##	fileName='C://_projectautomation/source/caseTool/writeWord/script_test/outputClassDefinition1.doc'
##	insertFile(aSelection, fileName)
##	aSelection.InsertBreak()
##
##	fileName='C://_projectautomation/source/caseTool/writeWord/script_test/outputClassDefinition2.doc'
##	insertFile(aSelection, fileName)
	
def insertFile(aSelection, fileName):
	aSelection.InsertFile(fileName)

from path import path
def insertFileAction(aSelection):
	docList = []
	inPath ='C://_projectautomation/source/caseTool/writeWord/script_test/temp/'
	p = path(inPath)
	for aFile in os.listdir(p):
	    if aFile.endswith('.doc'):
	        docList.append(aFile)
	        #print inPath+aFile
	        aSelection.InsertFile(inPath + aFile)
	        aSelection.InsertBreak()
	print docList
        

main()
#insertFile1()