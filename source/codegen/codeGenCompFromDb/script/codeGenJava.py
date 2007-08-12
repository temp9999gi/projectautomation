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
from dao.TableInfoDao import *

from system.QueryXmlApp import *
from system.ServiceXmlApp import *
from system.ActivityClassApp import *
from system.FieldApp import *
from SqlMaker import *


aCommonUtil = CommonUtil()

class WriteJavaFromDb:
	def __init__(self):
		inPath = sys.argv[0]
		self.CONS = Constants(inPath)
		self.mdbFilePath = sys.argv[1]
    #---------------------------------------------------------------------------
  
	#dao단위로 ActivityClass를 생성한다.
	#dao단위는 패키지가 된다.
	def genActivityClass(self):
		
		aFieldApp = self.getFieldApp()
		
		aTableInfoDao = TableInfoDao(self.mdbFilePath, self.CONS)
		rs = aTableInfoDao.getKlassListForActivityClassAction()
		aActivityClassApp = ActivityClassApp(self.CONS, aFieldApp)
		cl = aActivityClassApp.getKlassList(rs)


		aKlassInfoList = KlassInfoList()
		aKlassInfoList.setKlassList(cl)

		for aActivityClassInfo in aKlassInfoList.klassList:
			for aTableInfo in aActivityClassInfo.tableList:
				for aMethod in aTableInfo.methodList:
					aCommonUtil.myMkdir(self.CONS.ACTIVITY_CLASS_OUT_DIR / aActivityClassInfo.packageId)
					templateName = self.CONS.TEMPLATE_DIR / self.getTemplate(aMethod.crudGubun)
					outSource = aCommonUtil.generateCode(aMethod, str(templateName))
					fileName = self.CONS.ACTIVITY_CLASS_OUT_DIR / aActivityClassInfo.packageId / aMethod.classId + '.java'
					aCommonUtil.writeFile(fileName, outSource)

	def getTemplate(self, inCrudGubun):
		
		if inCrudGubun == 'find':
			templateName='ACTIVITY_CLASS_TEMPLATE_R.tmpl'

		if inCrudGubun == 'add':
			templateName='ACTIVITY_CLASS_TEMPLATE_C.tmpl'

		if inCrudGubun == 'update':
			templateName='ACTIVITY_CLASS_TEMPLATE_U.tmpl'

		if inCrudGubun == 'delete':
			templateName='ACTIVITY_CLASS_TEMPLATE_D.tmpl'
			
		if inCrudGubun == 'save':
			templateName='ACTIVITY_CLASS_TEMPLATE_S.tmpl'
		return templateName


	def genServiceXmlInfo(self):
		aTableInfoDao = TableInfoDao(self.mdbFilePath, self.CONS)
		rs = aTableInfoDao.getKlassListForServiceXmlInfoAction()

		aServiceXmlApp = ServiceXmlApp(self.CONS)
		cl = aServiceXmlApp.getKlassList(rs)


		aKlassInfoList = KlassInfoList()
		aKlassInfoList.setKlassList(cl)

		aCommonUtil = CommonUtil()
		for aServiceXmlInfo in aKlassInfoList.klassList:
			outSource = aCommonUtil.generateCode(aServiceXmlInfo, str(self.CONS.SERVICE_XML_TEMPLATE))
			fileName = self.CONS.SERVICE_XML_OUT_DIR / aServiceXmlInfo.service_Xml_Id + '-service.xml'
			aCommonUtil.writeFile(fileName, outSource)

	def getFieldApp(self):
		aTableInfoDao = TableInfoDao(self.mdbFilePath, self.CONS)
		rs1 = aTableInfoDao.getKlassListForCreateFieldAction()

		aFieldApp = FieldApp(self.CONS)
		cl1 = aFieldApp.getKlassList(rs1)
		return aFieldApp

	def genQueryXml(self):
		aFieldApp = self.getFieldApp()
		aTableInfoDao = TableInfoDao(self.mdbFilePath, self.CONS)
		rs = aTableInfoDao.getKlassListForActivityClassAction()

		aQueryXmlApp = QueryXmlApp(self.CONS)
		cl = aQueryXmlApp.getKlassList(rs, aFieldApp)


		aKlassInfoList = KlassInfoList()
		aKlassInfoList.setKlassList(cl)
					
		for aQueryXmlInfo in aKlassInfoList.klassList:
			outSource = aCommonUtil.generateCode(aQueryXmlInfo, str(self.CONS.QUERY_XML_TEMPLATE))
			fileName = self.CONS.QUERY_XML_OUT_DIR / aQueryXmlInfo.classId + '-query.xml'
			aCommonUtil.writeFile(fileName, outSource)

	def saveActivityClassToDb(self):
		aFieldApp = self.getFieldApp()

		aTableInfoDao = TableInfoDao(self.mdbFilePath, self.CONS)
		rs = aTableInfoDao.getKlassListForActivityClassAction()
		aActivityClassApp = ActivityClassApp(self.CONS, aFieldApp)
		cl = aActivityClassApp.getKlassList(rs)

		aKlassInfoList = KlassInfoList()
		aKlassInfoList.setKlassList(cl)

		for aActivityClassInfo in aKlassInfoList.klassList:
			for aTableInfo in aActivityClassInfo.tableList:
				for aMethod in aTableInfo.methodList:
					#aMethod.setTable(aTableInfo) #aMethod와 Table Info 관계 설정
					aTableInfoDao.insertMethodInfoService(aMethod)



		
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "USAGE: codeGenJava.py C:/_projectautomation/source/codegen/codeGenJava/db/MyDB.mdb"
		sys.exit()
	WriteJavaFromDb().genActivityClass()
	#WriteJavaFromDb().genServiceXmlInfo()
	#WriteJavaFromDb().genQueryXml()

	#WriteJavaFromDb().saveActivityClassToDb()
	
	