# -*- coding: utf-8 -*-
#
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
# to Do

import sys
from KlassInfoList import *

from Constants import *
from CommonUtil import *
from TableInfoDao import *

class WriteJavaFromDb:
	def Run(self):
		inPath = sys.argv[0]
		CONS = Constants(inPath)

		#dataSource='C://_projectautomation/source/mdb/MyDB.mdb'
		dataSource = sys.argv[1]

		aTableInfoDao = TableInfoDao(dataSource, CONS)
		cl = aTableInfoDao.getKlassListAction()
		
		aKlassInfoList = KlassInfoList()
		aKlassInfoList.setKlassList(cl)

		aCommonUtil = CommonUtil()
		for aKlass in aKlassInfoList.klassList:
			##JAVA_DOMAIN
##			outSource = aCommonUtil.generateCode(aKlass, str(CONS.JAVA_DOMAIN_TEMPLATE))
##			fileName = CONS.OUT_DIR / aKlass.klassName + '.java'
##			aCommonUtil.writeFile(fileName, outSource)

			##DAO소스생성
			outSource = aCommonUtil.generateCode(aKlass, str(CONS.DAO_TEMPLATE))
			fileName = CONS.DAO_OUT_DIR / 'SqlMap'+aKlass.klassName + 'Dao.java'
			print fileName
			aCommonUtil.writeFile(fileName, outSource)

			##DAO소스생성
			#file_name = DAO_OUT_DIR + aSqlMaster.className + DAO_SUFFIX
			#aSourceCdoe = commonUtil.generateCode(aSqlMaster, DAO_TEMPLATE)
			#writeFile(file_name, aSourceCdoe)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "USAGE: WriteJavaFromDb.py input.xls"
		sys.exit()
	WriteJavaFromDb().Run()
	