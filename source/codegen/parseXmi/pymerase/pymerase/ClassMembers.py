"""Contains classes representing meta information about the objects
that can be created by pymerase.
"""
from __future__ import nested_scopes
import copy
import os
import pprint
import types

from pymerase.util.bool import parseBoolValue
# import warning support
from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning
import pymerase.util.NameMangling
from pymerase.util.PymeraseType import PymeraseType
import warnings
from warnings import warn

from pymerase.output.dbAPI import fkeyTypes

###################
# UTILITY FUNCTIONS
from pymerase.util.iPymeraseUtil import getClassByName

def getBasePrimaryKeyName(tables, tbl, TRANSLATOR_NAME):
	"""
	Takes a list of all the table objects and a tbl object which you would like
	to retrieve the primary key (which is stored in base class
	"""
	# FIXME: implemented getBasePrimaryKeyName directly in ClassMetaInfo
	# FIXME: objects, so this function isn't needed any longer.
	warn("Call getBasePrimaryKeyName directly on ClassMetaInfo object",
			 DeprecationWarning)
	return tbl.getBasePrimaryKeyName()

def getAllAttributes(tables, tbl, TRANSLATOR_NAME):
	"""
	Takes a list of all the table objects, and a tbl object which you would like
	all the attributes from, including the attibutes from inherited base classes.

	returns attributes list
	"""
	atts = []
	if len(tbl.getBaseClassNames(TRANSLATOR_NAME)) > 0:
		for tblName in tbl.getBaseClassNames(TRANSLATOR_NAME):
			atts += getAllAttributes(tables,
															 getClassByName(tables,
																							tblName,
																							TRANSLATOR_NAME),
															 TRANSLATOR_NAME)
			atts += tbl.getAttributes()
			return atts
	else: 
		atts += tbl.getAttributes()
		return atts

#########################################################
#FIXME: Code to be used once UUIDs have been implemented#
#########################################################
#def getAllAssociationEnds(tables, tbl, TRANSLATOR_NAME):
#	"""
#	Takes a list of all the table objects, and a tbl object which you would like
#	all the associations from, including the association from inherited
#	base classes.
#
#	returns associations list
#	"""
#	assoc = {}
#	if len(tbl.getBaseClassNames(TRANSLATOR_NAME)) > 0:
#		for tblName in tbl.getBaseClassNames(TRANSLATOR_NAME):
#			assoc.update(getAllAssociationEnds(tables,
#																				 getClassByName(tables,
#																												tblName,
#																												TRANSLATOR_NAME),
#																				 TRANSLATOR_NAME))
#			assocEnds = tbl.getAssociationEnds()
#			assoc.update(assocEnds)
#			return assoc
#	else: 
#		assoc.update(tbl.getAssociationEnds())
#		return assoc


def getAllAssociationEnds(tables, tbl, TRANSLATOR_NAME):
	"""
	Takes a list of all the table objects, and a tbl object which you would like
	all the associations from, including the association from inherited
	base classes.

	returns associations list
	"""
	#FIXME: Temperary function until UUIDs are implemented
	assocList = []
	if len(tbl.getBaseClassNames(TRANSLATOR_NAME)) > 0:
		for tblName in tbl.getBaseClassNames(TRANSLATOR_NAME):
			assocList.extend(getAllAssociationEnds(tables,
																				 getClassByName(tables,
																												tblName,
																												TRANSLATOR_NAME),
																				 TRANSLATOR_NAME))
			assocList.extend(tbl.getAssociationEnds().values())
			return assocList
	else: 
		assocList.extend(tbl.getAssociationEnds().values())
		return assocList
	
###################

