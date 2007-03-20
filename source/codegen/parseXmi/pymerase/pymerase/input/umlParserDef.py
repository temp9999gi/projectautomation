# -*- coding: utf-8 -*-
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

import warnings
from warnings import warn
from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning

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

#import pymerase.input.parseXMI
#from pymerase.input.parseXMI import XMIClassMetaInfo

#from pymerase.input.parseXMI import *
#from pymerase.input.parseXMI import XMIClassMetaInfo
#from parseXMI import *



##class XMIClassAttribute(ClassAttribute):
##	"""Extention of ClassAttribute to keep track of indexed fields
##	"""
##	def __init__(self, pymeraseConfig, name=None):
##		ClassAttribute.__init__(self, pymeraseConfig, name)
##		self.indexed = 0
##
##	# FIXME: Do we need to know that a field is indexed
##	# FIXME: if we also keep a list of ERIndex classes?
##	def setIndexed(self, value):
##		self.indexed = parseBoolValue(value)
##
##	def isIndexed(self):
##		return self.indexed

class XMIClassMetaInfo(ClassMetaInfo):
	def __init__(self, pymeraseConfig, name=None):
		ClassMetaInfo.__init__(self, pymeraseConfig, name)

	def getAttributeByName(self, name, translatorName):
		"""Given a name return its ClassAttribute structure
		"""
		if not self.isPrimaryKeyConstructed():
			self.setPrimaryKeyName()

		return ClassMetaInfo.getAttributeByName(self, name, translatorName)

	def getAttributes(self):
		"""Return list of attributes in the order declared in the object
		definition.
		"""
		if not self.isPrimaryKeyConstructed():
			self.setPrimaryKeyName()

		return ClassMetaInfo.getAttributes(self)

	def isAutoSequence(self):
		# since all XMI classes have an auto-assigned sequence
		# always return true
		return 1

	def setPrimaryKeyName(self, name=None):
		"""Indicate what field in the table should be the primary key.
		If name is none, construct a reasonable primary key name.

		NOTE: The logic to determine if we need a primary key does
		NOTE: require that the class hierarchy be built
		NOTE: So this should only be called after everything is constructed
		"""

		# FIXME: we need to make sure that the dynamically constructed
		# FIXME: key is deleted if a new key is constructed.

		if name is None:
			if self.isRootClass():
				# we need to construct a primary key, since we're the base class
				# FIXME: we also need to allow the user some method of defining
				# FIXME: the primary key name
				if self._ClassMetaInfo__primaryKeyName is None:
					# Construct a primary key object
					self.setPrimaryKeyName(self.getName(None) + "_pk")
					#self.setPrimaryKeyName("_id") # for sigmoid
					primaryKey = ClassAttribute(self.config, self._ClassMetaInfo__primaryKeyName)
					primaryKey.setType(PymeraseType('serial'))
					primaryKey.setPrimaryKey(1)
					#primaryKey.setPrivateAccess() # for sigmoid
					self.addAttribute(primaryKey, insert=1)
		else:
			self._ClassMetaInfo__primaryKeyName = name

		warn("Setting primary_key_name: %s" % ( self._ClassMetaInfo__primaryKeyName ),
				 DebugWarning)

		# well actually this indicates that we tried to construct a key,
		# if it's not needed we don't bother trying again.
		self.setPrimaryKeyConstructed(1)


##	def appendIndices(self, pymeraseConfig, attributes):
##		"""Append list of indices to
##		"""
##		index = XMIIndex(pymeraseConfig, attributes)
##		# check to see if the field is going to automatically get an index
##		column_name = index.getColumnName()
##		column_field = self.__attributes.get(column_name, None)
##		if column_field is not None :
##			if column_field.isUnique():
##				warn("declaring index for unique field", DebugWarning)
##			elif column_field.isIndexed():
##				warn("declaring index for field with index", DebugWarning)
##			column_field.setIndexed(1)
##		else:
##			warn("index %s tried accessing field %s" % (index.getName(),column_name),
##					 DebugWarning)
##		# tag field as being indexed, and append it to the list of indexes.
##		self.__indices.append(index)
##
##	def getIndices(self):
##		return self.__indices
##
##	def getSecurity(self):
##		return self.__security
##
##	def appendSecurity(self, attributes):
##		"""Add information about user security to table
##		"""
##		self.__security.append(XMISecurity(attributes))

