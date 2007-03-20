###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2002 by:                                                 #
#    * California Institute of Technology                                 #
#                                                                         #
#    All Rights Reserved.                                                 #
#                                                                         #
# Permission is hereby granted, free of charge, to any person             #
# obtaining a copy of this software and associated documentation files    #
# (the "Software"), to deal in the Software without restriction,          #
# including without limitation the rights to use, copy, modify, merge,    #
# publish, distribute, sublicense, and/or sell copies of the Software,    #
# and to permit persons to whom the Software is furnished to do so,       #
# subject to the following conditions:                                    #
#                                                                         #
# The above copyright notice and this permission notice shall be          #
# included in all copies or substantial portions of the Software.         #
#                                                                         #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,         #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF      #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                   #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS     #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN      #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN       #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE        #
# SOFTWARE.                                                               #
###########################################################################
#
#       Authors: Diane Trout
# Last Modified: $Date: 2006/12/18 15:54:02 $
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



#############################################
# Extra classes for creating ER related information from an XMI file
##class XMIIndex:
##  """Information about indicies
##  """
##  def __init__(self, pymeraseConfig, attributes):
##    self.config = pymeraseConfig
##    
##    self.attributes = {}
##    for k, v in attributes.items():
##      self.attributes[k] = v
##
##  def getName(self, translatorName):
##    return self.attributes[u"name"]
##
##  def getColumnName(self, translatorName):
##    mangler = self.config.getNameMangler(translatorName)
##    return mangler.mangle(self.attributes[u"column_id"])
##
##
##class XMISecurity:
##  """Stores information about users
##  """
##  def __init__(self, attributes):
##    self.attributes = {}
##    for k, v in attributes.items():
##      self.attributes[k] = v
##
##  def getUser(self):
##    return self.attributes[u"user"]
##
##  def getPrivilege(self):
##    return self.attributes[u"privileges"]
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

    
##class XMIClassAttribute(ClassAttribute):
##  """Extention of ClassAttribute to keep track of indexed fields
##  """
##  def __init__(self, pymeraseConfig, name=None):
##    ClassAttribute.__init__(self, pymeraseConfig, name)
##    self.indexed = 0
##
##  # FIXME: Do we need to know that a field is indexed
##  # FIXME: if we also keep a list of ERIndex classes?
##  def setIndexed(self, value):
##    self.indexed = parseBoolValue(value)
##
##  def isIndexed(self):
##    return self.indexed
  
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
                           

##  def appendIndices(self, pymeraseConfig, attributes):
##    """Append list of indices to 
##    """
##    index = XMIIndex(pymeraseConfig, attributes)
##    # check to see if the field is going to automatically get an index
##    column_name = index.getColumnName()
##    column_field = self.__attributes.get(column_name, None)
##    if column_field is not None :
##      if column_field.isUnique():
##        warn("declaring index for unique field", DebugWarning)
##      elif column_field.isIndexed():
##        warn("declaring index for field with index", DebugWarning)
##      column_field.setIndexed(1)
##    else:
##      warn("index %s tried accessing field %s" % (index.getName(),column_name),
##           DebugWarning)
##    # tag field as being indexed, and append it to the list of indexes.
##    self.__indices.append(index)
##
##  def getIndices(self):
##    return self.__indices
##
##  def getSecurity(self):
##    return self.__security
##
##  def appendSecurity(self, attributes):
##    """Add information about user security to table
##    """
##    self.__security.append(XMISecurity(attributes))

# End extended classes
###########################
class ParseError(Exception):
  pass


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
      elif  thisEnd.getMultiplicity() != fkeyTypes.OneToOne:
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

#    # Map type name to UUID:
#    for uuid, classModel in classesInModel.items():
#      if attributeType.getTypeString() == classModel.name:
#        attributeUUID = uuid
#        break
#    else:
#      warn("In %s couldn't find %s" % (
#        thisEndType.getName(None),
#        attributeType.getTypeString()),
#        RuntimeWarning)
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
      warn("Attribute %s of type %s and uuid %s in class %s was not defined in model" % (
        attribute.getName(None),
        attributeType.getTypeString(),
        attribute.getUUID(),
        thisEndType.getName(None)),
           RuntimeWarning)           

def constructForeignKey(pymeraseConfig, classesInModel, attributeName):
  """Construct an attribute to store a foreign key
  """
  fkey = ClassAttribute(pymeraseConfig, attributeName)
  fkey.setType(PymeraseType('int'))
  fkey.setForeignKey(1)

  return fkey

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
    warn("  Parsing feature %s" % (name), DebugWarning)
  
    classFeature = ClassAttribute(self.pymeraseConfig, name)
    featureType = feature.type
    classFeature.setType(PymeraseType(featureType.name))
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
    #  warn("Skipping String", DebugWarning)
    #  return None
  
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
      #  raise ParseError("NSUML Returned a feature that was not a MAttribute")
  
      classMetaInfo.addAttribute(self.parseXMIFeature(classesInModel, feature))

    for association in self.getAssociationEnds(xmiClass):
      self.parseXMIAssociation(classesInModel, classMetaInfo, association)
  #    classMetaInfo.addAssociation(parseXMIAssociation(pymeraseConfig,
  #                                                     classesInModel,
  #                                                     classMetaInfo,
  #                                                     association))
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
    warn("  Parsing association %s (%s, %s)" % associationNameTuple,
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
    if model_element.__uniqueID__ is None:
      raise RuntimeError("UUID was none")

    return model_element.__uniqueID__
      


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

  classes = filter(lambda c: isinstance(c, umlClass), model.ownedElement)

  for xmiClass in classes:
    parsedClass = umlParser.parseXMIClass(classesInModel, xmiClass)
    if parsedClass is not None:
      classesInModel[parsedClass.getUUID()] = parsedClass

  addForeignKeys(pymeraseConfig, classesInModel)

  return classesInModel.values()

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
      #  # this requires python >= 2.3 but is more secure
      #  # so worth doing.
      # extracted_fd, extracted_name = tempfile.mkstemp(suffix='.xmi', text=1)
      # os.close(extracted_fd)
      #  #extracted_file = os.fdopen(extracted_fd, 'w+b')
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
  #  model = loadModel(source, UML14)

  objects = parseXMI(pymeraseConfig, model, classesInModel)

  return objects

