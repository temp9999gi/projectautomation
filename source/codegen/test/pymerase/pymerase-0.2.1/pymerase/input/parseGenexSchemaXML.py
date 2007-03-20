"""Parses Genex 2.x Schema Definition formated XML files"""

from __future__ import nested_scopes

import os
import sys
import re
from glob import glob

import warnings
from pymerase.util.Warnings import DebugWarning
from warnings import warn

import xml.sax
import pymerase
from pymerase.ClassMembers import ModelElement
from pymerase.ClassMembers import ClassAttribute
from pymerase.ClassMembers import Association
from pymerase.ClassMembers import AssociationEnd
from pymerase.ClassMembers import ClassMetaInfo
from pymerase.ClassMembers import createAssociation

from pymerase.util.bool import parseBoolValue
from pymerase.util.PymeraseType import PymeraseType
from pymerase.output.dbAPI import fkeyTypes

import pymerase.config

from xml.sax import sax2exts, saxutils, handler, SAXNotSupportedException, SAXNotRecognizedException
from xml.sax.handler import feature_namespaces

UNDEFINED="<<undefined>>"

#############################################
# Extra classes for handling ER related concepts
class ERIndex:
  """Information about indicies
  """
  def __init__(self, pymeraseConfig, attributes):
    self.config = pymeraseConfig
    
    self.__attributes = {}
    for k, v in attributes.items():
      self.__attributes[k] = v

  def getName(self, translatorName):
    return self.__attributes[u"name"]

  def getColumnName(self, translatorName):
    mangler = self.config.getNameMangler(translatorName)
    return mangler.mangle(self.__attributes[u"column_id"])


class ERSecurity:
  """Stores information about users
  """
  def __init__(self, attributes):
    self.__attributes = {}
    for k, v in attributes.items():
      self.__attributes[k] = v

  def getUser(self):
    return self.__attributes[u"user"]

  def getPrivilege(self):
    return self.__attributes[u"privileges"]

#class ERAssociation(Association):
#  """Extension of Association for some of the extra ER related
#  concepts. (Maybe, probably needs to be refactored more)
#  """
#  def __init__(self, pymeraseConfig, name=None):
#    Association.__init__(self, pymeraseConfig, name)
#    self.__targetAttributeName = None
#
#  def setTargetAttributeName(self, value):
#    self.__targetAttributeName = value
#
#  def getTargetAttributeName(self, translatorName):
#    mangler = self.config.getNameMangler(translatorName)
#    return mangler.mangle(self.__targetAttributeName)
#    
class ERClassAttribute(ClassAttribute):
  """Extention of ClassAttribute to keep track of indexed fields
  """
  def __init__(self, pymeraseConfig, name=None):
    ClassAttribute.__init__(self, pymeraseConfig, name)
    self.__indexed = 0

  # FIXME: Do we need to know that a field is indexed
  # FIXME: if we also keep a list of ERIndex classes?
  def setIndexed(self, value):
    self.__indexed = parseBoolValue(value)

  def isIndexed(self):
    return self.__indexed
  
class ERClassMetaInfo(ClassMetaInfo):
  def __init__(self, pymeraseConfig, name=None):
    ClassMetaInfo.__init__(self, pymeraseConfig, name)
    self.__autoSequence = 0
    self.__indicies = []
    self.__security = []

  def setAutoSequence(self, value):
    """set flag to indicate if the dbAPI should auto-create primary key values
    """
    self.__autoSequence = parseBoolValue(value)

  def isAutoSequence(self):
    """check flag to indicate if the dbAPI should auto-create primary key
    values
    """
    return self.__autoSequence

  def appendIndices(self, pymeraseConfig, attributes):
    """Append list of indices to 
    """
    index = ERIndex(pymeraseConfig, attributes)
    # check to see if the field is going to automatically get an index
    column_name = index.getColumnName(None)
    column_field = self.__attributes.get(column_name, None)
    if column_field is not None :
      if column_field.isUnique():
        warn("declaring index for unique field", DebugWarning)
      elif column_field.isIndexed():
        warn("declaring index for field with index", DebugWarning)
      column_field.setIndexed(1)
    else:
      warn("index %s tried accessing field %s" % (index.getName(),column_name),
           DebugWarning)
    # tag field as being indexed, and append it to the list of indexes.
    self.__indices.append(index)

    
  def appendSecurity(self, attributes):
    """Add information about user security to table
    """
    # Override default that throws an unimplemented error
    self.__security.append(ERSecurity(attributes))

