###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2003 by:																								 #
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
#			Revision: $Revision: 1.1 $
#

"""Creates Squash Sigmoid Psuedo UML File Format"""


#Imported System Packages.
import os
import string

from pymerase.ClassMembers import getAllAttributes
from pymerase.ClassMembers import getAllAssociationEnds

from pymerase.output.dbAPI import fkeyTypes

from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning
import warnings
from warnings import warn

############################
# Globals

TRANSLATOR_NAME='CreateSSUML'

############################
# Writer components

def write(destination, classList):
	"""
	Create Report in destination dirctory.
	"""
	text = []
	#Iterate through the tables/classes and process the data
	for cls in classList:

		#Handle Indentation for Class (Make it look pretty)
		tmp = 0
		cur = 0
		
		allAttributes = getAllAttributes(classList, cls, TRANSLATOR_NAME)
		allAssociationEnds = getAllAssociationEnds(classList, cls, TRANSLATOR_NAME)

		#Used to remove last comma
		#totalNumAttribs = len(allAssociationEnds) + len(allAttributes)
		
		for attribute in allAttributes:
			tmp = len(attribute.getName(TRANSLATOR_NAME))
			if tmp > cur:
				cur = tmp

		for assocEnd in allAssociationEnds:
			tmp = len(assocEnd.getOppositeEnd().getName(TRANSLATOR_NAME))
			if tmp > cur:
				cur = tmp

		#totalIdent is the total indentation for 'type' section.
		# Used to calculate how much whitespace should go inbetween
		# attribute and type information to make all the 'types' for
		# a give class line up with each other.
		totalIndent = cur + 3
					
			
		#Set Class Title Title
		#text.append("%s" % (cls.getName(TRANSLATOR_NAME)))
		className = cls.getName(TRANSLATOR_NAME)

		#Get name of class which this class inherits from
		baseClassNames = cls.getBaseClassNames(TRANSLATOR_NAME)
		#IF inherits from one class
		if len(baseClassNames) == 1:
			text.append("%s ^ %s" % (className, baseClassNames[0]))
		#elif inherits from more than one class --> Not supported
		elif len(baseClassNames) > 1:
			text.append("%s ^ %s" % (className, baseClassNames[0]))
			warn('Class %s inherts from %s classes... Only supports single inheritance. Choosing %s' % \
					 (className, len(baseClassNames), baseClassNames[0]), InfoWarning)
		#No inheritance needed
		else:
			text.append("%s" % (className))
					 
		#Start class def
		text.append("(")

		#Process each attribute in a given table (class)
		for attribute in getAllAttributes(classList, cls, TRANSLATOR_NAME):
			attribName = attribute.getName(TRANSLATOR_NAME)
			type = attribute.getType().getJavaTypeStr()

			#Pretty Indenting Calculation
			indentNum = totalIndent - len(attribName)
			indent = " " * indentNum
			
			text.append("	+ %s:" % (attribName) + indent + "%s," % (type))


		#Process each association end
		for assocEnd in getAllAssociationEnds(classList, cls, TRANSLATOR_NAME):

			mult = assocEnd.getMultiplicity()
			sym = ''

			#Handle Multiplicity
			if mult == fkeyTypes.OneToOne:
				sym = ''
			elif mult == fkeyTypes.ManyToOne:
				sym = '*'
			elif mult == fkeyTypes.ManyToMany:
				warn('ManyToMany relationships not supported, converting to ManyToOne for %s.%s' \
						 (className, assocEnd.getOppositeEnd().getName(TRANSLATOR_NAME)), DebugWarning)
				sym = '*'
			elif mult == fkeyTypes.OneToLots:
				warn('ManyToMany relationships not supported, converting to ManyToOne for %s.%s' \
						 (className, assocEnd.getOppositeEnd().getName(TRANSLATOR_NAME)), DebugWarning)
				sym = '*'

			name = assocEnd.getOppositeEnd().getName(TRANSLATOR_NAME)

			#Make it look pretty... calculate indentation
			indentNum = totalIndent - len(name)
			indent = " " * indentNum
			
			#Create Association Attribtues
			text.append("	+ %s:" % (name) + indent + "%s%s," \
									% (assocEnd.getOppositeEnd().getClassName(TRANSLATOR_NAME),
										 sym))

		#Remove last ','... not needed after last attribute
		text[len(text) - 1] = text[len(text) - 1].replace(',', '')
			
		text.append(");")
		text.append("")
			
	text = string.join(text, '\n')
	f = open(destination, 'w')
	f.write(text)
	f.close()
	warn("Squash Sigmoid Pseudo UML Generation Complete... Good Bye.", InfoWarning)