class ModelElement:
	"""Base interface for ClassAttribute and ClassAssociation
	"""
	def __init__(self, pymeraseConfig, name=None, ):
		self.config = pymeraseConfig

		self.setName(name)			 # setName calls NameMangler.mangle
		#self.name = name
		self.__friendlyName = None
		self.__description = None
		self.__type = None

		self.__uuid = None
		# utility
		self.__location = []
		self.__defined = 0
		
		# ER related
		self.__indexed = 0
		self.__primaryKey = 0
		
	def setName(self, value):
		self.name = value
		
	def getName(self, translatorName):
		return self.config.getNameMangler(translatorName).mangle(self.name)

	def setFriendlyName(self, value):
		self.__friendlyName = value
		
	def getFriendlyName(self):
		if self.__friendlyName is None:
			return self.name
		else:
			return self.__friendlyName

	def setDescription(self, value):
		self.__description = value
	
	def getDescription(self):
		return self.__description

	def setType(self, value):
		self.__type = value

	def getType(self):
		return self.__type

	def setUUID(self, uuid):
		if uuid is None:
			raise RuntimeError("UUID must not be None")
		
		self.__uuid = uuid
		
	def getUUID(self):
		return self.__uuid

	def appendLocation(self, location):
		"""Append a location describing where we saw this Element
		"""
		self.__location.append(location)

	def getLocations(self):
		"""Return list of locations describing where we saw this element
		"""
		return self.__location

	def setDefined(self, flag):
		"""Indicate if this model element has been fully defined

		As opposed to just having been created by a dangling association reference.
		"""
		self.__defined = flag
		
	def getDefined(self):
		"""
		"""
		return self.__defined
	
	def __str__(self):
		return str(self.__dict__)

	def getGetterName(self, translatorName):
		"""Return a getter function name conforming to whatever name mangling
		convention chosen.
		"""
		return self.config.getNameMangler(translatorName).createGetter(self.name)
	
	def getSetterName(self, translatorName):
		"""Return a setter function name conforming to whatever name mangling
		convention chosen.
		"""
		return self.config.getNameMangler(translatorName).createSetter(self.name)

	def getAppenderName(self, translatorName):
		"""Return an appender function name conforming to whatever name mangling
		convention chosen.

		Note: an appender adds more elements to an object that can contain
		multiple other objects
		"""
		return self.config.getNameMangler(translatorName).createAppender(self.name)

ATTRIBUTE_PUBLIC = 0
ATTRIBUTE_PROTECTED = 1
ATTRIBUTE_PRIVATE = 2

class ClassAttribute(ModelElement):
	"""Stores information about an attribute from the xml definition file
	and provides a standardized interface to get the elements.
	"""
	def __init__(self, pymeraseConfig, name=None):
		# add base class vars, name, type, description, friendlyName
		ModelElement.__init__(self, pymeraseConfig, name)
		self.__required = 0
		self.__unique = 0
		self.__primaryKey = 0
		self.__foreignKey = 0
		self.__access = ATTRIBUTE_PUBLIC

		self.__indexed = 0
		
	def setRequired(self, value):
		self.__required = parseBoolValue(value)
		
	def isRequired(self):
		return self.__required

	def setUnique(self, value):
		self.__unique = parseBoolValue(value)
		
	def isUnique(self):
		"""Return true if the field is going to be unique

		NOTE: primary keys are unique so return true in that case to
		"""
		return self.__unique or self.__primaryKey

	def setIndexed(self, value):
		self.__indexed = parseBoolValue(value)
		
	def isIndexed(self):
		return self.__indexed

	# FIXME: can something be a primary key and a foreign key?
	
	def setPrimaryKey(self, value):
		"""Flag this attribute as being a primary key
		"""
		flag = parseBoolValue(value)
		if self.isForeignKey() and flag:
			raise ValueError("An attribute cannot be both a primary key and a foreign key")
		else:
			self.__primaryKey = flag
		
	def isPrimaryKey(self):
		"""Does this attribute model an ER Primary key relationship
		""" 
		return self.__primaryKey

	def setForeignKey(self, value):
		"""Flag this attribute as being a foreign key
		"""
		flag = parseBoolValue(value)
		if self.isPrimaryKey() and flag:
			raise ValueError("An attribute cannot be both a primary key and a foreign key")
		else:
			self.__foreignKey = flag
		
	def isForeignKey(self):
		"""Does this attribute model an ER foreign key relationship
		"""
		return self.__foreignKey

	def isKey(self):
		"""Does this attribute model an ER key relationship
		"""
		return (self.__primaryKey or self.__foreignKey)

	def setPublicAccess(self):
		"""Indicate attribute has public access
		"""
		self.__access = ATTRIBUTE_PUBLIC

	def isPublicAccess(self):
		"""Does attribute has public access
		"""
		return self.__access == ATTRIBUTE_PUBLIC
	
	def setProtectedAccess(self):
		"""Indicate attribute has protected access
		"""
		self.__access = ATTRIBUTE_PROTECTED

	def isProtectedAccess(self):
		"""Does attribute has protected access
		"""
		return self.__access == ATTRIBUTE_PROTECTED
	
	def setPrivateAccess(self):
		"""Indicate attribute has private access
		"""
		self.__access = ATTRIBUTE_PRIVATE

	def isPrivateAccess(self):
		"""Does attribute has private access
		"""
		return self.__access == ATTRIBUTE_PRIVATE
