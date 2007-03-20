# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
from win32com.client import Dispatch
import pythoncom

from CommonUtil import CommonUtil

ComUtil = CommonUtil()


import FinderAppDao
import AccessUtil

data_source ='C://_projectautomation/source/analysisSupport/identifyComponent/db/Component.mdb'

class FinderApp:
	def __init__(self):
		pass

	def selectCrudMatrixAction(self):
		self.aFinderAppDao = FinderAppDao.FinderAppDao()
		print self.aFinderAppDao.selectCrudMatrixAction()

	def openAccessQueryAction(self):
		aAccessUtil = AccessUtil.AccessUtil(data_source)

		queryName='q_findComponent3'
		view = 0
		aAccessUtil.openAccessQueryAction(queryName, view)

	def openAccessFormAction(self):
		aAccessUtil = AccessUtil.AccessUtil(data_source)

		formName='frmComponent'
		view = 0
		aAccessUtil.openAccessFormAction(formName, view)


if __name__ == '__main__':
	aFinderApp= FinderApp()
	aFinderApp.openAccessFormAction()
	#aFinderApp.openAccessQueryAction()
	#aFinderApp.selectCrudMatrixAction()
	#print aFinderApp.getListFromSheet()
