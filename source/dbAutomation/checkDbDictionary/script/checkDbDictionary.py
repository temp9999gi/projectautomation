# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import sys;sys.path.append("C://_projectautomation/source/common")
import utils

import excelLib.ExcelHelperClassList as ExcelHelperClassList
from excelLib.ExcelReader import *
from excelLib.KlassInfoList import *

from Constants import *
from CommonUtil import *
import ReaderAppEnv

from CheckDbDictionaryDao import CheckDbDictionaryDao
from TbNameKorAndNullDao import TbNameKorAndNullDao

CONS = Constants()
##def getList(cursor):
##	voList = []
##	for row in cursor:
##		voList.append(row)
##	return voList
class WriterApp:
	def common1(self,aReaderAppEnv, dataSource):
		inFile = path(sys.argv[1])
#		print inFile
		aExcelReader = ExcelReader(inFile, CONS)
		self.aKlassInfoList = KlassInfoList()

		cl = aExcelReader.getKlassListFromExcel()
		self.aKlassInfoList.setKlassList(cl)
		self.aKlassInfoList.setReaderAppEnv(aReaderAppEnv)

	def insertTblAndColAction(self,aReaderAppEnv, dataSource):
		self.common1(aReaderAppEnv, dataSource)
		
		# db에 저장한다.
		aCheckDbDictionaryDao = CheckDbDictionaryDao(dataSource)

		tableList = self.aKlassInfoList.getKlassList()
		aCheckDbDictionaryDao.deleteTblAndColAction()

		aCheckDbDictionaryDao.insertTblAndColAction(tableList)

	def writeAction(self,aReaderAppEnv, dataSource):

		self.common1(aReaderAppEnv, dataSource)
		
		# db에 저장한다.
		aCheckDbDictionaryDao = CheckDbDictionaryDao(dataSource)
		
		tableList = self.aKlassInfoList.getKlassList()
		aCheckDbDictionaryDao.deleteAllAction()

		aCheckDbDictionaryDao.insertTblAndColAndElWordAction(tableList)

		#얘는 뭐하는 애냐면?
		#영문칼럼.영문낱단어에 대응하는 용어사전.한글명과
		#대응하는 한글명이 없는 경우 "|영문낱단어"를 가진 칼럼을 찾는다.
		#TbNameKorAndNull테이블에 등록한다.
		aTbNameKorAndNullDao = TbNameKorAndNullDao(dataSource)
		voList = aTbNameKorAndNullDao.selectNameKorAndNullAction()
		aTbNameKorAndNullDao.insertTbNameKorAndNullAction(voList)

		print "(MSG)insert: Ok"

def run():
	inPath = sys.argv[0]
	CONS.setConstant(inPath)

	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)
	aWriterApp = WriterApp()
	#dataSource='C://_projectautomation/source/dbAutomation/checkDbDictionary2/db/MyDB.mdb'
	dataSource = sys.argv[2]
	aWriterApp.writeAction(aReaderAppEnv, dataSource)
	print "(MSG) OK"

def run2():
	inPath = sys.argv[0]
	CONS.setConstant(inPath)

	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)
	aWriterApp = WriterApp()
	#dataSource='C://_projectautomation/source/dbAutomation/checkDbDictionary2/db/MyDB.mdb'
	dataSource = sys.argv[2]
	aWriterApp.insertTblAndColAction(aReaderAppEnv, dataSource)

	print "(MSG) Insert OK"

	
if __name__ == '__main__':
 	if len(sys.argv) < 2:
 		print "USAGE: WriterApp.py input.xls"
 		sys.exit()

	run()

