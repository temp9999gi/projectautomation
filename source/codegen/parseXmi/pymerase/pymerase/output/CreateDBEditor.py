###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2002 by:																								 #
#		* California Institute of Technology																 #
#																																				 #
#		All Rights Reserved.																								 #
#																																				 #
# Permission is hereby granted, free of charge, to any person						 #
# obtaining a copy of this software and associated documentation files		#
# (the "Software"), to deal in the Software without restriction,					#
# including without limitation the rights to use, copy, modify, merge,		#
# publish, distribute, sublicense, and/or sell copies of the Software,		#
# and to permit persons to whom the Software is furnished to do so,			 #
# subject to the following conditions:																		#
#																																				 #
# The above copyright notice and this permission notice shall be					#
# included in all copies or substantial portions of the Software.				 #
#																																				 #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,				 #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF			#
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND									 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS		 #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN			#
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN			 #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE				#
# SOFTWARE.																															 #
###########################################################################
#
#			 Authors: Brandon King
# Last Modified: $Date: 2007/01/01 13:36:52 $
#

import os
import re
import string

#from mx import DateTime

from pymerase.output.webUtil import makePackage
from pymerase.output.webUtil import CodeUtil
from pymerase.output.webUtil import HTMLUtil
from pymerase.util.fk_util import fk_util
from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociations

codeUtil = CodeUtil.CodeUtil()
htmlUtil = HTMLUtil.HTMLUtil()
fkUtil = fk_util()

def getLicense():
		text = """#!/usr/bin/env python
###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2002 by:																								 #
#		* California Institute of Technology																 #
#																																				 #
#		All Rights Reserved.																								 #
#																																				 #
# Permission is hereby granted, free of charge, to any person						 #
# obtaining a copy of this software and associated documentation files		#
# (the \"Software\"), to deal in the Software without restriction,				#
# including without limitation the rights to use, copy, modify, merge,		#
# publish, distribute, sublicense, and/or sell copies of the Software,		#
# and to permit persons to whom the Software is furnished to do so,			 #
# subject to the following conditions:																		#
#																																				 #
# The above copyright notice and this permission notice shall be					#
# included in all copies or substantial portions of the Software.				 #
#																																				 #
# THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND,			 #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF			#
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND									 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS		 #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN			#
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN			 #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE				#
# SOFTWARE.																															 #
###########################################################################
#
#			 Authors: Brandon King
# Last Modified: $Date: 2007/01/01 13:36:52 $
#"""
		return text

def writeFile(code, fileName, path):
		filePath = os.path.join(path, fileName)
		print 'WebCode[INFO] - Writing(%s)' % (fileName)
		file = open(filePath, 'w')
		file.write(code)
		file.close()	 	