# end class attribute


def createAssociation(pymeraseConfig, thisEnd, otherEnd, associationName=None, associationUUID=None):
	"""Helper function to create association with provided associationEnds
	"""
	# Make sure the AssociationEnds are bound to an Association
	if associationName is None:
		associationName = thisEnd.getName(None) + otherEnd.getName(None)
		
	if associationUUID is None:
		associationUUID = thisEnd.getName(None) + otherEnd.getName(None)
		
	if thisEnd.getAssociation() is None and otherEnd.getAssociation() is None:
		association = Association(pymeraseConfig, associationName)
		association.setUUID(associationUUID)
		thisEnd.setAssociation(association)
		association.addAssociationEnd(thisEnd)
		otherEnd.setAssociation(association)
		association.addAssociationEnd(otherEnd)
	# since we always construct both ends at a time is this code actually
	# needed?
	elif thisEnd.getAssociation() is None:
		association = otherEnd.getAssociation()
		thisEnd.setAssociation(association)
		association.addAssociationEnd(thisEnd)
	elif otherEnd.getAssociation() is None:
		association = thisEnd.getAssociation()
		otherEnd.setAssociation(association)
		association.addAssociationEnd(otherEnd)
	else:
		# everything is already set up
		assert thisEnd.getAssociation() == otherEnd.getAssociation()
		association = thisEnd.getAssociation()

	return association


class Association(ModelElement):
	"""Describe the meta info regarding the between two objects
	"""
	def __init__(self, pymeraseConfig, name=None):
		ModelElement.__init__(self, pymeraseConfig, name)

		if name is None:
			self.name = "anonymous association"
		else:
			self.name = name

		self.__associationEnds = []

	def addAssociationEnd(self, associationEnd):
		if len(self.__associationEnds) <= 2:
			# mark the AssociationEnd as being owned by this Association
			# we were using a dictionary to prevent multiple references
			# from being added to the associationEnd list
			#self.__associationEnds[associationEnd] = associationEnd
			self.__associationEnds.append(associationEnd)
		else:
			raise IndexError("Only allowed to have 2 AssociationEnd per Association")

	def removeAssociationEnd(self, associationEnd):
		if associationEnd in self.__associationEnds:
			self.__associationEnds.remove(associationEnd)
			associationEnd.setAssociation(None)
		else:
			raise ValueError("Attempted to remove association end that is not part"+
											 "of this association.")

	def getLinks(self):
		"""Return the list of association ends attached to this association
		"""
		#return self.__associationEnds.values()
		return self.__associationEnds

	def __len__(self):
		return len(self.__associationEnds)

	def __str__(self):
		associationName = self.getName(None)
		firstEndName = "--"
		secondEndName = "--"
		if len(self.__associationEnds) > 0:
			firstEndName = self.__association[0].getName(None)
		elif len(self.__associationEnds) > 1:
			secondEndName = self.__association[1].getName(None)
		return "Association: %s (%s, %s)" % (associationName,
																				firstEndName,
																				secondEndName)

