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
		self.DB_JAVA_TYPE_MAPPING = self.ETC_DIR / 'mapping_properties.xml'
		
		#-----------------------------------------------------------------------
		#DOMAIN
		self.JAVA_DOMAIN_TEMPLATE 	= self.TEMPLATE_DIR / "JAVA_DOMAIN_TEMPLATE.tmpl"
		self.DOMAIN_OUT_DIR 	= self.OUT_DIR / 'domain'
		#-----------------------------------------------------------------------
		#DAO
		self.DAO_TEMPLATE 	= self.TEMPLATE_DIR / "DAO_TEMPLATE.tmpl"
		self.DAO_OUT_DIR 	= self.OUT_DIR / 'dao' / 'ibatis'
		#-----------------------------------------------------------------------
		# IDAO
		self.IDAO_TEMPLATE 	= self.TEMPLATE_DIR / "IDAO_TEMPLATE.tmpl"
		self.IDAO_OUT_DIR 	= self.OUT_DIR / 'dao'

		
		
		