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
#
"""Creates SQL for creation of postgresql database"""

from __future__ import nested_scopes

import os
import sys
import re
import string
import types
from pymerase.util.output import *
from pymerase.output.dbAPI import fkeyTypes
from pymerase.util.SortMetaInfo import forwardDeclarationSort

import warnings
from pymerase.util.Warnings import DebugWarning
from warnings import warn

TRANSLATOR_NAME='CreateSQL'

def createACL(indent, objectName, users):
	"""Construct the postgres access control list for the list of users
	passed in.
	"""
	grant_format = 'GRANT %s on "%s" to "%s";'

	if users is None or len(users) == 0:
		return []
	
	acl_sql = ['REVOKE ALL on "%s" from PUBLIC;' % objectName]

	for u in users:
		if u.getPrivilege() == "ALL":
			privilege = 'ALL'
		else:
			privilege = 'SELECT'

		acl_sql.append(grant_format % (privilege,
																	 objectName,
																	 u.getUser()))

	acl_sql.append("")

	return acl_sql

def createCreateTable(indent, classMetaInfo):
	table_init_sql = []
	create_table_sql = []
	fields_sql = []

	className = classMetaInfo.getName(TRANSLATOR_NAME)
	create_table_sql.append("CREATE TABLE \"%s\" (" % className)

	# create fields
	for attribute in classMetaInfo.getAttributes():
		field_type = attribute.getType()
		if field_type.getSQLType() == "serial" and classMetaInfo.isAutoSequence():
			# Sequence should be created before it's used by the table
			# so insert the sql before the rest of the table
			# FIXME: should we check to make sure we've got an ER ClassMetaInfo
			# FIXME: for this call
			table_init_sql.extend(createSequence(0,
																					 attribute,
																					 classMetaInfo.getSecurity()))
			fields_sql.extend(createSequenceField(2, attribute))
			#fields_sql.extend(createField(2, f))
		else:
			fields_sql.extend(createField(2, attribute))

	attributeNames = map(lambda x: x.getName(TRANSLATOR_NAME),
											 classMetaInfo.getAttributes())
	# create foreign key references
	# FIXME: How do people forward declare things in SQL?
	#for association in classMetaInfo.getAssociations():
	#	associationAttributeName = association.getAssociationAttributeName(TRANSLATOR_NAME)
	#	if associationAttributeName in attributeNames:
	#		fields_sql.extend(createForeignKey(2, association))
	
	# convert fields to appropriate string, with ',' between fields
	# Not terminating fields
	if len(fields_sql) > 0:
		create_table_sql.append(string.join(fields_sql, "," + os.linesep))
	else:
		warn("Table %s has no attributes" % className, RuntimeWarning)


	# finish create table
	base=createInheritence(0,classMetaInfo.getBaseClassNames(TRANSLATOR_NAME))
	create_table_sql.append(") " + base + ";")
	
	table_sql = table_init_sql + create_table_sql

	# create ACL for field
	table_sql.extend(createACL(0, className, classMetaInfo.getSecurity()))
	table_sql.append("")
	
	return addIndentToStrings(indent, table_sql)

def createField(indent, field):
	field_sql = []
	field_type = field.getType()
	field_constraints = getFieldConstraints(field)
	field_sql.append('"%s" %s%s' % (field.getName(TRANSLATOR_NAME),
																	field_type.getSQLType(),
																	field_constraints))
	
	return addIndentToStrings(indent, field_sql)

def getFieldConstraints(field):
	options = ""
	# primary key takes precedence
	if field.isPrimaryKey():
		return " PRIMARY KEY"
	
	if field.isUnique():
		options += " UNIQUE"
	if field.isRequired():
		options += " NOT NULL"

	return options

def createForeignKey(indent, association):
	"""Create a foreign key block for the create table for an association.
	"""

	# FOREIGN KEY column REFERENCES foreign_table ( foreign_column) CASCADE
	fkey_sql = 'FOREIGN KEY ("%s") REFERENCES "%s" ( "%s" ) ON UPDATE CASCADE ON DELETE CASCADE'
	fkey_sql %= (association.getAssociationAttributeName(TRANSLATOR_NAME),
							 association.getTargetClassName(TRANSLATOR_NAME),
							 association.getTargetAttributeName(TRANSLATOR_NAME))
	
	return addIndentToStrings(indent, [fkey_sql])
	
