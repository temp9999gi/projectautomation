# -*- coding: utf-8 -*-
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
#			 Authors: Diane Trout
# Last Modified: $Date: 2007/01/02 09:13:54 $
#
"""Attempts to load a model defined in an xmi file into pymerase.

Currently requires the novosoft uml reader, which implies the need for jython.
It was currently tested with 0.4.19 downloaded from the argo cvs.
"""
# import system packages
from __future__ import nested_scopes

import warnings
from warnings import warn
from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning

import os
import pprint
import re
import string
import tempfile
import zipfile

from smw.metamodel import UML14
from smw.metamodel import UML13
from smw.io import loadModel

from pymerase.ClassMembers import ModelElement
from pymerase.ClassMembers import ClassAttribute
from pymerase.ClassMembers import AssociationEnd
from pymerase.ClassMembers import Association
from pymerase.ClassMembers import createAssociation
from pymerase.ClassMembers import ClassMetaInfo
from pymerase.util.bool import parseBoolValue
from pymerase.util.PymeraseType import PymeraseType
from pymerase.util.NameMangling import RelationalKey
from pymerase.output.dbAPI import fkeyTypes


from umlParserDef import *

#############################################
# Extra classes for creating ER related information from an XMI file
##class XMIIndex:
##	"""Information about indicies
##	"""
##	def __init__(self, pymeraseConfig, attributes):
##		self.config = pymeraseConfig
##		
##		self.attributes = {}
##		for k, v in attributes.items():
##			self.attributes[k] = v
##
##	def getName(self, translatorName):
##		return self.attributes[u"name"]
##
##	def getColumnName(self, translatorName):
##		mangler = self.config.getNameMangler(translatorName)
##		return mangler.mangle(self.attributes[u"column_id"])
##
##
##class XMISecurity:
##	"""Stores information about users
##	"""
##	def __init__(self, attributes):
##		self.attributes = {}
##		for k, v in attributes.items():
##			self.attributes[k] = v
##
##	def getUser(self):
##		return self.attributes[u"user"]
##
##	def getPrivilege(self):
##		return self.attributes[u"privileges"]
##

class XMIAssociationEnd(AssociationEnd):
	"""Extension of AssociationEnd for some of the extra ER related
	concepts. (Maybe, probably needs to be refactored more)
	"""
	def __init__(self, pymeraseConfig, name=None):
		AssociationEnd.__init__(self, pymeraseConfig, name)
		self.setAttributeName(None)

	def getAttributeName(self, translatorName):
		mangler = self.config.getNameMangler(translatorName)
		if self.getAttributeName(translatorName) is None:
			#return "TargetAttributeName"

			# depending on our multiplicity, determine which key name to
			# return
			if self.getMultiplicity() != fkeyTypes.OneToOne: 
				attributeName = self.getType().getBasePrimaryKeyName()
			else:
				attributeName = self.getName()
				attributeName = self.getType().getRootClass().getName(None)+"_fk"
		else:
			rkey = RelationalKey()
			if self.getMultiplicity() != fkeyTypes.OneToOne:
				# FIXME: should I just always use the base class name for primary keys?
				attributeName = self.getType().getBasePrimaryKeyName()
				#attributeName = rkey.getPrimaryKey(self.attributeName)
			else:
				attributeName = rkey.getForeignKey(self.attributeName)
			
		return mangler.mangle(attributeName)

		



