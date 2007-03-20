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

"""Creates Python TK Widgets of each Class/Table"""

import os
import sys
import re
import glob
import shutil

from pymerase.output.PyTkWidgets import HelperUtil
from pymerase.output.PyTkWidgets.Templates import Templates
from pymerase.util import PymeraseType
from pymerase.util.iPymeraseUtil import getClassByName
from pymerase.util.iPymeraseUtil import getAttribByName
from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociationEnds

from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning
import warnings
from warnings import warn

############################
# Globals

TRANSLATOR_NAME='CreatePyTkWidgets'
DBAPI_TRANSLATOR='CreateDBAPI'

codeTemplates = Templates()

def checkDestination(destination):
	"""
	Checks to see if the destination path exists, if it doesn't it creates the directory and moves into it.
	"""
	destination = os.path.abspath(destination)
	
	if os.path.exists(destination) == 0:
		os.mkdir(destination)
	elif os.path.isdir(destination) == 0:
		warn("%s exists but is not a directory." % (destination), RuntimeWarning)
		sys.exit(2)
				
def getAssociationByName(assocList, name):

	for assoc in assocList:
		if assoc.getOppositeEnd().getAttributeName(DBAPI_TRANSLATOR) == name:
			return assoc
	return None

###############################################
#CreateTkWidgets write function -- called by pymerase

def write(destination, classList):
	"""
	Creates PyTkDB Widgets in destination dirctory.
	"""

	templateDict = {}

	try:
		print ""
		print "\a"
		templateDict['%DBAPI%'] = raw_input("Enter DBAPI Name: ")
		print ""
		print ""
	except EOFError:
		#FIXME: Needs to be updated when full package support is added
		#	to pymerase.
		templateDict['%DBAPI%'] = classList[0].getPackage()
	
	checkDestination(destination)

	util = HelperUtil.HelperUtil()
				
	#Iterate through the tables/classes and process the data
	for myClass in classList:

		code = codeTemplates.getDbTemplate()

		#Replace Template %CLASSNAME% with actual class name
		code = re.sub('%CLASSNAME%', myClass.getName(DBAPI_TRANSLATOR), code)

		#Reset Grid Layout rowCounter
		util.resetRowCounter()

		#Get a list of attributes which are used for associations
		assocList = myClass.getAssociationEnds().values()
		assocAttribNameList = []
		for assocEnd in assocList:
			assocAttribNameList.append(assocEnd.getOppositeEnd().getAttributeName(DBAPI_TRANSLATOR))

		#Process all attributes in a given class
		attribList = getAllAttributes(classList, myClass, DBAPI_TRANSLATOR)
		for attrib in attribList:
						
			type = attrib.getType().getSQLType()

			#Check to see if attribute is also a Foreign Key
			if attrib.getName(DBAPI_TRANSLATOR) in assocAttribNameList:
				type = "FK"
				
			warn("Processing(%s:%s)" % (myClass.getName(TRANSLATOR_NAME), type), DebugWarning)

			#Process Primary Keys
			if attrib.isPrimaryKey() or type == "serial":
				warn('Ignoring Primary Key', InfoWarning)
			#Process Foriegn keys
			elif type == "FK":
				assoc = getAssociationByName(assocList, attrib.getName(DBAPI_TRANSLATOR))
				#oppAssoc - Opposite Association End
				oppAssoc = assoc.getOppositeEnd()
				oppAssocClass = getClassByName(classList,
																			 oppAssoc.getClassName(DBAPI_TRANSLATOR),
																			 DBAPI_TRANSLATOR)
				oppClassAttribList = getAllAttributes(classList, oppAssocClass, DBAPI_TRANSLATOR)
				oppClassPkAttrib = getAttribByName(oppClassAttribList,
																					 oppAssocClass.getPrimaryKeyName(DBAPI_TRANSLATOR),
																					 DBAPI_TRANSLATOR)

				code = re.sub('%OPTION_MENU_DICT%',
											util.makeOptionMenuDict(attrib.getName(DBAPI_TRANSLATOR),
																							oppAssocClass.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%UPDATE_FUNCTIONS%',
						util.makeUpdateOptionMenu(oppAssocClass.getName(DBAPI_TRANSLATOR),
																			attrib.getName(DBAPI_TRANSLATOR),
																			oppClassAttribList[1].getGetterName(DBAPI_TRANSLATOR),
																			oppClassPkAttrib.getGetterName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%LOAD_FUNCTION%',
											util.makeLoadFk(attrib.getName(DBAPI_TRANSLATOR),
																			oppClassAttribList[1].getGetterName(DBAPI_TRANSLATOR),
																			oppAssocClass.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%SAVE_FUNCTION%',
											util.makeSaveFk(oppAssocClass.getName(DBAPI_TRANSLATOR),
																			attrib.getName(DBAPI_TRANSLATOR)),
											code)
			#Process Integers and Doubles
			elif type == "integer":
				code = re.sub('%SAVE_FUNCTION%',
											util.makeSaveLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%LOAD_FUNCTION%',
											util.makeLoadLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			elif type == "double precision":
				code = re.sub('%SAVE_FUNCTION%',
											util.makeSaveLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%LOAD_FUNCTION%',
											util.makeLoadLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			elif type == "name":
				warn("FIXME: Ignoring name type", InfoWarning)
			#Process Text
			elif type == "text":
				code = re.sub('%SAVE_FUNCTION%',
											util.makeSaveLabelText(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%LOAD_FUNCTION%',
											util.makeLoadLabelText(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			#Process Variable Characters
			elif PymeraseType.isVarchar(type):
				code = re.sub('%SAVE_FUNCTION%',
											util.makeSaveLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%LOAD_FUNCTION%',
											util.makeLoadLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			#Process Characters
			elif PymeraseType.isChar(type):
				code = re.sub('%SAVE_FUNCTION%',
											util.makeSaveLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%LOAD_FUNCTION%',
											util.makeLoadLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			#Process Boolean
			elif type == "boolean":
				code = re.sub('%SAVE_FUNCTION%',
											util.makeSaveRadioBoolean(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%LOAD_FUNCTION%',
											util.makeLoadRadioBoolean(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			#Process Time Stamps
			elif type == "timestamp with time zone":
				warn("FIXME: Ignoring timestamp", InfoWarning)
			#Write out what is not being handled.
			else:
				warn("Table(%s), Type(%s), Attribute(%s) not processed.\n" \
						 "Please e-mail the above line to pymerase-devel@lists.sourceforge.net" % \
						 (myClass.getName(TRANSLATOR_NAME),
							type,
							attrib.getName(TRANSLATOR_NAME)),
						 InfoWarning)

		
		#Remove '%*%'
		code = re.sub('%SAVE_FUNCTION%', '', code)
		code = re.sub('%LOAD_FUNCTION%', '', code)
		code = re.sub('%OPTION_MENU_DICT%', '', code)
		code = re.sub('%UPDATE_FUNCTIONS%', '', code)
		
		#Write TkWidget to file
		fileName = "%sDbWidget.py" % (myClass.getName(DBAPI_TRANSLATOR))
		filePath = os.path.join(os.path.abspath(destination), fileName)

		f = open(filePath, 'w')
		f.write(code)
		f.close()
		
		warn("Python Tkinter DB Aware Widget Generation Complete... Good Bye.", InfoWarning)