def parseGenexFKeyType(fkey_type, tableName):
  """FKeyTypes = self.__parseGenexFKeyType(fkey_type)

  return an 'ennumeration' of key types based off of xml
  """
  if fkey_type == "ONE_TO_ONE":
    return fkeyTypes.OneToOne
  elif fkey_type == "MANY_TO_ONE":
    return fkeyTypes.ManyToOne
  elif fkey_type == "LOOKUP_TABLE":
    return fkeyTypes.OneToLots
  elif fkey_type == "LINKING_TABLE":
    return fkeyTypes.ManyToMany
  else:
    err_msg = "unsupported fkey (%s) for table %s" % (fkey_type, tableName)
    raise NotImplementedError(err_msg)
  
######################################
# Parsing related components

class GenexEntityResolver(xml.sax.handler.EntityResolver):
  """Attempt to map table.dtd file to a reasonable location
  """
  def resolveEntity(self, publicId, systemId):
    """
    """
    if re.search("table\.dtd$", systemId):
      return pymerase.config.table_dtd
    return systemId
  
class GenexClassParser(xml.sax.ContentHandler):
  def __init__(self, source, pymeraseConfig, classesInModel):
    self.source_path = source
    self.pymeraseConfig = pymeraseConfig
    self.tables = classesInModel
    self.external_keys = {}
    # name of file being currently parsed
    self.current_pathname = None
    # reference to currently parsed table
    self.currentTable = None

    # create parser
    self.parser = sax2exts.make_parser()
    self.parser.setFeature(feature_namespaces, 0)
    self.parser.setContentHandler(self)
    self.parser.setEntityResolver(GenexEntityResolver())
    
  def parse(self):
    """Read a genex source files and parse into generalized internal
    representation.
    """
    files = []
    if not os.path.exists(self.source_path):
      warn("Source does not exist", RuntimeWarning)
      return 
    if os.path.isdir(self.source_path):
      files = glob(os.path.join(self.source_path, "*.xml"))
      files.sort()
    elif os.path.isfile(self.source_path):
      files.append(self.source_path)
    else:
      warn("Unrecognized file type", RuntimeWarning)
      return

    for f in files:
      try:
        self.addFile(f)
      except NotImplementedError, e:
        warn(e, RuntimeWarning)
        
    self.resolveForeignKeys()
    
  def addFile(self, pathname):
    """self.addFile(pathname)

    Given the full path and filename to a specific Genex XML table
    definition file, load it and parse it into internal representation
    """
    self.current_pathname = pathname

    # parse file
    self.parser.parse(pathname)

  def resolveForeignKeys(self):
    """Add the external foreign key links discovered by addFile to the correct tables.
    """
    for local_class_name, fkey_list in self.external_keys.items():
      for fkey in fkey_list:
        try:
          fkey.setClassToCreate(fkey.getContainingClass())
          table_to_update = fkey.getTargetClassName(None)
          warn("Adding %s to %s" % (fkey.getContainingClassName(None),
                                    table_to_update),
               DebugWarning)
          self.tables[table_to_update].addAssociation(fkey)
        except KeyError, e:
          warn("class %s doesn't exist" % (table_to_update),
               RuntimeWarning)
          warn("Was trying to parse fkey %s" % (fkey.getName()),
               RuntimeWarning)

  def verifyTable(self, table):
    """verifyTable provides a few quick sanity checks to make sure the
    table is being processed correctly
    """
    
    if table.getName(None) is None:
      return 0
    elif len(table.getAttributes()) == 0:
      return 0
    else:
      return 1
    
  ############################
  # xml processing components
  def startElement(self, name, attributes):
    """
    Function called by the xml parser for each new xml element
    """
    if name == "table":
      # construct a new table reference
      cname = attributes['name'] # cname is name of class
      # get a reference to the class we're about to fill in.
      erClass = self.tables.get(cname,
                                ERClassMetaInfo(self.pymeraseConfig, cname))
      self.currentTable = self.tables.setdefault(cname, erClass)
      self.currentTable.setDefined(1)
      self.currentTable.setName(attributes.get('name', UNDEFINED))
      self.currentTable.setType(attributes.get('type', UNDEFINED))
      self.currentTable.setDescription(attributes.get('comment', None))
      self.currentTable.appendLocation("Defined in " + self.current_pathname)
      inherits = attributes.get('inherits_from', None)
      if not (inherits is None or inherits == u"none"):
        # get a reference to the base class, constructing a placeholder
        # class if it doesn't exist.yet.
        
        # FIXME: it is possible that by constructing a base class reference
        # FIXME: out of sequence that it won't be validated properly,
        # FIXME: and if the class that caused it to be created gets
        # FIXME: rejected, there will still be a reference to the placeholder
        # FIXME: class.
        baseRef = self.tables.setdefault(inherits,
                                         ERClassMetaInfo(self.pymeraseConfig,
                                                         inherits))
        baseRef.appendLocation("Defined as a base class in "+self.current_pathname)
        self.currentTable.appendBaseClass(baseRef)
      self.currentTable.setFilename(self.current_pathname)
      #self.currentTable.setPackage(self.defaultPackage)
    elif name == "column":
      class_name = attributes.get('name', UNDEFINED)
      classAttribute = ERClassAttribute(self.pymeraseConfig)
      
      # General attribute information
      classAttribute.setDefined(1)
      classAttribute.setName(attributes.get('name', UNDEFINED))
      classAttribute.setFriendlyName(attributes.get('full_name', UNDEFINED))
      classAttribute.setType(PymeraseType(attributes.get('type', UNDEFINED)))
      classAttribute.setDescription(attributes.get('comment', UNDEFINED))
      classAttribute.setRequired(attributes.get('not_null',UNDEFINED))

      # ER specfic information
      classAttribute.setUnique(attributes.get('unique', UNDEFINED))
      classAttribute.setIndexed(attributes.get('indexed', 0))
      classAttribute.setIndexed(attributes.get('primary_key', 0))

      # store the new attribute
      self.currentTable.addAttribute(classAttribute)
    elif name == "primary_key":
      # FIXME: I don't like the storing that primary key information
      # FIXME: in both as a flag in the attribute and as the name
      # FIXME: in the ClassMetaInfo
      # FIXME:
      # FXIME: Also Jason's perl code seems to be using the primary key
      # FIXME: flag as an indicator that there should be a constraint
      # FIXME: in postgres
      # update class attribute with indication that it's the primary key
      attributeName = attributes['column_id']
      classAttribute = self.currentTable.getAttributeByName(attributeName,None)
      if classAttribute is None:
        msg = "Trying to mark attribute %s of class %s as a primary key failed"
        msg += os.linesep + "I hope it's in a base class"
        msg %= (attributeName, self.currentTable.getName(None))
        warn(msg, RuntimeWarning)
      else:
        classAttribute.setPrimaryKey(1)
        self.currentTable.setPrimaryKeyName(classAttribute.getName(None))
        self.currentTable.setAutoSequence(attributes.get('serial', 0))
    elif name == "foreign_key":
      # get name of this association & class/type ref
      thisEndType = self.currentTable
      thisName = attributes.get('local_association_name')
      if thisName is None:
        thisName = self.currentTable.getName(None)

      # get name of other end & it's class/type classref
      otherTypeName = attributes.get('foreign_table')
      if otherTypeName is None:
        raise ValueError("required xml attribute 'foreign_table' is missing")
      otherEndType = self.tables.setdefault(otherTypeName,
                                           ERClassMetaInfo(self.pymeraseConfig,
                                                           otherTypeName))
      otherEndType.appendLocation("Defined as foreign key in " + self.current_pathname)
      otherName = attributes.get('foreign_association_name')
      if otherName is None:
        otherName = otherTypeName

      warn("%s:%s <-> %s:%s" % (thisEndType.getName(None),
                                 thisName,
                                 otherEndType.getName(None),
                                 otherName),
           DebugWarning)
      #################
      # make this association end
      
      # grab a copy of the AssociationEnd from 'this' class if it exists
      # else make a new AssociationEnd
      thisAssociationEnds = thisEndType.getAssociationEnds()
      thisEnd = thisAssociationEnds.setdefault(otherName, # note uses UUID
                                            AssociationEnd(self.pymeraseConfig,
                                                           thisName))
      # finish setting up this association end
      #thisEnd.setUUID(thisUUID) # used by XMI
      thisEnd.setType(thisEndType)
      
      thisEnd.setMultiplicity(fkeyTypes.getOppositeMultiplicity(parseGenexFKeyType(attributes['fkey_type'], self.currentTable.getName(None))))
      thisEnd.setAttributeName(attributes.get('column_id', None))
      thisEnd.setNavigable(1)
      thisEnd.setHasForeignKey(1)
      
      # construct other end
      otherAssociationEnds = otherEndType.getAssociationEnds()
      otherEnd = otherAssociationEnds.setdefault(thisName,
                                            AssociationEnd(self.pymeraseConfig,
                                                           otherName))
      #otherEnd.setUUID(otherUUID)
      otherEnd.setType(otherEndType)
      otherEnd.setAttributeName(attributes.get('foreign_table_pkey', None))
      otherEnd.setMultiplicity(parseGenexFKeyType(attributes['fkey_type'], self.currentTable.getName(None)))

      # set the foreign key name in case the user is customizing it
      otherEndType.setForeignKeyName(attributes.get('column_id', None))


      association = createAssociation(self.pymeraseConfig, thisEnd, otherEnd)

    elif name == "grant":
      # currently uninterested in privledges
      self.currentTable.appendSecurity(attributes)
    elif name == "unique":
      # get the list of unique fields and set an inidcator flag
      attribute_names = attributes['column_ids']
      attribute_name_list = re.split("\s+", attribute_names)
      for attribute_name in attribute_name_list:
        classAttribute = self.currentTable.getAttributeByName(attribute_name, None)
        if classAttribute is None:
          warn("In %s attribute %s was declared unique but not found among %s" % (
            self.current_pathname,
            attribute_name,
            str(self.currentTable.getAttributeNames(None))),
            SyntaxWarning)
        else:
          classAttribute.setUnique(1)

    elif name == "index":
      self.currentTable.appendIndices(self.pymeraseConfig, attributes)
    else:
      sys.stderr.write("Element: %s(%s)\n" % ( name, str(attributes.keys()) ))

  def endElement(self, name):
    """Execute code for closing element
    """
    # store resulting table information if the table is "ok"
    if name == "table":
      if self.verifyTable(self.currentTable):
        self.tables[self.currentTable.getName(None)] = self.currentTable
        self.currentTable = None
      else:
        warn("syntax error: table %s not defined" %(self.currentTable.getName(None)),
             SyntaxWarning)


  def skippedEntity(self, entity):
    warn("skippedEntity: %s" % (entity), DebugWarning)

  def startDocument(self):
    warn("Parsing file %s" % (self.current_pathname), DebugWarning)

def read(source, pymeraseConfig, classesInModel):
  """Parse source files describing objects of interest returning the abstract
  objects
  """
  parser = GenexClassParser(source, pymeraseConfig, classesInModel)
  parser.parse()

  modelElements = parser.tables.values()

  errors = 0
  for elementName, element in parser.tables.items():
    if element.getDefined() == 0:
      errors += 1
      warn("SyntaxError: %s was not defined" % (element.getName(None)),
           RuntimeWarning)

  if errors > 0:
    raise(SyntaxError, "There were syntax errors found")
  else:
    return modelElements

# FIXME: started working on trying to provide some error handling
# FIXME: for if elements are misdefined and can't be resolved.
# FIXME: should just write some ugly test cases, and use that for the testing.
# FIXME: (Where ugly means all sorts of bad references. Then I can
# FIXME: try and make sure I output the apporpriate error messages)
