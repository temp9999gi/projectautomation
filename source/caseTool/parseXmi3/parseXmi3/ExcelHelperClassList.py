# -*- coding: utf-8 -*-
from ExcelHelper import *
#-------------------------------------------------------------------------------
class ExcelHelperClassList(ExcelHelper):
	def __init__(self):
		ExcelHelper.__init__
		#self.packagePath=''

	def writeExcelCoreClassList(self,aExcelHelper, outputfile):
		aModelInfo = self.aModelInfo

		aExcelHelper.openExcelSheet(outputfile)

		aTargetSheet = aExcelHelper.addSheet("templ",'List')

		aReaderAppEnvXml = ReaderAppEnvXml()

		i = self.CONS.CLASS_LIST_START_POSITION #
##		for aClassInfo in aModelInfo.classInfoList:????????????

		outList = aModelInfo.getClassListOrInterfaceList()
		if not outList:
			log.debug("---def writeExcelCoreClassList---")
			log.debug("data is none")
# 			aExcelHelper.closeExcel()
# 			sys.exit(0)

		for aClassInfo in outList:
			aReaderAppEnvXml.saveWriterInfo(aClassInfo, self.CONS.INPUT_APP_ENV_XML)
			#self.writeClassListMasterInfo(aTargetSheet, aClassInfo)
			self.writeHeadInfo(aTargetSheet, aClassInfo)
			self.writeClassRecord(aTargetSheet, aClassInfo, i)
			i = i + 1

		aExcelHelper.deleteSheet(['templ']) #templ
		aExcelHelper.closeExcel()

##	def writeClassListMasterInfo(self, sh, aClassInfo):
##		self.writeHeadInfo(sh, aClassInfo)


	def writeClassRecord(self, sh, aClassInfo, row):
		#for attr in aClassInfo.attributeListOfClassInfo:
		i = row
		sh.Cells(i, 1).Value = i - (self.CONS.CLASS_LIST_START_POSITION-1)	#
		sh.Cells(i, 2).Value = aClassInfo.name					#
		self.aModelInfo.initPackagePath()
		self.aModelInfo.setPackagePath(aClassInfo.namespace)
		sh.Cells(i, 3).Value = self.aModelInfo.getPackagePath() #aClassInfo.namespace.name		#
		sh.Cells(i, 4).Value = self.aModelInfo.getDocumentation(aClassInfo.taggedValue) #
		
			

		
		
#-------------------------------------------------------------------------------

