# -*- coding: utf-8 -*-
# usage:  python gen.py Class.xml
# generates JavaBean Class.java and database access ClassMgr.java files from XML
# Programming by KyungUk, Sung
#
# Copyright (c) 2002 KyungUk, Sung
# start
# CONSTANTS & GLOBALS
import os

class Constants:
	def __init__(self, inPath):
		
		from path import path

		srcPath = path(inPath)
		pathString, filename = os.path.split(srcPath)
		
		parentPath = path(pathString).parent
		appRootPath = parentPath
		
		self.INPUT_DIR 	= appRootPath / 'input'

		self.INPUT_DATA_DIR 	= self.INPUT_DIR / 'inputData'
		self.OUT_DIR 	= appRootPath / 'output'
		self.ETC_DIR	= self.INPUT_DIR / 'etc'
		
		self.TEMPLATE_DIR 	= self.INPUT_DIR / 'templates' 
		self.PROPERTY_XML_FILE_DIR = self.INPUT_DIR

		self.JAVA_ANALYSIS_TEMPLATE 	= self.TEMPLATE_DIR / "JavaAnalysis.tmpl"

		
##		#파일명은 한글을 사용하면 에러남
##		self.INPUT_TABLE_TEMPLATE 	= self.INPUT_DIR / 'templates' / 'inputClassTemplate.xls'
##		self.OUTPUT_TABLE_EXCEL		= self.OUT_DIR / 'outputKlassDefinition.xls'

##		self.DB_JAVA_TYPE_MAPPING = self.ETC_DIR / 'mapping_properties.xml'
##		# 프로그램 환경 정보
##		self.INPUT_APP_ENV_XML 		= self.ETC_DIR / 'appEnv.xml'
