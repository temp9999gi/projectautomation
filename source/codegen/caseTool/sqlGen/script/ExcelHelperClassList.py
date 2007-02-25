# -*- coding: utf-8 -*-
from ExcelHelper import *
#-------------------------------------------------------------------------------
class ExcelHelperClassList(ExcelHelper):
	def __init__(self, CONS):
		ExcelHelper.__init__
		self.setCons(CONS)
		i = self.CONS.ATTRIBUTE_LIST_START_POSITION
		self.setCurrentRow(i)

	def writeExcelCoreClassList(self,aExcelHelper, outputfile):
		aModelInfo = self.aModelInfo

		aExcelHelper.openExcelSheet(outputfile)
		aExcelHelper.deleteSheet(['input']) #templ

		aTargetSheet = aExcelHelper.addSheet('templ', 'input')
		#aTargetSheet = aExcelHelper.getSheet('input')
		
		outList = aModelInfo.getClassListOrInterfaceList()
		if not outList:
			log.debug("---def writeExcelCoreClassList---")
			log.debug("data is none")
# 			aExcelHelper.closeExcel()
# 			sys.exit(0)

		for aClassInfo in outList:
			self.writeAttribute(aTargetSheet, aClassInfo)

#		aExcelHelper.deleteSheet(['templ']) #templ
		#aExcelHelper.closeExcel()

#-------------------------------------------------------------------------------
	def writeAttribute(self, sh, aClassInfo):

		#attributes = self.aModelInfo.getAttributes(aClassInfo)
		attributes = aClassInfo.fieldList
		
		i = self.getCurrentRow()
		for attr in attributes:
			self.writeAttributeRecord(sh, i, aClassInfo, attr)
			i = i + 1

##		#속성정보가 없는 경우에 대한 처리
##		if i == self.CONS.ATTRIBUTE_LIST_START_POSITION:
##			self.writeAttributeRecordBlank(sh, i)
##			i = i + 1

		self.setCurrentRow(i)

	def writeAttributeRecord(self, sh, row, aClassInfo, attr):
        # NO	ClassName	가시성	타입	속성명

		sh.Cells(row, 1).Value = row - (self.CONS.ATTRIBUTE_LIST_START_POSITION-1)	# 번호
		sh.Cells(row, 2).Value = aClassInfo.name
		sh.Cells(row, 3).Value = attr.visibility	# 가시성
		sh.Cells(row, 4).Value = attr.javaType		# 타입
		sh.Cells(row, 5).Value = attr.name			# 속성명
		