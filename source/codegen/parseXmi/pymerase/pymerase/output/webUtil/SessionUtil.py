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

import os
import time
import pickle
import re
import sys

from myWebUtil.xor_string import xor_string



######################
# SessionUtil

class SessionUtil:
	def __init__(self):
		self.SCRIPT_PATH = os.getcwd()
		self.CONTACT_EMAIL = "kingb@caltech.edu"
		
		self.DISPLAY_ON = 1
		self.DISPLAY_OFF = 0
		self.YES = 1
		self.NO = 0
		
		
	def getNewSession(self):
		"""
		returns a string to be used as session id.
		"""
		return str(time.time())


	def isValidSession(self, sessionId):
		"""
		Checks for valid sessionId.
		
		returns 1 if valid
		returns 0 if invalid
		"""
		if re.search("/", sessionId) == None:
			return 1
		else:
			self.printHeader()
			print "Invalid filename: %s" % sessionId
			return 0

		
	def openSessionDir(self, sessionId):
		"""
		opens the Session directory for storing and loading sessions and annotations
		"""
		
		#FIXME: May want to change this so user can use
		#FIXME: command line to choose where sessions should go.
		os.chdir('/tmp/')
		
		#FIXME: Change this so it uses the name of the web based
		#FIXME: interface as base session directory
		if not os.path.isdir('dbweb'):
			os.mkdir('dbweb')
			os.chdir('/tmp/dbweb')

		elif os.path.isdir('dbweb'):
			os.chdir('/tmp/dbweb')
			
		if os.path.isdir(sessionId):
			os.chdir(sessionId)
		else:
			os.mkdir(sessionId)
			os.chdir(sessionId)

	def saveSessionStatus(self, session):
		"""
		Given a session obj, pickles out to file called session_status
		in the current working directory
		
		Call openSessionDir(sessionId) to change to session directory
		"""
		self.openSessionDir(session.info['session'])
		file = open('session_status', 'w')
		pickle.dump(session, file)
		file.close()

		
	def loadSessionStatus(self, sessionId):
		"""
		Opens session directory, loads the session object and returns it.
		"""
		self.openSessionDir(sessionId)
		
		file = open('session_status', 'r')
		session = pickle.load(file)
		file.close()
		
		return session


	def debugInfo(self, mysession):
		"""
		Prints session information for debugging purposes.
		"""
				
		print "<strong><u>session.info</u></strong><br>"
		for x in mysession.info.keys():
			print "%s (%s)<br>" % (x, mysession.info[x])

			print "<br>"
			print "<strong><u>session.menuStatus</u></strong><br>"
			for x in mysession.menuStatus.keys():
				print "%s (%s)<br>" % (x, mysession.menuStatus[x])

				
	def isFromForm(self, formName, form):
		"""
		Checks to see if the form that sent it was from formName
		
		Yes returns 1
		No	returns 0
		"""
		mysession = self.loadSessionStatus(form["session"].value)
		if mysession.info['form'] == formName:
			return 1
		else:
			return 0
	

	def getMenuList(self, mysession):
		
		#FIXME: Check for tables that are suppose to be
		#FIXME: accessable during current stage.
		list = []
		for x in mysession.menuStatus.keys():
			list.append(x)

		return list



	#FIXME: Maybe this should go in another class? HTMLUtil maybe?
	#FIXME: altough HTMLUtil is currently, kind of general.
	def insertSessionIntoHtmlForm(self, html, sessionId):
		"""
		Inserts sessionId into html form and returns html
		"""
		return re.sub("mysession", sessionId, html)


	def getDBSessionArgs(self, mysession):
		"""
		Given a Session object, returns tuple of arguments for
		connecting with PyMerase DBAPI DBSession object.

		returns (login, passwd)
		"""
		login = mysession.info['user']
		ePass = mysession.info['passwd']
		#raise ValueError, "ePass(%s) type(%s)" % (ePass, type(ePass))
		if ePass == "" or ePass is None:
			passwd = None
		else:
			passwd = xor_string(ePass, 25)

		return (login, passwd)









