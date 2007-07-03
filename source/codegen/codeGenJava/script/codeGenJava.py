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
from DaoMethodInfoDao import *

class WriteJavaFromDb:
	def __init__(self):
		inPath = sys.argv[0]
		self.CONS = Constants(inPath)
		#dataSource='C://_projectautomation/source/mdb/MyDB.mdb'
		self.dataSource = sys.argv[1]

	def genDomainObject(self):
		aTableInfoDao = TableInfoDao(self.dataSource, self.CONS)
		cl = aTableInfoDao.getKlassListAction()
		
		aKlassInfoList = KlassInfoList()
		aKlassInfoList.setKlassList(cl)

		aCommonUtil = CommonUtil()
		for aKlass in aKlassInfoList.klassList:
			##JAVA_DOMAIN
			outSource = aCommonUtil.generateCode(aKlass, str(self.CONS.JAVA_DOMAIN_TEMPLATE))
			fileName = self.CONS.DOMAIN_OUT_DIR / aKlass.klassName + '.java'
			aCommonUtil.writeFile(fileName, outSource)

	def genDao(self):
		aDao = DaoMethodInfoDao(self.dataSource, self.CONS)
		klassList = aDao.getKlassListAction()

		aCommonUtil = CommonUtil()
		for aKlass in klassList:
			##DAO소스생성
			outSource = aCommonUtil.generateCode(aKlass, str(self.CONS.DAO_TEMPLATE))
			fileName = self.CONS.DAO_OUT_DIR / 'SqlMap'+aKlass.klassName + 'Dao.java'
			#print fileName
			aCommonUtil.writeFile(fileName, outSource)

		for aKlass in klassList:
			##IDAO소스생성
			outSource = aCommonUtil.generateCode(aKlass, str(self.CONS.IDAO_TEMPLATE))
			fileName = self.CONS.IDAO_OUT_DIR / aKlass.klassName + 'Dao.java'
			#print fileName
			aCommonUtil.writeFile(fileName, outSource)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "USAGE: WriteJavaFromDb.py input"
		sys.exit()
	#WriteJavaFromDb().genDomainObject()
	WriteJavaFromDb().genDao()
	