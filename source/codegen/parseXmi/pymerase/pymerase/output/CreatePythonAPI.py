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
"""Creates Python API to Postgres Database"""

from __future__ import nested_scopes

# Copyright 2001, California Institute of Technology.
# ALL RIGHTS RESERVED.
#
#
#			 Authors: Diane Trout
# Last Modified: $Date: 2007/01/01 13:36:52 $

import os
import sys
import string
import re
import types
import shutil
import inspect
from pymerase.util.output import *
from pymerase.util.SortMetaInfo import forwardDeclarationSort
from pymerase.output.PythonAPI import fkeyTypes

import warnings
from pymerase.util.Warnings import DebugWarning
from warnings import warn



############################
# helper files
def getMITCopyright():
	return """
###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) %4s by:																								 #
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
""" % (str(2002))

TRANSLATOR_NAME='CreateDBAPI'
SQL_TRANSLATOR_NAME='CreateSQL'

############################
# Writer components
def createDocString(indent, description):
	doc_string = []
	if description is not None:
		description = string.strip(description)
		description = re.sub(" +", " ", description)
		#FIXME: word wrap would be nice.
		if len(description) > 0:
			doc_string.append('"""')
			doc_string.append(description)
			doc_string.append('"""')
			return addIndentToStrings(indent, doc_string)
	return None

def createHeader(indent, classMetaInfo):
	"""Create the top of the PythonAPI file
	"""

	header = []
	# FIXME: do I really need to make the modules executable?
	header.append(u"#!/usr/bin/env python")
	header.append(getMITCopyright())
	description = createDocString(0, classMetaInfo.getDescription())
	if not description is None:
		header.extend(description)
	header.append(u"")
	header.append(u"from __future__ import nested_scopes")
	header.append(u"import types")
	header.append(u"import mx.DateTime")
	header.append(u"from warnings import warn")
	# Try not to be dependent on the name of the package since
	# we have no good way of knowing that.
	# FIXME: unfortunatly we need import school to suck in DBSession
	#header.append(u"from dbAPI import *")
	header.append(u"from API import *")
#	for fkey in classMetaInfo.getAssociations():
#		foreign_class = fkey.getClassToCreateName()
#		header.append(u"import %s" % (foreign_class))
#
	for baseClass in classMetaInfo.getBaseClassNames(TRANSLATOR_NAME):
		header.append(u"from %s import %s" % (baseClass, baseClass))
		
	header.append(u"")
	
	return addIndentToStrings(indent, header)

def createClassHeader(indent, classMetaInfo):
	baseClasses = classMetaInfo.getBaseClassNames(TRANSLATOR_NAME)
	baseClasses = ['DBClass'] + baseClasses
	#baseClasses = baseClasses
	baseClassString = string.join(baseClasses, ", ")
	if len(baseClassString ) > 0:
		baseClassString = '(' + baseClassString + ')'
	header = [u"class %s%s:" % (classMetaInfo.getName(TRANSLATOR_NAME),
															baseClassString)]
	header.append(u"	table_name = \"%s\"" % (
															classMetaInfo.getName(SQL_TRANSLATOR_NAME)))
	return addIndentToStrings(indent, header)


