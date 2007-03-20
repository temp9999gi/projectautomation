# -*- coding: utf-8 -*-
import sys
#from Constants import *
# start
import CrudMatrixDao

class CrudAccessValue:
	def __init__(self):
		self.crudAccessValue = {}
		self.__run()
		
	def __run(self):
		aCrudMatrixDao = CrudMatrixDao.CrudMatrixDao()
		# print aCrudMatrixDao.selectCrudAccessValueAction()

		for row in aCrudMatrixDao.selectCrudAccessValueAction():
			crudGubun = row[0]; accessValue= row[1]
			self.crudAccessValue[crudGubun] = accessValue
			
	def getAccessValue(self, crudGubun):
		
		try:
			out = self.crudAccessValue[crudGubun]
		except KeyError:
			out = crudGubun
			
		return out
	
if __name__ == "__main__":
	aCrudAccessValue = CrudAccessValue()
	print aCrudAccessValue.getAccessValue('C')

