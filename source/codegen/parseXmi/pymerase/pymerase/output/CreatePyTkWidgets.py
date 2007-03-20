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

############################
# Writer components

#def isFKey(name):
#		"""
#		Checks to see if a field is a foreign key or primary key.
#
#		returns 1 if is fk or pk
#		returns 0 if is not fk or pk
#		"""
#		#FIXME: GeneX specific currently... needs to be more generic.
#		#FIXME: Should make sure FK/PK are at end of string
#		result = re.search('Fk', name)
#		result2 = re.search('Pk', name)
#		result3 = re.search('ID', name)
#		if result != None or result2 != None or result3 != None:
#				return 1
#		else:
#				return 0

def checkDestination(destination):
	"""
	Checks to see if the destination path exists, if it doesn't it creates the directory and moves into it.
	"""
	destination = os.path.abspath(destination)
	
	if os.path.exists(destination) == 0:
		os.mkdir(destination)
	elif os.path.isdir(destination) == 0:
		warn("%s exists but is not a directory." % (destination),
				 RuntimeWarning)
		sys.exit(2)
				

def copyLib(destination, templateDict):
	"""
	Copies lib files to destination directory and add
	required information to specific lib files.
	"""
	path, file = os.path.split(HelperUtil.__file__)
	path = os.path.join(path, "lib")
	search = os.path.join(path, "*.py")

	#List of files that need more inforation before copying
	template_files = [os.path.join(path, "dbSession.py")]

	#Retive files to copy
	filesToCopy = glob.glob(search)

	warn("--Copying Lib Files--", InfoWarning)
	
	for file in filesToCopy:
		filePath, fileName = os.path.split(file)
		fileDest = os.path.join(destination, fileName)

		#If not a template file, copy
		if file not in template_files:
			warn('%s' % (fileName), DebugWarning)
			shutil.copyfile(file, fileDest)
		#Else, add information, then copy
		else:
			warn('%s' % (fileName), DebugWarning)
			f = open(file, 'r')
			newFile = re.sub('%DBAPI%', templateDict['%DBAPI%'], f.read())
			f.close()

			df = open(fileDest, 'w')
			df.write(newFile)
			df.close()
			
	warn("--Done--", InfoWarning)



def getAssociationByName(assocList, name):
	"""
	getAssociationByName->association or None
	"""
	for assoc in assocList:
		if assoc.getOppositeEnd().getAttributeName(DBAPI_TRANSLATOR) == name:
			return assoc
	return None


###############################################
#CreateTkWidgets write function -- called by pymerase

