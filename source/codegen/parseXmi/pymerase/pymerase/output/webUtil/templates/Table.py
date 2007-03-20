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
# Last Modified: $Date: 2007/01/01 13:36:53 $
#

import cgi
import os
import sys
import re
import string

import config

from myWebUtil.SessionUtil import SessionUtil
from myWebUtil.HTMLUtil import HTMLUtil
from myWebUtil.xor_string import xor_string

from #--DBAPI--# import DBSession

#GLOBALS
SCRIPT_PATH = os.getcwd()


def processNewRecord():
	mysession = util.loadSessionStatus(form['session'].value)
	login, passwd = util.getDBSessionArgs(mysession)
	
	dbs = DBSession(dsn=config.DSN,
									database=config.DATABASE,
									user=login,
									password=passwd)
		
	htmlUtil.printHeader()

	obj = dbs.#--TABLE_NAME--#()

#--INSERT_PROCESS_NEW_RECORD--#

	obj.commit()

	print 'Commit Complete'
	htmlUtil.printReturnMainMenu(mysession)


def processEditRecord():
	mysession = util.loadSessionStatus(form['session'].value)
	login, passwd = util.getDBSessionArgs(mysession)
	
	dbs = DBSession(dsn=config.DSN,
									database=config.DATABASE,
									user=login,
									password=passwd)
		
	htmlUtil.printHeader()

	objList = dbs.getObjects(dbs.#--TABLE_NAME--#, [str(form['#--INSERT_PK_NAME--#'].value)])
	obj = objList[0]

#--INSERT_PROCESS_EDIT_RECORD--#

	obj.commit()

	print 'Update Complete'
	htmlUtil.printReturnMainMenu(mysession)
	

def displayMenuForm():
	"""
	Displays Menu for Table

	Edit or New Record
	"""
	mysession = util.loadSessionStatus(form['session'].value)
	login, passwd = util.getDBSessionArgs(mysession)

	html = htmlUtil.getHtmlTemplate("#--TABLE_NAME--#_menu.html", config.HTML_PATH)
	html = util.insertSessionIntoHtmlForm(html, mysession.info['session'])

	dbs = DBSession(dsn=config.DSN,
									database=config.DATABASE,
									user=login,
									password=passwd)

	objList = dbs.getAllObjects(dbs.#--TABLE_NAME--#)

#--INSERT_TABLE_MENU_LIST--#
																
	mysession.info['form'] = '#--TABLE_NAME--#'
	util.saveSessionStatus(mysession)
	htmlUtil.printHeader()
	print html
	

def displayNewForm(warnings = ""):
	mysession = util.loadSessionStatus(form['session'].value)
	login, passwd = util.getDBSessionArgs(mysession)
	
	htmlUtil.printHeader()
	
	html = htmlUtil.getHtmlTemplate("#--TABLE_NAME--#.html", config.HTML_PATH)
	html = util.insertSessionIntoHtmlForm(html, mysession.info['session'])
	html = htmlUtil.insertHandler(html, 'commitNew')

	dbs = DBSession(dsn=config.DSN,
									database=config.DATABASE,
									user=login,
									password=xor_string(passwd,25))

#--INSERT_LINK_MENU_CODE--#
	
	mysession.info['form'] = '#--TABLE_NAME--#'
	util.saveSessionStatus(mysession)
		 
	print html

def displayEditForm():
	mysession = util.loadSessionStatus(form['session'].value)
	login, passwd = util.getDBSessionArgs(mysession)
	
	dbs = DBSession(dsn=config.DSN,
									database=config.DATABASE,
									user=login,
									password=passwd)
		
	objList = dbs.getObjects(dbs.#--TABLE_NAME--#,
													 [str(form['selection'].value)])
	obj = objList[0]
 
	html = htmlUtil.getHtmlTemplate("#--TABLE_NAME--#.html", config.HTML_PATH)
	html = util.insertSessionIntoHtmlForm(html, mysession.info['session'])

#--INSERT_FORM_LOADER--#

#--INSERT_ID--#

	html = htmlUtil.insertHandler(html, 'commitEdit')

#--INSERT_LINK_MENU_CODE--#

	htmlUtil.printHeader()
	print html


def displayViewForm():
	import HTMLgen

	tbl = HTMLgen.Table(width="700")
	
	mysession = util.loadSessionStatus(form['session'].value)
	login, passwd = util.getDBSessionArgs(mysession)
	
	html = htmlUtil.getHtmlTemplate("#--TABLE_NAME--#_template.html", config.HTML_PATH)
	html = util.insertSessionIntoHtmlForm(html, mysession.info['session'])

	dbs = DBSession(dsn=config.DSN,
									database=config.DATABASE,
									user=login,
									password=xor_string(passwd,25))
	
	objList = dbs.getObjects(dbs.#--TABLE_NAME--#,
														[str(form['selection'].value)])
	try:
		obj = objList[0]
	except:
		msg = "Invalid object in table #--TABLE_NAME--#\n pk(%s)" \
					% (str(form['selection'].value))
		raise ValueError, msg

#--INSERT_GET_DATA--#

#--INSERT_LINK_FORMS--#

	headerList = []
#--INSERT_HEADER_LIST--#

	htmlBody = []
#--INSERT_HTML_BODY_LIST--#

	tbl.body = []
	tbl.body.append(headerList)
	tbl.body.append(htmlBody)

	html = re.sub("<!--INSERT_FORM_HERE-->", tbl.__str__(), html)
	
	htmlUtil.printHeader()
	print html
	htmlUtil.printReturnMainMenu(mysession)


def displayLinkView():
	import HTMLgen

	tbl = HTMLgen.Table(width="700")
	
	mysession = util.loadSessionStatus(form['session'].value)
	login, passwd = util.getDBSessionArgs(mysession)

	html = htmlUtil.getHtmlTemplate("#--TABLE_NAME--#_template.html", config.HTML_PATH)
	html = util.insertSessionIntoHtmlForm(html, mysession.info['session'])

	dbs = DBSession(dsn=config.DSN,
									database=config.DATABASE,
									user=login,
									password=passwd)

	fObjList = dbs.getObjects(getattr(dbs, form['reqObj'].value), form['selection'].value)
	fObj = fObjList[0]

	objList = fObj.get#--TABLE_NAME--#()

	headerList = []
#--INSERT_HEADER_LIST--#

	tblList = []
	tblList.append(headerList)

	for obj in objList:
#--INSERT_GET_DATA2--#

#--INSERT_LINK_FORMS2--#

		tblRow = []
#--INSERT_TABLE_ROW_DATA--#
		tblList.append(tblRow)

	tbl.body = tblList

	html = re.sub('<!--INSERT_FORM_HERE-->', tbl.__str__(), html)

	htmlUtil.printHeader()
	print html

#Main
if __name__ == '__main__':
	form = cgi.FieldStorage()
	util = SessionUtil()
	htmlUtil = HTMLUtil()
	
	if not form:
		htmlUtil.printHeader()
		print "Illegal Operation!<br>"
		print "\"Who is general error, and why is he reading my hard drive?\""

	#Check where data came from.
	if util.isFromForm('MainMenu', form):
		displayMenuForm()

	#Handles form when data is sent to self.
	elif util.isFromForm('#--TABLE_NAME--#', form):
		if form['handler'].value == "edit":
			displayEditForm()
		elif form['handler'].value == "new":
			displayNewForm()
		elif form['handler'].value == "view":
			displayViewForm()
		elif form['handler'].value == "commitEdit":
			processEditRecord()
		elif form['handler'].value == "commitNew":
			processNewRecord()
		elif form['handler'].value == "returnMenu":
			displayMenuForm()
		else:
			htmlUtil.printHeader()
			print "Error:"
			cgi.print_form(form)

			
				
	#Error!!! 
	else:
		if form.has_key('handler'):
			if form['handler'].value == 'viewLink':
				mysession = util.loadSessionStatus(form['session'].value)
				mysession.info['form'] = '#--TABLE_NAME--#'
				util.saveSessionStatus(mysession)
				displayLinkView()

		else:
			htmlUtil.printHeader()
			print "<strong>Error!!! Major Error!!!</strong><br>"
			if not form:
				print "Not form!"
			else:
				mysession = util.loadSessionStatus(form['session'].value)
				util.debugInfo(mysession)