def createIndices(indent, classMetaInfo):
	"""Given a list of indices, construct all the CREATE INDEX statements.
	"""
	index_sql = []
	indexList = classMetaInfo.getIndices()
	for index in indexList:
		index_sql.extend(createIndex(0,
																 classMetaInfo.getName(TRANSLATOR_NAME),
																 index.getName(TRANSLATOR_NAME),
																 index.getColumnName(TRANSLATOR_NAME)))
	index_sql.append("")

	assocEndList = filter(lambda ae: ae.getMultiplicity() == fkeyTypes.ManyToOne, classMetaInfo.getAssociationEnds().values())

	for assocEnd in assocEndList:
		index_sql.extend(createIndex(0,
																 classMetaInfo.getName(TRANSLATOR_NAME),
																 classMetaInfo.getName(TRANSLATOR_NAME) + '_' + \
																 assocEnd.getOppositeEnd().getType().getForeignKeyName(TRANSLATOR_NAME) + '_index',
																 assocEnd.getOppositeEnd().getType().getForeignKeyName(TRANSLATOR_NAME)))
	index_sql.append("")
	
	return addIndentToStrings(indent, index_sql)
		
def createIndex(indent, table_name, index_name, column_list):
	"""Construct CREATE INDEX statement

	the parameter column_list can either be a preformatted string for the
	sql statement, or a list that will be converted into the correct format.
		 e.g.	['col1', 'col2'] -> 'col1, col2'
	"""
	index_format = 'CREATE INDEX \"%s\" ON \"%s\" (\"%s\");'

	if type(column_list) == types.StringType:
		column_names = column_list
	else:
		column_names = string.join(column_list, ", ")

	index_sql = [ index_format % ( index_name,
																 table_name,
																 column_names)]

	return addIndentToStrings(indent, index_sql)

def createInheritence(indent, baseClassList):
	"""Construct PostgresSQL to define list of base class/tables to inherit from
	"""

	if baseClassList is None or len(baseClassList) == 0:
		return ""

	return "INHERITS (\"%s\")" % (string.join(baseClassList, ", "))


def createSequence(indent, attribute, users):
	sequence_name = getSequenceName(attribute)
	
	sequence = 'CREATE SEQUENCE "%s" start 1 increment 1 maxvalue 2147483647 '
	sequence += 'minvalue 1 cache 1;'

	sequence_sql = [sequence % (sequence_name)]
	sequence_sql.append("")

	sequence_sql.extend(createACL(0, sequence_name, users))
	
	return addIndentToStrings(indent, sequence_sql)
	
def createSequenceField(indent, attribute):
	sequence_name = getSequenceName(attribute)
	sequence_constraints = getFieldConstraints(attribute)
	sequence_format = '"%s" integer DEFAULT nextval(\'"%s"\'::text)%s'
	
	sequence = [sequence_format % (attribute.getName(TRANSLATOR_NAME),
																 sequence_name,
																 sequence_constraints)]

	return addIndentToStrings(indent, sequence)

def getSequenceName(attribute):
	return attribute.getName(TRANSLATOR_NAME) + "_seq"

def writeTable(output_stream, classMetaInfo):
	"""
	"""
	body = []
	body.extend(createCreateTable(0, classMetaInfo))
	body.extend(createIndices(0, classMetaInfo))
														
	body_string = string.join(body, os.linesep)
	output_stream.write(body_string)

def write(destination, parsedInput):
	# Write out all the individual package members
	outputStream = getOutputStream(destination)

	# it is useful for the list of classes to be sorted in such a way
	# that classes that inherit from others are later in the list.
	tables = forwardDeclarationSort(parsedInput)

	for t	in tables:
		try:
			warn("Processing %s" % t.getName(TRANSLATOR_NAME), DebugWarning)
			writeTable(outputStream, t)
		except NotImplementedError, e:
			warn("Skipping %s because: %s" % (t.getName(TRANSLATOR_NAME), str(e)),
					 RuntimeWarning)

	outputStream.close()