class AssociationEnd(ModelElement):
	"""Maintain meta information each end of an association.

	
	"""
	# NOTE: association name mangled slightly is probably the _pk & _fk 
	# NOTE: values of the table
	
	def __init__(self, pymeraseConfig, name=None):
		# add base class vars, name, type, description, friendlyName
		ModelElement.__init__(self, pymeraseConfig, name)

		# point to our containing association
		self.__association = None
		
		# class references
		self.__type = None

		# status information
		self.__navigable = 0
		self.__multiplicity = None
		self.__aggregation = 0
		self.__access = ATTRIBUTE_PUBLIC

		# things to make ER easier
		# name of attribute providing the link
		self.__attributeName = "unamed_attribute"
		# define which association end has the foreign key
		self.__hasForeignKey = 0

	def __str__(self):
		return "AssociationEnd:" + pprint.pformat(self.__dict__)

	def setAssociation(self, value):
		"""set the Association this AssociationEnd is attached to
		"""
		if value is None:
			self.__association = None
		elif isinstance(value, Association):
			if self.__association != value:
				self.__association = value
		else:
			raise ValueError("expected Association type")
		
	def getAssociation(self):
		"""return the Association this AssociationEnd is attached to
		"""
		return self.__association

	def setAttributeName(self, name):
		self.__attributeName = name
		
	def getAttributeName(self, translatorName):
		"""Returns the name of the attribute this association end refers to.

		(ER Concept?)
		"""
		mangler = self.config.getNameMangler(translatorName)
		return mangler.mangle(self.__attributeName)

	def setType(self, value):
		"""Set type of this association (usually a class)
		"""
		self.__type = value

	def getType(self):
		"""return type of this association (usually a class)
		"""
		return self.__type
	
	def getClassName(self, translatorName):
		"""Returns the name of the class that is being queried.
		"""
		# FIXME: should we check to see if it exits?
		return self.__type.getName(translatorName)

	def setHasForeignKey(self, value):
		"""set to true if the class this association end is the one containing
		the foreign key
		"""
		# FIXME: how can we check to make sure that only one side has hasForeignKey
		# FIXME: set?
		self.__hasForeignKey = parseBoolValue(value)

	def hasForeignKey(self):
		"""set to true if the class this association end is the one containing
		the foreign key
		"""
		return self.__hasForeignKey
	
	def setMultiplicity(self, value):
		self.__multiplicity = value

	def getMultiplicity(self):
		return self.__multiplicity

	def setNavigable(self, value):
		self.__navigable = parseBoolValue(value)

	def isNavigable(self):
		return self.__navigable

	def getOppositeEnd(self):
		if self.__association is None or len(self.__association) == 1:
			return None
		else:
			otherEnd = filter(lambda x: x != self, self.__association.getLinks())
			if len(otherEnd) == 1:
				return otherEnd[0]
			elif len(otherEnd) == 0 and len(self.__association.getLinks()) == 2:
				# we have a self referental (object where both ends are the same
				# object. So it doesn't matter which one we return
				return self.__association.getLinks()[0]
			else:
				raise RuntimeError("association had the wrong number of links %d instead of 2" % len(self.__association.getLinks()))


	def getGetterName(self, translatorName):
		"""Return a getter function name conforming to whatever name mangling
		convention chosen.
		"""
		mangler = self.config.getNameMangler(translatorName)
		return mangler.createGetter(self.getName(translatorName))
	
	def getSetterName(self, translatorName):
		"""Return a setter function name conforming to whatever name mangling
		convention chosen.
		"""
		mangler = self.config.getNameMangler(translatorName)
		return mangler.createSetter(self.getName(translatorName))

	def getAppenderName(self, translatorName):
		"""Return an appender function name conforming to whatever name mangling
		convention chosen.

		Note: an appender adds more elements to an object that can contain
		multiple other objects
		"""
		mangler = self.config.getNameMangler(translatorName)
		return mangler.createAppender(self.getName(translatorName))

	
