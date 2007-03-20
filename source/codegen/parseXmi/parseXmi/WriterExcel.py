# -*- coding: utf-8 -*-
# 
# generates xml files from Excel
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
from ModelInfo import *
from Constants import *
import CommonUtil as comUtil
#from CommonUtil import *
import ExcelHelper

CONS = Constants()
class WriterExcel:
	def writeExcelClassDefinition(self, aModelInfo):
		aCommonUtil = comUtil.CommonUtil()
		aCommonUtil.copyTemplate(CONS.INPUT_CLASS_EXCEL_TEMPLATE , CONS.OUTPUT_CLASS_EXCEL)
		
		aExcelHelper = ExcelHelper.ExcelHelperClassDefiniton()
		
		aExcelHelper.writeExcelCoreClassDef(aModelInfo, aExcelHelper, CONS.OUTPUT_CLASS_EXCEL)

	def writeExcelClassList(self, aModelInfo):
		aCommonUtil = comUtil.CommonUtil()

		aCommonUtil.copyTemplate(CONS.INPUT_CLASS_LIST_EXCEL_TEMPLATE , \
			CONS.OUTPUT_CLASS_LIST_EXCEL)

		aExcelHelper = ExcelHelper.ExcelHelperClassList()

		aExcelHelper.writeExcelCoreClassList(aModelInfo, aExcelHelper, CONS.OUTPUT_CLASS_LIST_EXCEL)