def write(destination, classList):
	"""
	Creates PyTk Widgets in destination dirctory.
	"""

	#Information required to copy all lib files
	# (Needs more information)
	templateDict = {}

	try:
		print ""
		print "\a"
		apiName = raw_input("Enter DBAPI Name: ")
		print ""
		print ""
	except EOFError:
		#FIXME: Needs to be updated when full packages support is
		#	added to pymerase.
		if len(classList) >= 1:
			apiName = classList[0].getPackage()
		else:
			raise ValueError, 'ERROR, len(classList) < 1'

	templateDict['%DBAPI%'] = apiName


	checkDestination(destination)

	util = HelperUtil.HelperUtil()

	#Copy lib files with additional information
	copyLib(destination, templateDict)
				
	#Iterate through the tables/classes and process the data
	for myClass in classList:

		code = codeTemplates.getBasicTemplate()

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
		for attrib in getAllAttributes(classList, myClass, DBAPI_TRANSLATOR):
			
			type = attrib.getType().getSQLType()

			#Check to see if an attribute is also an association,
			# if so, change type to 'FK'
			if attrib.getName(DBAPI_TRANSLATOR) in assocAttribNameList:
				type = "FK"

			warn("Processing(%s:%s)" % (myClass.getName(TRANSLATOR_NAME), type),
					 DebugWarning)
			warn("	CapsWord: %s; English: %s" % (myClass.getName(DBAPI_TRANSLATOR),
																						 myClass.getName(TRANSLATOR_NAME)),
					 DebugWarning)
			#Process Primary keys
			if attrib.isPrimaryKey() or type == "serial":
				warn('Ignoring Primary Key', InfoWarning)

			#Process Foreign Keys
			if type == "FK":
				assoc = getAssociationByName(assocList,
																		 attrib.getName(DBAPI_TRANSLATOR))
				code = util.processFkVarElement(attrib,
																				assoc.getOppositeEnd(),
																				DBAPI_TRANSLATOR,
																				code)
				code = re.sub('%GET_FUNCTION%',
							 util.makeGetLabelIntegerEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%GET_FUNCTION%',
											util.makeGetOptionMenu(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%SET_FUNCTION%',
											util.makeSetLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%SET_FUNCTION%',
											util.makeSetOptionMenu(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				#code = re.sub('%SET_FUNCTION%',
				#			util.makeSelectOptionMenuItem(attrib.getName(DBAPI_TRANSLATOR)),
				#							code)
				#code = re.sub('%SET_FUNCTION%',
				#			util.makeAppendOptionMenu(attrib.getName(DBAPI_TRANSLATOR)),
				#							code)
			
			#Process Integers and Doubles
			elif type == "integer":
				code = re.sub('%VAR_ELEMENT%',
							 util.makeLabelIntegerEntry(attrib.getName(DBAPI_TRANSLATOR),
																					attrib.getName(TRANSLATOR_NAME),
																					attrib.isRequired()),
											code)
				code = re.sub('%GET_FUNCTION%',
							util.makeGetLabelIntegerEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				
				code = re.sub('%SET_FUNCTION%',
											util.makeSetLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			elif type == "double precision":
				code = re.sub('%VAR_ELEMENT%',
									util.makeLabelFloatEntry(attrib.getName(DBAPI_TRANSLATOR),
																					 attrib.getName(TRANSLATOR_NAME),
																					 attrib.isRequired()),
											code)
				code = re.sub('%GET_FUNCTION%',
							 util.makeGetLabelFloatEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				
				code = re.sub('%SET_FUNCTION%',
									util.makeSetLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
			elif type == "name":
				warn("FIXME: Ignoring 'name' type", InfoWarning)
			#Process Text
			elif type == "text":
				code = re.sub('%VAR_ELEMENT%',
											util.makeLabelText(attrib.getName(DBAPI_TRANSLATOR),
																				 attrib.getName(TRANSLATOR_NAME),
																				 attrib.isRequired()),
											code)
				code = re.sub('%GET_FUNCTION%',
											util.makeGetLabelText(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				
				code = re.sub('%SET_FUNCTION%',
											util.makeSetLabelText(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				
			#Process Variable Characters
			elif PymeraseType.isVarchar(type):
				code = re.sub('%VAR_ELEMENT%',
						util.makeLabelMaxLengthEntry(attrib.getName(DBAPI_TRANSLATOR),
																				 attrib.getName(TRANSLATOR_NAME),
																				 int(PymeraseType.getVarcharLen(type)),
																				 attrib.isRequired()),
											code)
				code = re.sub('%GET_FUNCTION%',
											util.makeGetLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				
				code = re.sub('%SET_FUNCTION%',
											util.makeSetLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				
			#Process Characters
			elif PymeraseType.isChar(type):
				code = re.sub('%VAR_ELEMENT%',
							util.makeLabelMaxLengthEntry(attrib.getName(DBAPI_TRANSLATOR),
																					 attrib.getName(TRANSLATOR_NAME),
																					 1,
																					 attrib.isRequired()),
											code)
				code = re.sub('%GET_FUNCTION%',
											util.makeGetLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				
				code = re.sub('%SET_FUNCTION%',
											util.makeSetLabelEntry(attrib.getName(DBAPI_TRANSLATOR)),
											code)
								
			#Process Boolean
			elif type == "boolean":
				code = re.sub('%VAR_ELEMENT%',
											util.makeRadioBoolean(attrib.getName(DBAPI_TRANSLATOR),
																						attrib.getName(TRANSLATOR_NAME),
																						attrib.isRequired()),
											code)
				code = re.sub('%GET_FUNCTION%',
										util.makeGetRadioBoolean(attrib.getName(DBAPI_TRANSLATOR)),
											code)
				code = re.sub('%SET_FUNCTION%',
										util.makeSetRadioBoolean(attrib.getName(DBAPI_TRANSLATOR)),
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


		#Association Processing
		assocList = myClass.getAssociationEnds().values()

		warn("ASSOCIATION ENDS:", DebugWarning)
		for assocEnd in assocList:
			warn("	%s" % (assocEnd.getAttributeName(DBAPI_TRANSLATOR)), DebugWarning)
			warn("	%s" % (assocEnd.getName(DBAPI_TRANSLATOR)), DebugWarning)
		warn("END ASSOCIATIONS", DebugWarning)
								
		#Remove '%*%'
		code = re.sub('%VAR_ELEMENT%', '', code)
		code = re.sub('%GET_FUNCTION%', '', code)
		code = re.sub('%SET_FUNCTION%', '', code)
		
		#Write TkWidget to file
		fileName = "%sWidget.py" % (myClass.getName(DBAPI_TRANSLATOR))
		filePath = os.path.join(os.path.abspath(destination), fileName)

		f = open(filePath, 'w')
		f.write(code)
		f.close()
		
		warn("Python Tkinter Widget Generation Complete... Good Bye.", InfoWarning)
