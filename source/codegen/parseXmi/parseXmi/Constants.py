# -*- coding: utf-8 -*-
# start
# CONSTANTS & GLOBALS

class Constants :
	global INPUT_XML_FILE		
	
	def __init__(self):
		
		from path import path
		
		# cwd = path('C:\_kldp\codegen\excel\writeXmlFromExcel')
		cwd = path('.')
		
		self.INPUT_DIR 	= cwd / 'input' 
		self.INPUT_DATA_DIR 	= self.INPUT_DIR / 'inputData'
		
 
		self.ETC_DIR	= self.INPUT_DIR / 'etc'
		
		self.TEMPLATE_DIR 	= self.INPUT_DIR / 'templates' 

		self.XML_TEMPLATE 	= self.TEMPLATE_DIR / "XML.tmpl"

		fullCwd = path('C:\_kldp\codegen\parseXmi\parseXmi')
		self.OUT_DIR 	= fullCwd / 'output'
		#파일명은 한글을 사용하면 에러남
		self.INPUT_CLASS_EXCEL_TEMPLATE 	= self.INPUT_DIR / 'templates' / \
			'inputClassTemplate.xls'
		self.OUTPUT_CLASS_EXCEL		= self.OUT_DIR / 'outputClassDefinition.xls'

		self.INPUT_CLASS_LIST_EXCEL_TEMPLATE 	= self.INPUT_DIR / 'templates' / \
			'inputClassListTemplate.xls'
		self.OUTPUT_CLASS_LIST_EXCEL		= self.OUT_DIR / 'outputClassList.xls'

		
		self.DB_JAVA_TYPE_MAPPING = self.ETC_DIR / 'mapping_properties.xml'
		
		# 프로그램 환경 정보
		self.INPUT_APP_ENV_XML 		= self.ETC_DIR / 'appEnv.xml'

	def setInputXmlFile(self, inputXmlFile):
		Constants.INPUT_XML_FILE = inputXmlFile
	def getInputXmlFile(self):
		return Constants.INPUT_XML_FILE		
	