# End extended classes
###########################
class ParseError(Exception):
	pass



class umlParser:
	def __init__(self, pymeraseConfig):
		self.pymeraseConfig = pymeraseConfig
		
	def parseXMIMultiplicity(self, multiplicity, tableName):
		"""FKeyTypes = self.__parseGenexFKeyType(fkey_type)
	
		return an 'ennumeration' of key types based off of xml
		"""
		#print tableName, fkey_type
		lower = multiplicity.range[0].lower
		upper = multiplicity.range[0].upper
		if lower == 0 or lower == 1:
			if upper == 1:
				return fkeyTypes.OneToOne
			else:
				return fkeyTypes.ManyToOne
		elif lower == -1 and upper == -1:
			return fkeyTypes.ManyToMany
		else:
			err_msg = "unsupported fkey (%s) for association %s" % (fkey_type,
																															tableName)
			raise NotImplementedError(err_msg)
	
		raise ValueError("Bad parse logic")

	def parseXMIFeature(self, classesInModel, feature):
		name = feature.name
		warn("	Parsing feature %s" % (name), DebugWarning)
	
		classFeature = ClassAttribute(self.pymeraseConfig, name)
		
		try:
			featureType = feature.type
		except AttributeError:
			featureType = ''

		try:
			myFeatureName = featureType.name
		except AttributeError:
			myFeatureName = ''

		classFeature.setType(PymeraseType(myFeatureName))
		classFeature.setUUID( self.getUUID( featureType ))

		# FIXME: What else to set?
													 
		return classFeature

	def parseXMIClass(self, classesInModel, xmiClass):
		name = xmiClass.name
		UUID = self.getUUID(xmiClass)
		warn("Parsing class %s" % (name), DebugWarning)
	
		# FIXME: bad hack to ignore garbage provided by NSUML
		# FIXME: perhaps we should ignore things that are part of the java package?
		#if name == "String":
		#	warn("Skipping String", DebugWarning)
		#	return None
	
		classMetaInfo = classesInModel.setdefault(UUID,
			 		XMIClassMetaInfo(self.pymeraseConfig, name))
		classMetaInfo.setUUID(UUID)
		classMetaInfo.setAbstract(xmiClass.isAbstract)
		classMetaInfo.setPackage(xmiClass.namespace.name)
		# add in all the potential base classes
		for generalization in xmiClass.generalization:
			baseClassName = generalization.parent.name
			baseClassUUID = self.getUUID(generalization.parent)
			baseClassRef = classesInModel.setdefault(baseClassUUID,
						 XMIClassMetaInfo(self.pymeraseConfig,
															baseClassName))
			baseClassRef.setUUID(baseClassUUID)
			classMetaInfo.appendBaseClass(baseClassRef)
		
		# documentation strings are apparently optional
		# FIXME: why is the documentation a list?
		# FIXME: should I do more than just concatinate the list?
		documentation = string.join(xmiClass.comment, os.linesep)
		if documentation is not None and len(documentation) > 0:
			classMetaInfo.setDescription(string.join(documentation, os.linesep))
	
		for feature in xmiClass.feature:
			#if not isinstance(attribute, uml.foundation.core.MAttribute):
			#	raise ParseError("NSUML Returned a feature that was not a MAttribute")
	
			classMetaInfo.addAttribute(self.parseXMIFeature(classesInModel, feature))

		for association in self.getAssociationEnds(xmiClass):
			self.parseXMIAssociation(classesInModel, classMetaInfo, association)
	#		classMetaInfo.addAssociation(parseXMIAssociation(pymeraseConfig,
	#																										 classesInModel,
	#																										 classMetaInfo,
	#																										 association))
	#
		return classMetaInfo


	def parseXMIAssociation(self, classesInModel, classMetaInfo, end):
		thisName = end.name
		thisUUID = self.getUUID(end)
		otherName = self.getOppositeEnd(end).name
		otherUUID = self.getUUID(self.getOppositeEnd(end))
		associationName = end.association.name
		associationUUID = self.getUUID(end.association)
	
		associationNameTuple = (associationName, thisName, otherName)
		warn("	Parsing association %s (%s, %s)" % associationNameTuple,
				 DebugWarning)
		
		# get names of types
		thisEndTypeName = self.getEndClassName(end)
		thisEndTypeUUID = self.getUUID(self.getEndClass(end))
		otherEndTypeName = self.getEndClassName(self.getOppositeEnd(end))
		otherEndTypeUUID = self.getUUID(self.getEndClass(self.getOppositeEnd(end)))
	
		# get references to type objects from the master class list
		thisEndType = classesInModel.setdefault(thisEndTypeUUID,
																						XMIClassMetaInfo(self.pymeraseConfig,
																														 thisEndTypeName))
		thisEndType.setUUID(thisEndTypeUUID)
		otherEndType = classesInModel.setdefault(otherEndTypeUUID,
																						 XMIClassMetaInfo(self.pymeraseConfig,
																															otherEndTypeName))
		otherEndType.setUUID(otherEndTypeUUID)
	
		#################
		# make this association end
		
		# grab a copy of the AssociationEnd from 'this' class if it exists
		# else make a new AssociationEnd
		thisAssociationEnds = thisEndType.getAssociationEnds()
		thisEnd = thisAssociationEnds.setdefault(thisUUID,
				XMIAssociationEnd(self.pymeraseConfig,
								 thisName))
		# finish setting up this association end
		thisEnd.setUUID(thisUUID)
		thisEnd.setType(thisEndType)
		thisEnd.setAttributeName(associationName)
		thisEndType.setAssociationEnd(thisEnd)
		thisEnd.setMultiplicity(self.parseXMIMultiplicity(end.multiplicity,
												thisEndTypeName))
		thisEnd.setNavigable(end.isNavigable)
	
		#########
		# fill in a minimalist other end
		
		# grab a copy of the associationEnd from 'other' class if it exists
		# else make a new AssociationEnd
		otherAssociationEnds = otherEndType.getAssociationEnds()
		otherEnd = otherAssociationEnds.setdefault(otherUUID,
							 XMIAssociationEnd(self.pymeraseConfig,
																 otherName))
		otherEnd.setUUID(otherUUID)
		otherEnd.setType(otherEndType)
		otherEnd.setAttributeName(associationName)

		otherEnd.setMultiplicity(self.parseXMIMultiplicity(self.getOppositeEnd(end).multiplicity, otherEnd.getName(None)))
		otherEndType.setAssociationEnd(otherEnd)
		
		association = createAssociation(self.pymeraseConfig,
													thisEnd,
													otherEnd,
													associationName,
													associationUUID)
		
		return thisEnd

	def getOppositeEnd(self, associationEnd):
		"""Given an association end go find the other end
		"""
		association = associationEnd.association.connection
		for end in association:
			if end is not associationEnd:
				return end
		else:
			raise RuntimeError("Couldn't find opposite end")

	def getUUID(self, model_element):
		"""Return the unique id of a UML model element
		"""
##		if model_element.__uniqueID__ is None:
##			raise RuntimeError("UUID was none")
		try:
			out = model_element.__uniqueID__
		except AttributeError:
			out = ''
			
		return out
			


class uml13Parser(umlParser):
	"""Utility functions for accessing a model using UML 1.3 naming conventions
	"""
	def getAssociationEnds(self, xmiClass):
		"""Get the list of association ends attached to xmiClass
		"""
		return xmiClass.associationEnd
	
	def getEndClassName(self, associationEnd):
		"""Get the name of the Class containing this Association End
		"""
		return associationEnd.type.name
	
	def getEndClass(self, associationEnd):
		"""Get the class referenced by this association end
		"""
		return associationEnd.type
	
class uml14Parser(umlParser):
	"""Utility functions for accessing a model using UML 1.4 naming conventions
	"""
	def getAssociationEnds(self, xmiClass):
		"""Get the list of association ends attached to xmiClass
		"""
		return xmiClass.association
	
	def getEndClassName(self, associationEnd):
		"""Get the name of the Class containing this Association End
		"""
		return associationEnd.participant.name

	def getEndClass(self, associationEnd):
		"""Get the class referenced by this association end
		"""
		return associationEnd.participant
	