class ClassMetaInfo(ModelElement):
	"""Contains all the information about the database table, fields, keys,
	type, generating file, etc.
	"""
	def __init__(self, pymeraseConfig, name=None):
		# add base class vars, name, type, description
		ModelElement.__init__(self, pymeraseConfig, name)
			
		# source file for class meta info
		self.__path = None
		self.__filename = None

		# Information about this class,
		# base classes, elements contained, linked to by this class
		self.__packageName = pymeraseConfig.getDefaultPackage()
		self.__attributes = {}
		self.__attributes_order = []
		self.__associationEnds = {}

		# inheritance info
		self.__abstract = 0
		self.__baseClasses = []
		self.__rootClassName = None
		
		# things useful for ER/SQL Modules
		self.__primaryKeyName = None
		self.__primaryKeyConstructed = 0
		self.__foreignKeyName = None
#		self.__security = []
#		self.__indices = []

	def setFilename(self, pathname):
		"""Set source filename for the definition of this object
		"""
		self.__path, self.__filename = os.path.split(pathname)

	def getFilename(self):
		"""Get source filename for the definition of this object
		"""
		return self.__filename

	def setAbstract(self, value):
		self.__abstract = parseBoolValue(value)

	def isAbstract(self):
		return self.__abstract

	def setAssociationEnd(self, value):
		"""set AssociationEnd attached to this object
		"""
		if isinstance(value, AssociationEnd):
			self.__associationEnds[value.getUUID()] = value
		else:
			raise ValueError("expected AssociationEnd type")
		
	def getAssociationEnd(self, uuid):
		"""Return named association end attached to this object
		"""
		return self.__associationEnds[uuid]

	def getAssociationEnds(self):
		"""Return dictionary of associationEnds attached to this object

		(use AssociationEnd.getOppositeEnd to find out about the
		other side of this association)
		"""

		return self.__associationEnds
	

	def getAttributeByName(self, name, translatorName):
		"""Given a name return its ClassAttribute structure
		"""
		mangler = self.config.getNameMangler(translatorName)
		return self.__attributes.get(mangler.mangle(name), None)
		
	def getAttributes(self):
		"""Return list of attributes in the order declared in the object
		definition.
		"""
		return map(lambda x: self.__attributes[x], self.__attributes_order)

	def getAttributeNames(self, translatorName):
		"""Return list of attribute names
		"""
		return map(lambda x: x.getName(translatorName), self.getAttributes())

	def addAttribute(self, class_attribute, insert=0):
		"""Store field object in a way to allow random and sequential access.

		the insert flag allows placing an attribute at the head of the order
		list. (Useful for creating primary keys)
		"""
		# if we already have the attribute ignore the additional
		# addition, as when we return things in the order added
		# we'll return multiple instances
		if self.__attributes.has_key(class_attribute.getName(None)):
			return
		
		if not insert:
			self.__attributes_order.append(class_attribute.getName(None))
		else:
			self.__attributes_order.insert(0, class_attribute.getName(None))
			
		self.__attributes[class_attribute.getName(None)] = class_attribute

	def removeAttributeByName(self, attributeName):
		"""Remove attribute from class meta info
		"""
		del self.__attributes[attributeName]
		self.__attributes_order.remove(attributeName)
	def appendBaseClass(self, classToAdd):
		"""append the name of super class to the list of classes
		"""
		#FIXME: should we be following the MAGE convention of using 'add'?
		if isinstance(classToAdd, ClassMetaInfo):
			self.__baseClasses.append(classToAdd)
		else:
			raise ValueError("appendBaseClass requires an object of type"\
											 "ClassMetaInfo")

	def setBaseClasses(self, classListToReplace):
		"""Overwrite list of super classes with a new list
		"""
		if types(classlistToReplace) != types.ListType:
			raise ValueError("setBaseClass requires list")

		self.__baseClasses = None
		for c in classListToReplace:
			self.__appendBaseClass(c)

	def getBaseClasses(self):
		"""Return list of super class references
		"""
		return self.__baseClasses
	
	def getBaseClassNames(self, translatorName):
		"""Returns list of super class names
		"""
		return map(lambda x: x.getName(translatorName), self.__baseClasses)

	def setPackage(self, packageName):
		if type(packageName) == types.StringType or \
			 type(packageName) == types.UnicodeType:
			self.__packageName = packageName

	def getPackage(self):
		return self.__packageName
	
	def isRootClass(self):
		"""Return true if we don't inherit from any other class.
		"""
		return not len(self.__baseClasses)

	def getRootClass(self):
		"""Return the name of the root most class in the type hiearchy

		(Well actually the first root class found in a depth first search)
		"""
		if self.isRootClass():
			return self

		for c in self.__baseClasses:
			rootClass = c.getRootClass()
			if rootClass is not None:
				return rootClass

		return None


	##############
	# ER related methods
	def isAutoSequence(self):
		"""check flag to indicate if the dbAPI should auto-create primary key
		values
		"""
		# return true if we're a base class
		if self.isRootClass():
			return 1
		else:
			return 0

	def getBasePrimaryKeyName(self, translatorName=None):
		"""Recurse through the class hierarchy to find the primary key
		(which is only declared in the top class of a class tree)
		"""

		rootClass = self.getRootClass()
		return rootClass.getPrimaryKeyName(translatorName)

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
				if self.__primaryKeyName is None:
					# Construct a primary key object
					self.__primaryKeyName = self.name + "_pk"
					primaryKey = ClassAttribute(self.config, self.__primaryKeyName)
					primaryKey.setType(PymeraseType('serial'))
					self.addAttribute(primaryKey, insert=1)
		else:
			self.__primaryKeyName = name

		warn("Setting primary_key_name: %s" % ( self.__primaryKeyName ),
				 DebugWarning)

		# well actually this indicates that we tried to construct a key,
		# if it's not needed we don't bother trying again.
		self.__primaryKeyConstructed = 1
													 

	def getPrimaryKeyName(self, translatorName):
		"""return primary key name

		Default to user defined key otherwise use the primary key name
		of the base class.
		"""
		
		if self.__primaryKeyName is not None:
			primaryKeyName = self.__primaryKeyName
		elif self.isRootClass() and not self.__primaryKeyConstructed:
			self.setPrimaryKeyName()
			primaryKeyName = self.__primaryKeyName
		else:
			return self.getBasePrimaryKeyName(translatorName)
			
		mangler = self.config.getNameMangler(translatorName)
		return mangler.mangle(self.__primaryKeyName)

	def setPrimaryKeyConstructed(self, value):
		"""set if primary key has been constructed
		"""
		self.__primaryKeyConstructed = parseBoolValue(value)

	def isPrimaryKeyConstructed(self):
		"""indicate state of primary key construction
		"""
		return self.__primaryKeyConstructed
	
	def setForeignKeyName(self, keyName=None):
		"""Set the foreign key name that should be used for this class.
		"""
		if keyName is None:
			if self.__foreignKeyName is None:
				# Construct a primary key object
				self.__foreignKeyName = self.name + "_fk"
				self.__foreignKeyNameConstructed = 1
		else:
			self.__foreignKeyName = keyName

		warn("Setting foreign_key_name: %s" % ( self.__foreignKeyName ),
				 DebugWarning)
		return self.__foreignKeyName

	def getForeignKeyName(self, translatorName):
		"""Return the foreign key name that should be used for this class.
		"""
		mangler = self.config.getNameMangler(translatorName)
		
		if self.__foreignKeyName is not None:
			return mangler.mangle(self.__foreignKeyName)
		elif not self.isRootClass():
			 return mangler.mangle(self.setForeignKeyName())
		else:
			primaryKeyName = self.getPrimaryKeyName(translatorName)
			self.__foreignKeyName = pymerase.util.NameMangling.RelationalKey().getForeignKey(primaryKeyName)
			warn("No foreign key name set for %s, making one up %s" % (self.name,
																																 self.__foreignKeyName),
					 InfoWarning)
			return self.__foreignKeyName

		
	def getIndices(self):
		return []

	def getSecurity(self):
		return []

	def appendSecurity(self, attributes):
		"""Add information about user security to table
		"""
		raise NotImplementedError("Input module doesn't support encoding"\
															"security information")