def createClassInit(indent, classMetaInfo):
	className = classMetaInfo.getName(TRANSLATOR_NAME)
	docString = createDocString(2, classMetaInfo.getDescription())
	init = []
	init.append(u"def __init__(self, primary_key=None, db_session=None):")
	if docString is not None:
		init.extend(docString)
		
	#init.append(u"	warn('initializing %s: '+repr(self))" % (classMetaInfo.getName()))

	for baseClass in classMetaInfo.getBaseClassNames(TRANSLATOR_NAME):
		#init.append(u"	warn('initializing superclass %s')" % (baseClass))
		init.append(u"	%s.__init__(self, db_session=db_session)" % (baseClass))

	# set the db_session variable for this most sub class after
	# not initializing it for all of the base classes
	init.append(u"	DBClass.__init__(self, db_session)")
	for f in classMetaInfo.getAttributes():
		# FIXME: we need to make sure there's no unparasable characters in
		# FIXME: columns
		try:
			init.append(u"	self.attributes[\"%s\"] = Attribute(\"%s\", %s, \"%s\")" %(
				f.getName(SQL_TRANSLATOR_NAME),
				f.getName(SQL_TRANSLATOR_NAME),
				f.getType().getPythonTypeStr(),
				f.getFriendlyName()
				))
		except KeyError, e:
			warn(str(f), RuntimeWarning)
			raise KeyError(e)
	for fkey in classMetaInfo.getAssociations():
		try:
			# come up with a name for the class reference made harder
			# if we're declaring the reference within the class we're refering to
			class_reference = fkey.getClassToCreateName(TRANSLATOR_NAME)
			if fkey.getClassToCreateName(TRANSLATOR_NAME) != className:
				init.append(u"	import %s" % (class_reference))
				class_reference = class_reference + "." + class_reference

			init.append(u"	self.associations[\"%s\"] = Association(\"%s\", \"%s\", \"%s\", \"%s\", %s, self, %s)" %(
				fkey.getClassToCreateName(SQL_TRANSLATOR_NAME),
				fkey.getAssociationAttributeName(SQL_TRANSLATOR_NAME),
				fkey.getContainingClassName(SQL_TRANSLATOR_NAME),
				fkey.getTargetClassName(SQL_TRANSLATOR_NAME),
				fkey.getTargetAttributeName(SQL_TRANSLATOR_NAME),
				fkey.getCardinality(),
				class_reference
				))
		except KeyError, e:
			warn(str(fkey), RuntimeWarning)
			raise KeyError(e)

	init.append("	if self.db_session is not None:")
	init.append("		self.connect()")
	init.append("	if primary_key is not None:")
	init.append("		self.loadSelf(primary_key)")
	#init.append(u"	warn('finished init %s')" % (
	#								 classMetaInfo.getName(TRANSLATOR_NAME)))
	init.append(u"")
	
	return addIndentToStrings(indent, init)

def createUtilityAccessors(indent, classMetaInfo):
	"""Create member functions for returning information
	not directly stored in the database
	"""
	utilities = []

	classIdentifier = classMetaInfo.getPrimaryKeyName(SQL_TRANSLATOR_NAME)

	if classIdentifier is not None:
		utilities.append(u"def getPrimaryKeyName(self):")
		utilities.append(u"	return '%s'" % (classIdentifier))
		utilities.append(u"")

	return addIndentToStrings(indent, utilities)

def createAccessors(indent, fields):
	# FIXME: accessors shouldn't allow modifying primary key.
	# FIXME: or at least doing so should load a different record
	accessors = []
	for f in fields:
		description = createDocString(indent, f.getDescription())
		accessors.append(u"def %s(self):" % ( f.getGetterName(TRANSLATOR_NAME) ))
		if description is not None:
			accessors.extend(description)
		sqlName = f.getName(SQL_TRANSLATOR_NAME)
		accessors.append(u"	return self.attributes[\"%s\"].value" % ( sqlName ))
		accessors.append(u"")
		accessors.append(u"def %s(self, value): " % (
																		 f.getSetterName(TRANSLATOR_NAME) ))
		if description is not None:
			accessors.extend(description)
		accessors.append(u"	self.attributes[\"%s\"].setValue(value)" % ( sqlName ))
		accessors.append(u"")

	return addIndentToStrings(indent, accessors)

def createLinks(indent, foreignKeys):
	"""Construct functions to construct objects our current table is linked to.
	"""
	# FIXME: we should cache the object we created for update abilities.
	
	object_refs = []
	for fkey in foreignKeys:
		# define getter
		object_refs.append(u"def %s(self):" %(fkey.getGetterName(TRANSLATOR_NAME)))

		sqlClassName = fkey.getClassToCreateName(SQL_TRANSLATOR_NAME)
		object_refs.append(u"	link = self.associations['%s']" % (sqlClassName))
		object_refs.append(u"	return link.getObjects()")
		object_refs.append(u"")

		# define setter
		if fkey.getCardinality() == fkeyTypes.OneToOne:
			setterName = fkey.getSetterName(TRANSLATOR_NAME)
		else:
			setterName = fkey.getAppenderName(TRANSLATOR_NAME)
		
		object_refs.append(u"def %s(self, object):" % (setterName))
		object_refs.append(u"	link = self.associations['%s']" % (sqlClassName))
		object_refs.append(u"	link.appendObjects(object)")
		object_refs.append(u"")

		# should there be a remove?

	return addIndentToStrings(indent, object_refs)

