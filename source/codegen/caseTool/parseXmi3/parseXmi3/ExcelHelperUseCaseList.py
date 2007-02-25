# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
from ExcelHelper import *

class ExcelHelperUseCaseList(ExcelHelper):
	def __init__(self):
		ExcelHelper.__init__

	def writeExcelCoreUseCaseList(self,aExcelHelper, outputfile):
		aModelInfo = self.aModelInfo

		aExcelHelper.openExcelSheet(outputfile)

		aTargetSheet = aExcelHelper.addSheet("templ",'List')

		aReaderAppEnvXml = ReaderAppEnvXml()

		i = self.CONS.USECASE_LIST_START_POSITION # UseCase
		for aUseCase in aModelInfo.getUseCaseList():
			aReaderAppEnvXml.saveWriterInfo(aUseCase, self.CONS.INPUT_APP_ENV_XML)
			self.writeHeadInfo(aTargetSheet, aUseCase)
			self.writeUseCaseRecord(aTargetSheet, aUseCase, i)
			i = i + 1

		aExcelHelper.deleteSheet(['templ']) #templ
		aExcelHelper.closeExcel()

	def writeUseCaseRecord(self, sh, aUseCase, row):
		#for attr in aUseCase.attributeListOfUseCaseInfo:
		i = row
		sh.Cells(i, 1).Value = i - (self.CONS.USECASE_LIST_START_POSITION-1)
		sh.Cells(i, 2).Value = aUseCase.name		
		actor = self.aModelInfo.getActor(aUseCase)
		sh.Cells(i, 3).Value = aUseCase.namespace.name+'/' + actor
		sh.Cells(i, 4).Value = self.aModelInfo.getDocumentation(aUseCase.taggedValue)
#-------------------------------------------------------------------------------
	"""
<UML:UseCase xmi.id="UMLUseCase.3" xmi.uuid="DCE:2F0E53B4-C105-4CB0-A6A2-597F921DFC07"
	name="������ visibility="public" isSpecification="false"
	namespace="UMLModel.2" isRoot="false" isLeaf="false" isAbstract="false"
	participant="UMLAssociationEnd.10"/>"""
	
	"""
<UML:Association xmi.id="UMLAssociation.8" xmi.uuid="DCE:E160B30A-2CF3-4E8F-80CA-481EF585A30B"
	name="" visibility="public" isSpecification="false" namespace="UMLModel.2">
	<UML:Association.connection>
	<UML:AssociationEnd xmi.id="UMLAssociationEnd.9"
		xmi.uuid="DCE:4CB9C230-4A8F-4963-AFE8-8F5995281D95" name="" visibility="public"
		isSpecification="false" isNavigable="false" ordering="unordered" aggregation="none"
		targetScope="instance" changeability="changeable"
		association="UMLAssociation.8" type="UMLActor.4"/>
	<UML:AssociationEnd xmi.id="UMLAssociationEnd.10"
		xmi.uuid="DCE:B80EB6B9-419E-4970-9445-5405E4C3941D" name="" visibility="public"
		isSpecification="false" isNavigable="true" ordering="unordered"
		aggregation="none" targetScope="instance" changeability="changeable"
		association="UMLAssociation.8" type="UMLUseCase.3"/>
	</UML:Association.connection>
</UML:Association>
	"""
