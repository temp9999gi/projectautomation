# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
# to Do
# 끝났으면 끝났다고 메시지를 보내야 하는 것 아니니..
import sys
from KlassInfoList import *
from ExcelReader import *
from Constants import *
from CommonUtil import *
class WriteJavaFromExcel:
	def Run(self):
		inPath = sys.argv[0]
		CONS = Constants(inPath)
		inFile = CONS.INPUT_DATA_DIR / sys.argv[1]
		aExcelReader = ExcelReader(inFile)
		aKlassInfoList = KlassInfoList()
		aKlassInfoList.setKlassList(aExcelReader.getKlassListFromExcel())

		aCommonUtil = CommonUtil()
		for aKlass in aKlassInfoList.klassList:
			outSource = aCommonUtil.generateCode(aKlass, str(CONS.JAVA_ANALYSIS_TEMPLATE))
			fileName = CONS.OUT_DIR / aKlass.klassName + '.java'
			aCommonUtil.writeFile(fileName, outSource)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "USAGE: WriteJavaFromExcel.py input.xls"
		sys.exit()
	WriteJavaFromExcel().Run()