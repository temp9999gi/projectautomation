# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
import ExcelReader
import CrudAccessValue
import CrudMatrixDao
"""
일단 해야 하는 것은 뭐냐면?
crud를 주면 c를 반환한다.
rud를 주면 D
"""
def getKeyCrud(crudGubun):
	if crudGubun.find('C')>=0:
		return 'C'
	if crudGubun.find('D')>=0:
		return 'D'
	if crudGubun.find('U')>=0:
		return 'U'
	if crudGubun.find('R')>=0:
		return 'R'

	return crudGubun #에러 상황이다.

class CrudMatrixApp:
	def __init__(self):
		self.aCrudMatrixDao = CrudMatrixDao.CrudMatrixDao()

	def insertCrudMatrixAction(self,inFile, inSheetName, inColCount):
		aCrudAccessValue = CrudAccessValue.CrudAccessValue()
		
		aExcelReader= ExcelReader.ExcelReader(inFile, inSheetName, inColCount)
		voList=[]
		for row  in aExcelReader.getListFromSheet():
			usecaseName, crudGubunOriginal, className, commonYn = row[0:4]
			crudGubun = getKeyCrud(crudGubunOriginal)
			accessValue = aCrudAccessValue.getAccessValue(crudGubun)
			#print
			xx=(usecaseName, crudGubun, className, crudGubunOriginal, accessValue,\
				commonYn)
			voList.append(xx)
			
		self.aCrudMatrixDao.insertCrudMatrixAction(voList)
		print "(MSG)Ok"

if __name__ == '__main__':
	inFile='C:/_projectautomation/source/analysisSupport/identifyComponent/input/inputData/input.xls'
	inSheetName='input'
	inColCount = 4 #inSheet의 칼럼수
	aCrudMatrixApp= CrudMatrixApp()
	aCrudMatrixApp.insertCrudMatrixAction(inFile, inSheetName, inColCount)


	