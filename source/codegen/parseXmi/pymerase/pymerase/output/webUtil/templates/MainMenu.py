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
import pgdb as db_api
import crypt
import os
import sys
import re
import string
import pickle

import config

sys.path.insert(0, config.BASE_PATH)
sys.path.insert(0, config.API_PATH)
sys.path.insert(0, config.MYWEBUTIL_PATH)

from myWebUtil.Session import Session
from myWebUtil.SessionUtil import SessionUtil
from myWebUtil.HTMLUtil import HTMLUtil

from #--DBAPI--# import DBSession
from myWebUtil.xor_string import xor_string

#GLOBALS
htmlUtil = HTMLUtil()
util = SessionUtil()

TEMPLATE_PATH = os.path.join(os.getcwd(), 'html')

def isFromLoginForm(form):
	#Login form is the only form that passes a key called form...
	#	all others pass it in session status pickle
	if form.has_key('form') and form.has_key('login') and form.has_key('password'):
		if form['form'].value == "login":
			return 1
	else:
		return 0


def getMenuHtml(mysession):
	
	menuInsert = ""
	
	menuList = util.getMenuList(mysession)
	menuList.sort()
	
	for menu in menuList:
		menuInsert += htmlUtil.getMenuInsert(menu, mysession)
		
	return menuInsert
		

def getMainMenuTemplate(mysession):
	"""
	Loads MainMenu Template and inserts data and returns the html
	"""
	html = htmlUtil.getHtmlTemplate('MainMenu.html', TEMPLATE_PATH)

	title = config.WEB_TITLE
	html = htmlUtil.insertHtmlTitle(html, title)
	html = util.insertSessionIntoHtmlForm(html, mysession.info['session'])
	
	menuInsert = getMenuHtml(mysession)
	html = re.sub("<!--INSERT_MENU_HERE-->", menuInsert, html)
	
	mainInsert = "<strong><font color=\"#000066\">User:</font></strong> %s<br>" \
							 % (mysession.info['user'])
	mainInsert += "<strong><font color=\"#000066\">SessionID:</font></strong> %s<br><br>" \
								% (mysession.info['session'])
	
	mainInsert += "<!--INSERT_HTML_HERE-->"

	html = re.sub("<!--INSERT_HTML_HERE-->", mainInsert, html)

	return html


if __name__ == '__main__':
	
	form = cgi.FieldStorage()
	
	if not form:
		htmlUtil.printHeader()
		print "Illegal Operation!<br>"
		print "\"Who is general error, and why is he reading my hard drive?\""

	#Execute this if form type is login
	elif isFromLoginForm(form):
		login = form['login'].value
		passwd = form['password'].value

		if passwd == "":
			passwd = None

		try:
			dbs = DBSession(dsn=config.DSN,
											database=config.DATABASE,
											user=login,
											password=passwd)

		except:
			htmlUtil.printHeader()
			print 'User or Password Invalid'
			raise ValueError("User or Password Invalid (%s,%s)" % (login, passwd))
		
		mysession = Session()
			
		#save session status
		mysession.info['user'] = login
		if passwd is not None:
			mysession.info['passwd'] = xor_string(passwd, 25)
		else:
			mysession.info['passwd'] = ""
		mysession.info['session'] = util.getNewSession()
		mysession.info['form'] = 'MainMenu'	 #saves name of form that is sending the information
			
		sessionId = mysession.info['session']
			
		util.openSessionDir(sessionId)
		util.saveSessionStatus(mysession)

		html = getMainMenuTemplate(mysession)
			
		htmlUtil.printHeader()
		print html
			
#--INSERT_ELIF_ISFROM--#

	#Show main menu with current status
	elif isFromSelf('MainMenu', form):
		#form ALWAYS passes session tag around... that's why this works.
		mysession = util.loadSessionStatus(form['session'].value)
		
		html = getMainMenuTemplate(mysession)
		
		mysession.info['form'] = 'MainMenu'
		util.saveSessionStatus(mysession)
		
		htmlUtil.printHeader()
		print html

		#Error!!! 
	else:
		htmlUtil.printHeader()
		print "<strong>Error!!! Major Error!!!</strong><br>"
		if not form:
			print "Not form!"
		else:
			mysession = util.loadSessionStatus(form['session'].value)
			util.debugInfo(mysession)