#######################################
# Output Translater Interface

def writeClass(destination, classMetaInfo):
	"""
	"""
	class_name = classMetaInfo.getName(TRANSLATOR_NAME)
	class_links = classMetaInfo.getAssociations()
	class_fields =	classMetaInfo.getAttributes()
	class_filename = classMetaInfo.filename

	# FIXME: the second element in this tuple needs to contain the package
	# FIXME: name
	package_name = classMetaInfo.getPackage()
	if package_name is not None:
		package_name += '.'
	else:
		package_name = ""
		
	package_name += class_name
	package_information = (class_name, package_name)

	output_stream = getOutputStream(destination, class_name, ".py")
	
	body = []
	body.extend(createHeader(0, classMetaInfo))
	body.extend(createClassHeader(0, classMetaInfo))
	body.extend(createClassInit(2, classMetaInfo))
	body.extend(createUtilityAccessors(2, classMetaInfo))
	body.extend(createAccessors(2, class_fields))
	body.extend(createLinks(2, class_links))
	
	body_string = string.join(body, os.linesep)
	output_stream.write(body_string)

	return package_information

def parsePackageInformation(packageInformation):
	def createImports(packageInformation):
		module_list = []
		for moduleName, modulePath in packageInformation:
			module_list += ["import %s" % (modulePath)]
		return string.join(module_list, os.linesep)

	def createModuleToClassList(packageInformation):
		module_list = ""
		
		for moduleName, packagePath in packageInformation:
			if type(packagePath) == types.ListType:
				modulePath = packagePath
			else:
				modulePath = [packagePath]
			modulePath.extend([moduleName])
			
			module_list += "('%s', %s), " % (moduleName, string.join(modulePath,'.'))
		return '['+module_list+']'
	
	package_macros = {}

	package_macros['IMPORT_MODULES'] = createImports(packageInformation)
	package_macros['MODULES'] = createModuleToClassList(packageInformation)

	return package_macros

def writeTemplateFile(package_macros, source_filename, destination_filename):
	# Get file handles
	source_file = open(source_filename)
	destination_file = open(destination_filename, "w")

	# start copying replacing any template information
	macro_re = re.compile("%%([A-Za-z0-9_]*)%%")
	for line in source_file.xreadlines():
		macro_match = macro_re.search(line)
		if macro_match is not None:
			macro = macro_match.group(1)
			replacement = package_macros.get(macro, None)
			if replacement is not None:
				line = re.sub("%%"+macro+"%%", replacement, line)
		destination_file.write(line)

	source_file.close()
	destination_file.close()
	
def writePackage(destination, package_information):
	# write the package definition
	module_pathname = inspect.getabsfile(writePackage)
	module_path, module_filename = os.path.split(module_pathname)

	warn("module_pathname: %s" % (module_pathname), DebugWarning)
	
	# parse package information
	package_macros = parsePackageInformation(package_information)

	# get module_path
	# FIXME: this is for the better segmented version
	files_to_copy = [('API.py', 'API.py'),
									 ('init.py', '__init__.py'),
									 ('fkeyTypes.py', 'fkeyTypes.py')]
#	files_to_copy = [('dbAPI.py', '__init__.py'),
#									 ('fkeyTypes.py', 'fkeyTypes.py')]
	# Get filenames
	for source_filename, destination_filename	in files_to_copy:
		source_pathname = os.path.join(module_path, "PythonAPI", source_filename)
		destination_pathname = os.path.join(destination, destination_filename)

		writeTemplateFile(package_macros, source_pathname, destination_pathname)

	# Create dummy init
	#destination_file = open(os.path.join(module_path, "__init__.py"), "w")
	#destination_file.close()
	
	
def write(destination, parsedInput):
	# Write out all the individual package members

	if not os.path.exists(destination):
		os.mkdir(destination)
	elif not os.path.isdir(destination):
		msg = "PATH(%s) is not a directory!" % (destination)
		raise ValueError(msg)

	# it is useful for the list of classes to be sorted in such a way
	# that classes that inherit from others are later in the list.
	tables = forwardDeclarationSort(parsedInput)


	package_information = []
	for t in tables:
		try:
			package_information.append(writeClass(destination, t))
		except NotImplementedError, e:
			warn("Skipping %s" % ( t.getName() ), DebugWarning)

	writePackage(destination, package_information)