def addForeignKeys(pymeraseConfig, classesInModel):
	"""Given a dictionary of classes construct reasonable foreign key references.
	"""
	for c in classesInModel.values():
		convertClassAttributesToRelations(pymeraseConfig,
																			classesInModel,
																			c)
		
	for classRef in classesInModel.values():
		for thisEnd in classRef.getAssociationEnds().values():
			##########
			# FIXME: split this into a seperate phase
			##########
			# construct a foreign key attribute if needed
			thisEndType = thisEnd.getType()
			otherEnd = thisEnd.getOppositeEnd()
			otherEndType = otherEnd.getType()
			if thisEnd.getMultiplicity() != fkeyTypes.OneToOne and otherEnd.getMultiplicity() != fkeyTypes.OneToOne:
				# Handle: (or at least faily informatively about many to many)
				err = "Pymerase doesn't support Many To Many relationships"+ os.linesep
				err += "please add a linking table"
				warn(err, RuntimeWarning)
			elif otherEnd.getMultiplicity() != fkeyTypes.OneToOne:
				# Handle: one to many
				# put the key in the other end
				hasKey = otherEnd
			elif	thisEnd.getMultiplicity() != fkeyTypes.OneToOne:
				# Handle: many to one
				# put the key in this end
				hasKey = thisEnd
			else:
				if thisEnd.getUUID() <= otherEnd.getUUID():
					hasKey = thisEnd
				else:
					hasKey = otherEnd

			if hasKey == otherEnd:
				#fkeyName = thisEndType.getRootClass().getName(None) + "_fk"
				# FIXME: should we use the association name or the primary key name?
				#fkeyName = thisEndType.getRootClass().getName(None) + "_fk"
				fkeyName = thisEnd.getType().getName(None) + "_fk"
				#fkeyName = thisEnd.getAssociation().getName(None) +"_fk"
				if otherEndType.getAttributeByName(fkeyName, None) is None:
					foreignKey = constructForeignKey(pymeraseConfig,
																					 classesInModel,
																					 fkeyName)
					otherEndType.addAttribute(foreignKey)
					otherEnd.setHasForeignKey(1)
			else:
				# FIXME: should we use the association name or the primary key name?
				#fkeyName = otherEndType.getRootClass().getName(None) + "_fk"
				fkeyName = otherEnd.getType().getName(None) + "_fk"
				#fkeyName = thisEnd.getAssociation().getName(None) +"_fk"
				if thisEndType.getAttributeByName(fkeyName, None) is None:
					foreignKey = constructForeignKey(pymeraseConfig,
																					 classesInModel,
																					 fkeyName)
					thisEndType.addAttribute(foreignKey)
					thisEnd.setHasForeignKey(1)

	return classesInModel

def convertClassAttributesToRelations(pymeraseConfig, classesInModel, thisEndType):
	"""if attribute is a class convert it to a relationship
	"""
	# for all attributes
	for attribute in thisEndType.getAttributes():
		# if this attribute is actually a defined class create an association to it
		attributeType = attribute.getType()
		# check to see if our type is one of the "standard" types
		# so we don't try turning it into an association
		# FIXME: the type system of pymerase desperatly needs to be reworked.

		if attributeType.isNativeType(language="python"):
			continue

#		# Map type name to UUID:
#		for uuid, classModel in classesInModel.items():
#			if attributeType.getTypeString() == classModel.name:
#				attributeUUID = uuid
#				break
#		else:
#			warn("In %s couldn't find %s" % (
#				thisEndType.getName(None),
#				attributeType.getTypeString()),
#				RuntimeWarning)
#
		otherEndType = classesInModel.get(attribute.getUUID(), None)
		
		if otherEndType is not None:
			#print "NEED to convert %s to relation" % (attributeType)
			# construct thisEnd of the association
			thisEndName = thisEndType.getName(None)
			thisEnd = XMIAssociationEnd(pymeraseConfig, thisEndName)
			thisEnd.setUUID(thisEndName)
			thisEnd.setType(thisEndType)
			thisEnd.setMultiplicity(fkeyTypes.OneToOne)
			thisEnd.setNavigable(1)
			thisEndType.setAssociationEnd(thisEnd)

			otherEndName = attribute.getName(None)
			otherEnd = XMIAssociationEnd(pymeraseConfig, otherEndName)
			otherEnd.setUUID(otherEndName)
			otherEnd.setType(otherEndType)
			otherEnd.setMultiplicity(fkeyTypes.ManyToOne)
			otherEnd.setNavigable(1) # should we allow navigation this way?
			otherEndType.setAssociationEnd(otherEnd)

			association = createAssociation(pymeraseConfig, thisEnd, otherEnd, attribute.getName(None))
			thisEndType.removeAttributeByName(attribute.getName(None))
			# modify current attribute to be of FK type?
			#attribute.setType(PymeraseType('integer'))
			# FIXME: converting to fk type needs to have a more general solution
			#attribute.setName(attribute.getName(None) + "_fk")
		else:
			warningMessage =  """Attribute <%(getName)s> of type <%(getTypeString)s> and uuid <%(getUUID)s> in class <%(TypegetName)s> was not defined in model"""  % \
				{'getName': attribute.getName(None), 'getTypeString': attributeType.getTypeString(),
				 'getUUID': attribute.getUUID(), 'TypegetName':thisEndType.getName(None)}
			print warningMessage
			# 나중에는 아래 코멘트를 풀어야 한다.
