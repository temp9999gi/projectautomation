# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import sys;sys.path.append("C://_projectautomation/source/common")
import logging
import utils
# import shutil

import ExcelHelperClassList
from KlassInfoList import *
from ExcelReader import *
from Constants import *
from CommonUtil import *
import ReaderAppEnv

from myDao import MyDao
from MyDao2 import MyDao2

CONS = Constants()
def getList(cursor):
	voList = []
	for row in cursor:
		voList.append(row)
	return voList
class WriterApp:
	def writeAction(self,aReaderAppEnv):

		inFile = CONS.INPUT_DATA_DIR / sys.argv[1]
		aExcelReader = ExcelReader(inFile, CONS)
		self.aKlassInfoList = KlassInfoList()

		xx = aExcelReader.getKlassListFromExcel()
		self.aKlassInfoList.setKlassList(xx)
		self.aKlassInfoList.setReaderAppEnv(aReaderAppEnv)
		
		# db에 저장한다.
		aDao = MyDao()
		tableList = self.aKlassInfoList.getKlassList()
		aDao.deleteAllAction()
		
		aDao.setVo(tableList)
		aDao.insertAction()
		
		#얘는 뭐하는 애냐면?
		#영문칼럼.영문낱단어에 대응하는 용어사전.한글명과
		#대응하는 한글명이 없는 경우 "|영문낱단어"를 가진 칼럼을 찾는다.
		#테이블을 생성한다.
		aMyDao2 = MyDao2()
		sql=aMyDao2.selectNameKorAndNull()
		voList = aMyDao2.selectAction(sql)
		aDao.insertTbNameKorAndNullAction(voList)

		log.info('---def writeAction---')
		log.info("(MSG)insert: Ok")
		print "(MSG)insert: Ok"


if __name__ == '__main__':
 	if len(sys.argv) < 2:
 		print "USAGE: WriterApp.py input.xls"
 		sys.exit()

	inPath = sys.argv[0]
	CONS.setConstant(inPath)

	utils.initLog(CONS.LOG_FILE)
	utils.addConsoleLogging()
	log = logging.getLogger('ExcelMain')

	#log.debug("argv0: ['%s'], attrs.getValue(attrName): ['%s']",attrName, attrs.getValue(attrName))
	log.debug("---input argument---")
	log.debug("sys.argv[0]: ['%s']",sys.argv[0])
	log.debug("sys.argv[1]: ['%s']",sys.argv[1])
	

	aReaderAppEnv = ReaderAppEnv.ReaderAppEnv()
	aReaderAppEnv.saveAppEnvInfo(CONS.INPUT_APP_ENV_XML)
	aWriterApp = WriterApp()
	aWriterApp.writeAction(aReaderAppEnv)