def write(destination, tables):
		
		#Path information
		temp = os.path.abspath(makePackage.__file__)
		temp = os.path.split(temp)
		webUtilPath = temp[0]

		
		webCodePath = destination
		myWebUtilPath = os.path.join(webCodePath, 'myWebUtil')
		htmlPath = os.path.join(webCodePath, 'html')

		if os.path.isdir(destination):
				if not os.path.isdir(webCodePath):
						os.mkdir(webCodePath)
						os.mkdir(myWebUtilPath)
		else:
				msg = "Invalid destination (%s)" % destination
				raise ValueError, msg

		if not os.path.exists(myWebUtilPath):
				os.mkdir(myWebUtilPath)
		elif os.path.exists(myWebUtilPath) and not os.path.isdir(myWebUtilPath):
				msg = "Invalid desination (%s)" % (myWebUtilPath)
				raise ValueError, msg
				

		if not os.path.isdir(htmlPath):
				os.mkdir(htmlPath)
		elif os.path.exists(htmlPath) and not os.path.isdir(htmlPath):
				msg = "Invalid destination (%s)" % htmlPath
				raise ValueError, msg

		path, temp = os.path.split(makePackage.__file__)
		path = os.path.join(path, 'templates')

		#makePackage and populate with static .py scripts
		makePackage.makePackage(destination, webUtilPath)

		#retrive session code template
		sessionCode = makePackage.getTemplate(path, 'Session.py')
		mainMenuCode = makePackage.getTemplate(path, 'MainMenu.py')
		
		counter = 1
		stageCount = 1
		tableList = []

		###########################################################
		## Table Processing
		###########################################################		
		for tbl in tables:
				tableName = tbl.getName()
								
				print 'Processing %s...' % (tableName)

				###########################################################
				## Session Code
				###########################################################
				sessionCode = codeUtil.insertMenuStatus(sessionCode, tableName)
				
				sessionCode = codeUtil.insertTableStage(sessionCode, tableName, 'stage1')

				#print 'WebCode[INFO] - Count(%s)' % (counter)
				if counter <= 3:
						tableList.append(tableName)
						counter += 1
				else:
						counter = 2
						stage = 'stage%s' % (stageCount)
						sessionCode = codeUtil.insertStageComplete(sessionCode,
																											 stage,
																											 tableList)
				
						tableList = []
						tableList.append(tableName)
						stageCount += 1

				
				###########################################################
				## Main Menu Code
				###########################################################
				mainMenuCode = codeUtil.insertElifIsfrom(tableName, mainMenuCode)
				
				###########################################################
				## Table Code
				###########################################################
				tableCode = makePackage.getTemplate(path, 'Table.py')
				tableCode = codeUtil.insertTableName(tableCode, tableName)
				tableFileName = os.path.join(destination,
																		 '%s_web.py' % (tableName))
				htmlFileName = os.path.join(htmlPath,
																		'%s_menu.html' % (tableName))
				viewFileName = os.path.join(htmlPath,
																		'%s_template.html' % (tableName))

				assocList = getAllAssociations(tables, tbl)
				assocNameList = []
				for a in assocList:
						assocNameList.append(a.getName())
				
				for attrib in getAllAttributes(tables, tbl):
						if not isFKey(attrib.getName()) and not attrib.isPrimaryKey():
								tableCode = codeUtil.insertFormLoader(tableCode,
																											attrib)
						#Make sure attrib is only a primary key and not both PK & FK.
						if attrib.isPrimaryKey() and attrib.getName() not in assocNameList:
								tableCode = codeUtil.insertFormId(tableCode,
																									attrib)

								tableCode = re.sub("#--INSERT_PK_NAME--#", attrib.getName(), tableCode)
								
						else:
								tableCode = codeUtil.insertProcessNewRecord(tableCode,
																														attrib)
								tableCode = codeUtil.insertProcessEditRecord(tableCode,
																														 attrib)
				
				assocList = fkUtil.getLocalLinks(tbl)

				for assoc in assocList:
						tableCode = codeUtil.insertMenuList(tableCode, tables, assoc)

				tableCode = codeUtil.insertTableMenuList(tableCode, tables, tbl)

				#####
				#Setup View Mode
				tableCode = codeUtil.insertGetData(tableCode, getAllAttributes(tables, tbl))
				tableCode = codeUtil.insertGetData2(tableCode, getAllAttributes(tables, tbl))
				tableCode = codeUtil.insertHeaderList(tableCode, getAllAttributes(tables, tbl))

				assocList = []
				for assoc in getAllAssociations(tables, tbl):
						assocList.append(assoc.getName())
				
				tableCode = codeUtil.insertHtmlBodyList(tableCode,
																								getAllAttributes(tables, tbl),
																								assocList)
				
				tableCode = codeUtil.insertTableRowData(tableCode,
																								getAllAttributes(tables, tbl),
																								assocList)

				#Get links in local table
				localAssocList = fkUtil.getLocalLinks(tbl)
				
				tableCode = codeUtil.insertLinkForm(tableCode,
																						localAssocList)

				tableCode = codeUtil.insertLinkForm2(tableCode,
																						localAssocList)
				#####
				
				tableFile = open(tableFileName, 'w')
				tableFile.write(tableCode)
				tableFile.close()
				del tableCode
				
				#####
				
				htmlMenu = makePackage.getTemplate(path, "table_menu_template.html")
				htmlMenu = htmlUtil.insertTitle(htmlMenu, tbl.getName())

				htmlFile = open(htmlFileName, "w")
				htmlFile.write(htmlMenu)
				htmlFile.close()
				del htmlMenu

				viewTemplate = makePackage.getTemplate(path, "view_mode_template.html")
				viewTemplate = htmlUtil.insertTitle(viewTemplate, tbl.getName())

				viewFile = open(viewFileName, 'w')
				viewFile.write(viewTemplate)
				viewFile.close()
				del viewFile

		writeFile(sessionCode, 'Session.py', myWebUtilPath)
		del sessionCode

		writeFile(mainMenuCode, 'MainMenu.py', webCodePath)
		del mainMenuCode
		
		mainMenuHtml = makePackage.getTemplate(path, 'menu_template.html')
		writeFile(mainMenuHtml, 'MainMenu.html', htmlPath)
		del mainMenuHtml

		print os.linesep \
					+ 'CreatDBEditor Processing Complete... Have a nice day!' \
					+ os.linesep


def isFKey(name):
		"""
		Checks to see if a field is a foreign key.

		returns 1 if is fk
		returns 0 if is not fk
		"""
		#FIXME: GeneX specific currently... needs to be more generic.
		result = re.search('_fk', name)
		if result != None:
				return 1
		else:
				return 0