##			warn("Attribute %s of type %s and uuid %s in class %s was not defined in model" % (
##				attribute.getName(None),
##				attributeType.getTypeString(),
##				attribute.getUUID(),
##				thisEndType.getName(None)),
##					 RuntimeWarning)

def constructForeignKey(pymeraseConfig, classesInModel, attributeName):
	"""Construct an attribute to store a foreign key
	"""
	fkey = ClassAttribute(pymeraseConfig, attributeName)
	fkey.setType(PymeraseType('int'))
	fkey.setForeignKey(1)

	return fkey


				
def parseXMI(pymeraseConfig, model, classesInModel):
	"""Convert external UML model to pymerase's model classes.
	"""
	if isinstance(model, UML13.Model):
		umlClass = UML13.Class
		umlParser = uml13Parser(pymeraseConfig)
	elif isinstance(model, UML14.Model):
		umlClass = UML14.Class
		umlParser = uml14Parser(pymeraseConfig)
	else:
		raise ValueError("Pymerase only supports UML 1.3 and 1.4 metamodel")

	#원본 classes = filter(lambda c: isinstance(c, umlClass), model.ownedElement)
	classes = filter(lambda c: isinstance(c, umlClass), model.getAllParts())
	#print classes
	#print 'model.getAllParts()',model.getAllParts()

	#---------------------------------------------------------------------------
	# parseXMI_test(pymeraseConfig, model, classesInModel)
	#---------------------------------------------------------------------------
	
	for xmiClass in classes:
		parsedClass = umlParser.parseXMIClass(classesInModel, xmiClass)
		if parsedClass is not None:
			classesInModel[parsedClass.getUUID()] = parsedClass

	addForeignKeys(pymeraseConfig, classesInModel)

	return classesInModel.values()

def parseXMI_test(pymeraseConfig, model, classesInModel):

	aAttributes = filter(lambda c: isinstance(c, UML13.Attribute), model.getAllParts())

	for attr in aAttributes:
		print 'attr.initialValue.body', attr.initialValue.body #UML:Expression body를 가지고 온다.
##		print 'attr.name', attr.name
##		print 'attr.owner', attr.owner.name
		# print 'attr.getAllParts', attr.getAllParts() 아무것도 리턴 안됨
		
		#print 'attr', dir(attr)

#	return classesInModel.values()

def read(source, pymeraseConfig, classesInModel):
	"""Parse source files describing objects of interest returning the abstract
	objects
	"""

	# Default package name is the name of the xmi file
	path, filename = os.path.split(source)
	base, ext = os.path.splitext(filename)

	# try and extract zipfile
	if zipfile.is_zipfile(source):
		# probably a zargo/zuml file
		zarchive = zipfile.ZipFile(source, 'r')
		zmodel_name = None
		for zfile in zarchive.infolist():
			if re.match(".*\.xmi$", zfile.filename):
				# have we already seen an xmi file?
				if zmodel_name is not None:
					raise RuntimeError("Unrecognized file type, too many xmi files")
				else:
					zmodel_name = zfile.filename
		if zmodel_name is None:
			raise RuntimeError("zipfile contained no XMI file")

		# save the extracted file in a way that makes smw happy
		#extracted_file = tempfile.NamedTemporaryFile(suffix=".xmi")
		extracted_name = None
		try:
			# the more secure version didn't work as I couldn't open the
			# filed
			#try:
			#	# this requires python >= 2.3 but is more secure
			#	# so worth doing.
			# extracted_fd, extracted_name = tempfile.mkstemp(suffix='.xmi', text=1)
			# os.close(extracted_fd)
			#	#extracted_file = os.fdopen(extracted_fd, 'w+b')
			# extracted_file = open(extracted_name, 'w')
			# except AttributeError, e:
			extracted_name = tempfile.mktemp(suffix='.xmi')
			extracted_file = open(extracted_name, 'w')
			extracted_file.write(zarchive.read(zmodel_name))
			extracted_file.flush()
			model = loadModel(extracted_file.name)
			extracted_file.close()
		finally:
			if extracted_name is not None:
				os.unlink(extracted_name)
	else:
		model = loadModel(source)
	#try:
	#except AttributeError, e:
	#	model = loadModel(source, UML14)

	objects = parseXMI(pymeraseConfig, model, classesInModel)

	return objects

