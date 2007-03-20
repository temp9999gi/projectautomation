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

"""Creates a report of each Class/Table"""


#Imported System Packages.
import os
import string

from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociationEnds

from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning
import warnings
from warnings import warn

############################
# Globals

TRANSLATOR_NAME='CreateReport'

############################
# Writer components

def write(destination, classList):
	"""
	Create Report in destination dirctory.
	"""
	text = []
	#Iterate through the tables/classes and process the data
	for cls in classList:
			
		#Set Class Title Title
		text.append("CLASS: %s" % (cls.getName(TRANSLATOR_NAME)))

		#Get name of class which this class inherits from
		baseClassNames = cls.getBaseClassNames(TRANSLATOR_NAME)
		if len(baseClassNames) >= 1:
			for baseClass in baseClassNames:
				text.append("	Inherits From: %s" % (baseClass))

		#Process each attribute in a given table (class)
		for attribute in getAllAttributes(classList, cls, TRANSLATOR_NAME):
				
			type = attribute.getType().getSQLType()
			text.append("	ATTRIBUTE:")
			text.append("		Name = %s" % \
									(attribute.getName(TRANSLATOR_NAME)))
			text.append("		Type = %s" % \
									(type))
			text.append("		GetterName = %s" \
									% (attribute.getGetterName(TRANSLATOR_NAME)))
			text.append("		SetterName = %s" % \
									(attribute.getSetterName(TRANSLATOR_NAME)))
			text.append("		AppenderName = %s" % \
									(attribute.getAppenderName(TRANSLATOR_NAME)))
			text.append("		isRequired = %s" % (attribute.isRequired()))
			text.append("		isUnique = %s" % (attribute.isUnique()))
			text.append("		isIndexed = %s" % (attribute.isIndexed()))
			text.append("		isPrimaryKey = %s" % (attribute.isPrimaryKey()))

		for assocEnd in getAllAssociationEnds(classList, cls, TRANSLATOR_NAME):
			text.append("	ASSOC END:")
			text.append("		Name = %s" % (assocEnd.getName(TRANSLATOR_NAME)))
			text.append("		AttribName = %s" % \
									(assocEnd.getAttributeName(TRANSLATOR_NAME)))
			text.append("		GetterName = %s" % \
									(assocEnd.getGetterName(TRANSLATOR_NAME)))
			text.append("		SetterName = %s" % \
									(assocEnd.getSetterName(TRANSLATOR_NAME)))
			text.append("		AppenderName = %s" % \
									(assocEnd.getAppenderName(TRANSLATOR_NAME)))
			text.append("		Multiplicity = %s" % (assocEnd.getMultiplicity()))
			text.append("		isNavigable = %s" % (assocEnd.isNavigable()))
			text.append("		OppositeEnd = %s.%s" % \
									(assocEnd.getOppositeEnd().getClassName(TRANSLATOR_NAME),
									 assocEnd.getOppositeEnd().getAttributeName(TRANSLATOR_NAME)))
			

		text.append("")
			
	text = string.join(text, '\n')
	f = open(destination, 'w')
	f.write(text)
	f.close()
	warn("Report Generation Complete... Good Bye.", InfoWarning)

