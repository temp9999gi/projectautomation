# -*- coding: utf-8 -*-
from  string import *
import re
import csv

#from classDef import *
from myDao import MyDao
from WriterExcelMain import *

class columnVo:
	pass

def writeAtion(aWriterExcelMain, voList,title,inSheetName):
	aWriterExcelMain.writeSheetAtion(voList,title,inSheetName)
# 	print voList
	
def getList(cursor):
	voList = []
	for row in cursor:
		voList.append(row)
	return voList
	
def Run():
	dataSource= sys.argv[1]
	
	aDao = MyDao(dataSource)
##	aDao.deleteAll()
##	aDao.setVo(tableList)
##	aDao.insertTable()
##	aDao.insertColumn()
	aWriterExcelMain = WriterExcelMain()
	#print '------ErrorType:selectTypeErrorAndColumnKorIsEqual-----'
	#101한글명같고 타입다른것
	cursor = aDao.selectTypeErrorAndColumnKorIsEqual()
	voList = getList(cursor)
	cursor.Close()
	title = ('num', 'columnKor', 'columnEng', 'colType', 'tableEng', \
		'tableKR', 'bizName')
	inSheetName='101'
	writeAtion(aWriterExcelMain,voList,title,inSheetName)
	
	
	#print '------ErrorLength:selectLengthErrorAndColumnKorIsEqual-----'
	#102한글명같고 길이다른것
	cursor = aDao.selectLengthErrorAndColumnKorIsEqual()
	voList = getList(cursor)
	cursor.Close()
	title = ('num', 'columnKor', 'columnEng', 'length', 'tableEng', \
		'tableKR', 'bizName')
	inSheetName='102'
	writeAtion(aWriterExcelMain,voList,title,inSheetName)

	
	#print '------Error ColumnEngError:selectColumnEngErrorAndColumnKorIsEqual-----'
	#103한글명같고 영문명다른것
	cursor = aDao.selectColumnEngErrorAndColumnKorIsEqual()
	voList = getList(cursor)
	cursor.Close()
	#no1, columnKor, columnEng, tableEng, tableKR, bizName
	title = ('num', 'columnKor', 'columnEng', 'tableEng', \
		'tableKR', 'bizName')
	inSheetName='103'
	writeAtion(aWriterExcelMain,voList,title,inSheetName)

	#print '------Error TypeError:selectTypeErrorAndColumnEngIsEqual-----'
	#201영문명같고 타입다른것
	cursor = aDao.selectTypeErrorAndColumnEngIsEqual()
	voList = getList(cursor)
	cursor.Close()
	#no1, columnKor, columnEng, type1, tableEng, tableKR, remark AS bizName
	title = ('num', 'columnKor', 'columnEng', 'type', 'tableEng', \
		'tableKR', 'bizName')
	inSheetName='201'
	writeAtion(aWriterExcelMain,voList,title,inSheetName)
	
	#print '------Error LengthError:selectLengthErrorAndColumnEngIsEqual-----'
	#202영문명같고 길이다른것
	cursor = aDao.selectLengthErrorAndColumnEngIsEqual()
	voList = getList(cursor)
	cursor.Close()
	title = ('num', 'columnKor', 'columnEng', 'length', 'tableEng', \
		'tableKR', 'bizName')
	inSheetName='202'
	writeAtion(aWriterExcelMain,voList,title,inSheetName)

	#print '------Error ColumnKor Error:selectColumnKorErrorAndColumnEngIsEqual-----'
	#203영문명같고 한글명다른것
	cursor = aDao.selectColumnKorErrorAndColumnEngIsEqual()
	voList = getList(cursor)
	cursor.Close()
	#no1 AS [No], columnKor, columnEng, tableEng, tableKR, remark AS bizName
	title = ('num', 'columnKor', 'columnEng', 'tableEng', \
		'tableKR', 'bizName')
	inSheetName='203'
	writeAtion(aWriterExcelMain,voList,title,inSheetName)
	
	#---------------------------------------------------------------------------
	aWriterExcelMain.deleteSheet('templ')
	aWriterExcelMain.closeExcel()

	
	
	print "(MSG) OK"
	
if __name__ == '__main__':
	# inXmlFile = './input/'+sys.argv[1]
	Run()



