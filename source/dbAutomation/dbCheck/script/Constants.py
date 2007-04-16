# -*- coding: utf-8 -*-
# start
# CONSTANTS & GLOBALS
import os
from path import path

class Constants :
	global INPUT_XML_FILE
		
	def __init__(self):
		pass # self.DB_JAVA_TYPE_MAPPING = self.ETC_DIR / 'mapping_properties.xml'

	def setConstant(self, inPath):
		
		srcPath = path(inPath)

		pathString, filename = os.path.split(srcPath)
		

		parentPath = path(pathString).parent
		appRootPath = parentPath

		self.INPUT_DIR 	= appRootPath / 'input'
		
		self.LOG_FILE 	= path(pathString) / "appLog.log"
		
		self.INPUT_DATA_DIR 	= self.INPUT_DIR / 'inputData'
		
 
		self.ETC_DIR	= self.INPUT_DIR / 'etc'
		
		self.TEMPLATE_DIR 	= self.INPUT_DIR / 'templates' 

		self.XML_TEMPLATE 	= self.TEMPLATE_DIR / "XML.tmpl"


		
		self.OUT_DIR 	= appRootPath / 'output'
		#파일명은 한글을 사용하면 에러남
		#------------------------------------------------------------------------
		self.OUTPUT_XLS_FILE 	= self.OUT_DIR / 'output.xls'
		self.XLS_FILE_TEMPLATE 	= self.TEMPLATE_DIR / 'tmpl_output.xls'
		#------------------------------------------------------------------------
		
		self.INPUT_CLASS_ATTRIBUTE 	= self.INPUT_DIR / 'inputData' / \
			'input.xls'

		self.INPUT_CLASS_EXCEL_TEMPLATE 	= self.INPUT_DIR / 'templates' / \
			'inputClassTemplate.xls'
		self.INPUT_INTERFACE_XLS_TEMPLATE 	= self.INPUT_DIR / 'templates' / \
			'inputInterfaceTemplate.xls'

		self.INPUT_CLASS_XLS_TMPL_FOR_EXPORT 	= self.INPUT_DIR / 'templates' / \
			'inputClassTmplForExport.xls'
			
		self.OUTPUT_CLASS_EXCEL		= self.OUT_DIR / 'outputClassDefinition'
# 		self.INPUT_CLASS_TEMPLATE 	= self.INPUT_DIR / 'templates' / 'inputClassTemplate.xls'
# 		self.OUTPUT_CLASS_EXCEL		= self.OUT_DIR / 'outputClassDefinition.xls'

		self.OUTPUT_INTERFACE_EXCEL		= self.OUT_DIR / 'outputInterfaceDefinition'
		
		self.OUTPUT_CLASS_EXPORT_XLS	= self.OUT_DIR / 'outputClassForExport.xls'
		
		self.INPUT_CLASS_LIST_XLS_TEMPLATE 	= self.INPUT_DIR / 'templates' / \
			'inputClassListTemplate.xls'
			


		self.OUTPUT_CLASS_LIST_EXCEL		= self.OUT_DIR / 'outputClassList.xls'
		
		self.INPUT_INTERFACE_LIST_XLS_TEMPLATE 	= self.INPUT_DIR / 'templates' / \
			'inputInterfaceListTemplate.xls'

		self.OUTPUT_INTERFACE_LIST_EXCEL		= self.OUT_DIR / 'outputInterfaceList.xls'

		self.INPUT_USECASE_LIST_TEMPLATE 	= self.INPUT_DIR / 'templates' / \
			'inputUseCaseListTemplate.xls'
		self.OUTPUT_USECASE_LIST_EXCEL		= self.OUT_DIR / 'outputUseCaseList.xls'

		
		self.DB_JAVA_TYPE_MAPPING = self.ETC_DIR / 'mapping_properties.xml'
		
		# 프로그램 환경 정보
		self.INPUT_APP_ENV_XML 		= self.ETC_DIR / 'appEnv.xml'
		
		#CLASS_EXCEL_TEMPLATE의 ATTRIBUTE START 위치
		self.ATTRIBUTE_LIST_START_POSITION = 2
		
		
		self.CLASS_LIST_START_POSITION = 7 #클래스의 목록 시작위치
		
		self.USECASE_LIST_START_POSITION = 7 #클래스의 목록 시작위치
		
		self.EXCEL_MAX_SHEET_COUNT = 250


		
	def setInputXmlFile(self, inputXmlFile):
		Constants.INPUT_XML_FILE = inputXmlFile
	def getInputXmlFile(self):
		return Constants.INPUT_XML_FILE		
	
