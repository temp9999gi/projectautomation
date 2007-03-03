# -*- coding: utf-8 -*-
from  string import *
import re
import csv

#from classDef import *
from myDao import *
from WriterExcelMain import *

class columnVo:
	pass

def myWrite(voList):
	aWriterExcelMain = WriterExcelMain()
	aWriterExcelMain.run(voList)
	print voList


def Run():

	aDao = MyDao()
##	aDao.deleteAll()
##	aDao.setVo(tableList)
##	aDao.insertTable()
##	aDao.insertColumn()

	#print '------ErrorType:selectTypeErrorAndColumnKorIsEqual-----'
	#101한글명같고 타입다른것
	cursor = aDao.selectTypeErrorAndColumnKorIsEqual()
	voList = []
	for row in cursor:
		voList.append(row)
		#print no1, columnKor, columnEng, colType, tableEng, tableKR, bizName
	cursor.Close()
	myWrite(voList)
	
	
	#print '------ErrorLength:selectLengthErrorAndColumnKorIsEqual-----'
	#102한글명같고 길이다른것
	cursor = aDao.selectLengthErrorAndColumnKorIsEqual()
	for row in cursor:
		##print row
		no1, columnKor, columnEng, length, tableEng, tableKR, bizName = row
		#print no1, columnKor, columnEng, length, tableEng, tableKR, bizName

	cursor.Close()

	#print '------Error ColumnEngError:selectColumnEngErrorAndColumnKorIsEqual-----'
	cursor = aDao.selectColumnEngErrorAndColumnKorIsEqual()
	for row in cursor:
		no1, columnKor, columnEng, tableEng, tableKR, bizName = row
		#print no1, columnKor, columnEng, tableEng, tableKR, bizName

	cursor.Close()

	#print '------Error TypeError:selectTypeErrorAndColumnEngIsEqual-----'
	cursor = aDao.selectTypeErrorAndColumnEngIsEqual()
	for row in cursor:
		no1, columnKor, columnEng, colType, tableEng, tableKR, bizName = row
		#print no1, columnKor, columnEng, colType, tableEng, tableKR, bizName

	cursor.Close()
	
	#print '------Error LengthError:selectLengthErrorAndColumnEngIsEqual-----'
	cursor = aDao.selectLengthErrorAndColumnEngIsEqual()
	for row in cursor:
		no1, columnKor, columnEng, length, tableEng, tableKR, bizName = row
		#print no1, columnKor, columnEng, length, tableEng, tableKR, bizName

	cursor.Close()

	#print '------Error ColumnKor Error:selectColumnKorErrorAndColumnEngIsEqual-----'
	cursor = aDao.selectColumnKorErrorAndColumnEngIsEqual()
	for row in cursor:
		no1, columnKor, columnEng, tableEng, tableKR, bizName = row
		#print no1, columnKor, columnEng, tableEng, tableKR, bizName

	cursor.Close()
	
if __name__ == '__main__':
	# inXmlFile = './input/'+sys.argv[1]
	Run()



