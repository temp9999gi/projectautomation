###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2001 by:																								 #
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
#			 Authors: Diane Trout
# Last Modified: $Date: 2007/01/01 13:36:52 $

"""Create table.dtd XML describing the objects passed to this translator.
"""
from __future__ import nested_scopes



import os
import sys
import string
import re
import types

from pymerase.util.output import *
from pymerase.output.dbAPI import fkeyTypes

import warnings
from pymerase.util.Warnings import DebugWarning
from warnings import warn

TRANSLATOR_NAME="CreateTableXML"
# Note: derived from code provided by Brandon King (fgdb2xml.py)

tableTypeList = { "DATA": "&data_table;",
									"VALIDATION": "&validation_table;",
									"SUBSET": "&subset_table;",
									"LINKING": "&linking_table;",
									"SYSTEM": "&system_table;",
									"VIEW": "&view;",
									}
	
def parseTableType(tableType):
	return tableTypeList.get(tableType, tableType)
	
def NoneStr(object):
	if object is None:
		return ""
	else:
		return str(object)

def parseCardinality(cardinality):
	if cardinality == fkeyTypes.OneToOne:
		return "&fkey_oto;"
	elif cardinality == fkeyTypes.ManyToOne:
		return "&fkey_mto;"
	elif cardinality == fkeyTypes.OneToLots:
		return "&fkey_lookup;"
	elif cardinality == fkeyTypes.ManyToMany:
		return "&fkey_linking;"
	else:
		err_msg = "unsupported fkey (%s) for table" % (cardinality)
		raise NotImplementedError(err_msg)

class XMLSchemaWriter:

	def __init__(self, tblList):

		self.classList = tblList
		
	def write(self, destination):
		destination = os.path.abspath(destination)
		if os.path.exists(destination):
			if not os.path.isdir(destination):
				msg = "%s is not a directory" % (destination)
				raise ValueError, msg
		else:
			os.mkdir(destination)

		for klass in self.classList:
			fileName = klass.getName(TRANSLATOR_NAME) + ".xml"
			filePath = os.path.join(destination, fileName)
			f = open(filePath, 'w')

#			attributeNameList = map(lambda x: x.getName(TRANSLATOR_NAME),
#															klass.getAttributes())
#			attributes = {}
#			for attribute in klass.getAttributes():
#				attributes[attribute.getName(TRANSLATOR_NAME)] = attribute
#
			associationEnds = {}
			for end in klass.getAssociationEnds().values():
				associationEnds[end.getName(TRANSLATOR_NAME)] = end
			
			doc = []
			#Add header
			doc.append("<?xml version=\"1.0\" standalone=\"no\"?>")
			doc.append("<!DOCTYPE table SYSTEM \"table.dtd\">")
			
			#Add Table Info
			doc.append("<table name=\"%s\"" % (klass.getName(TRANSLATOR_NAME)))
			doc.append("			 comment=\"%s\"" % (NoneStr(klass.getDescription())))
			baseClasses = string.join(klass.getBaseClassNames(TRANSLATOR_NAME), ', ')
			if len(baseClasses) > 0:
				doc.append("			 inherits_from=\"%s\"" % (baseClasses))
			doc.append("	>")
			
			#Add Column Info
			for attribute in klass.getAttributes(): #attributes.values():
				association = associationEnds.get(attribute.getName(TRANSLATOR_NAME),
																					None)
				doc.extend(self.createAttribute(klass, attribute, association))
				if association is not None:
					del associationEnds[attribute.getName(TRANSLATOR_NAME)]

			# write out any remaining associations (which should be the 1..*s)
			for association in associationEnds.values():
				doc.extend(self.createAssociation(association))
									 
			doc.append("</table>")

			doc = string.join(doc, os.linesep)
			f.write(doc)
			f.close()

	def createAttribute(self, klass, attribute, association):
		doc = []
		doc.append("	<column name=\"%s\"" % (attribute.getName(TRANSLATOR_NAME)))
				
		#Add full_name (friendly name)
		doc.append("			full_name=\"%s\"" % (NoneStr(attribute.getFriendlyName())))
				
		#Convert appropriate values and add type
		try:
			doc.append("			type=\"%s\"" % (attribute.getType().getSQLType()))
		except NotImplementedError, e:
			doc.append("			type=\"%s\"" % (attribute.getType().getTypeString()))
			msg = "%s has invalid type string '%s'"
			msg %= (attribute.getName(TRANSLATOR_NAME),
							attribute.getType().getTypeString())
			print msg

		#If no comment, enter empty string
		if attribute.getDescription() is None:
			doc.append("			comment=\"\"/>")
		else:
			doc.append("			comment=\"%s\"/>" % (attribute.getDescription()))

		#print klass.getName(TRANSLATOR_NAME)+": ",
		if association is not None:
			doc.extend(self.createAssociation(association))

		# FIXME: it'd be nice if this was at the end of the table element
		# FIXME: also what happens if a primary key requires multiple columns
		if attribute.isPrimaryKey():
			doc.append("	<primary_key column_id=\"%s\"/>" % (attribute.getName(TRANSLATOR_NAME)))
		return doc
	
	def createAssociation(self, thisEnd):
		#print association.getName(TRANSLATOR_NAME),
		association = []
		otherEnd = thisEnd.getOppositeEnd()
		association.append("	<foreign_key column_id=\"%s\"" % (thisEnd.getAttributeName(TRANSLATOR_NAME)))
		association.append("		 foreign_table			=\"%s\"" % (NoneStr(otherEnd.getType().getName(TRANSLATOR_NAME))))
		association.append("		 foreign_table_pkey =\"%s\"" % (NoneStr(otherEnd.getAttributeName(TRANSLATOR_NAME))))
		association.append("		 fkey_type					=\"%s\"/>" % (parseCardinality(otherEnd.getMultiplicity())))
		return association
				

#				#Handle One-to-Many linking
#				if attribute.getType() == "mto":
#					doc.append("	<foreign_key column_id=\"%s_fk\"" % (attribute.getName(TRANSLATOR_NAME)))
#					doc.append("		 foreign_table			=\"%s\"" % (attribute.getName(TRANSLATOR_NAME)))
#					doc.append("		 foreign_table_pkey =\"%s_pk\"" % (attribute.getName(TRANSLATOR_NAME)))
#					doc.append("		 fkey_type					=\"&fkey_mto;\"/>")
#
		return doc
		
def write(destination, parsedInput):
	# Write out all the individual package members
	if not os.path.exists(destination):
		os.mkdir(destination)
	elif not os.path.isdir(destination):
		msg = "PATH(%s) is not a directory!" % (destination)
		raise ValueError(msg)

	package_information = []

	writer = XMLSchemaWriter(parsedInput)
	writer.write(destination)
