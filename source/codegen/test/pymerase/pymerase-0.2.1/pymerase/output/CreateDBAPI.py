###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) 2001 by:                                                 #
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
"""Creates Python API to Postgres Database"""

from __future__ import nested_scopes

# Copyright 2001, California Institute of Technology.
# ALL RIGHTS RESERVED.
#
#
#       Authors: Diane Trout
# Last Modified: $Date: 2006/12/18 15:54:02 $

import os
import sys
import string
import re
import types
import shutil
from pymerase.util.Template import Template
from pymerase.util.output import *
from pymerase.util.SortMetaInfo import forwardDeclarationSort
from pymerase.util.Template import Template
from pymerase.output.dbAPI import fkeyTypes

import warnings
from pymerase.util.Warnings import DebugWarning
from warnings import warn



############################
# helper files
def getMITCopyright():
  return """
###########################################################################
#                                                                         #
# C O P Y R I G H T   N O T I C E                                         #
#  Copyright (c) %4s by:                                                 #
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
  header.append(u"from bool import Bool")
  header.append(u"import mx.DateTime")
  header.append(u"from warnings import warn")
  # Try not to be dependent on the name of the package since
  # we have no good way of knowing that.
  # FIXME: unfortunatly we need import school to suck in DBSession
  #header.append(u"from dbAPI import *")
  header.append(u"from dbAPI import *")
#  for fkey in classMetaInfo.getAssociations():
#    foreign_class = fkey.getClassToCreateName()
#    header.append(u"import %s" % (foreign_class))
#
  for baseClass in classMetaInfo.getBaseClassNames(TRANSLATOR_NAME):
    header.append(u"from %s import %s" % (baseClass, baseClass))

  header.append(u"")
  header.append(u"def getPrimaryKeyName():")
  header.append(u"  return '%s'" % (classMetaInfo.getPrimaryKeyName(SQL_TRANSLATOR_NAME)))
  header.append(u"")
  header.append(u"def getForeignKeyName():")
  header.append(u"  return '%s'" % (classMetaInfo.getForeignKeyName(SQL_TRANSLATOR_NAME)))
  header.append(u"")
  header.append(u"def getClass():")
  header.append(u"  return %s" % (classMetaInfo.getName(TRANSLATOR_NAME)))
  header.append(u"")
  header.append(u"def getTableName():")
  header.append(u"  return \"%s\"" % (classMetaInfo.getName(SQL_TRANSLATOR_NAME)))
  header.append(u"")
  header.append(u"def getClassName():")
  header.append(u"  return \"%s\"" % (classMetaInfo.getName(TRANSLATOR_NAME)))
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
  header.append(u"  table_name = \"%s\"" % (
                              classMetaInfo.getName(SQL_TRANSLATOR_NAME)))
  return addIndentToStrings(indent, header)


def createClassInit(indent, classMetaInfo):
  className = classMetaInfo.getName(TRANSLATOR_NAME)
  docString = createDocString(2, classMetaInfo.getDescription())
  init = []
  init.append(u"def __init__(self, primary_key=None, db_session=None):")
  if docString is not None:
    init.extend(docString)
    
  #init.append(u"  warn('initializing %s: '+repr(self))" % (classMetaInfo.getName()))

  for baseClass in classMetaInfo.getBaseClassNames(TRANSLATOR_NAME):
    #init.append(u"  warn('initializing superclass %s')" % (baseClass))
    init.append(u"  %s.__init__(self, db_session=db_session)" % (baseClass))

  # set the db_session variable for this most sub class after
  # not initializing it for all of the base classes
  init.append(u"  DBClass.__init__(self, db_session)")
  for f in classMetaInfo.getAttributes():
    # FIXME: we need to make sure there's no unparasable characters in
    # FIXME: columns
    try:
      init.append(u"  self.fields[\"%s\"] = Field(\"%s\", %s, \"%s\")" %(
        f.getName(SQL_TRANSLATOR_NAME),
        f.getName(SQL_TRANSLATOR_NAME),
        f.getType().getPythonTypeStr(),
        f.getFriendlyName()
        ))
    except KeyError, e:
      warn(str(f), RuntimeWarning)
      raise KeyError(e)
  for thisEnd in classMetaInfo.getAssociationEnds().values():
    try:
      otherEnd = thisEnd.getOppositeEnd()

      init.append(u"  import %s" % (otherEnd.getType().getName(TRANSLATOR_NAME)))
      init.append(u"  self.associations[\"%s\"] = DBAssociation(self, %s, %s, %s)" %(
        otherEnd.getName(SQL_TRANSLATOR_NAME),
        otherEnd.getType().getName(TRANSLATOR_NAME),
        otherEnd.hasForeignKey(),
        otherEnd.getMultiplicity()
        ))
        
#      classToCreateName = otherEnd.getType().getName(TRANSLATOR_NAME)
#
#      # we don't need to import the class if it's this class
#      if classToCreateName != className:
#        init.append(u"  import %s" % (classToCreateName))
#        classToCreateName = classToCreateName + "." + classToCreateName
#
#      init.append(u"  self.associations[\"%s\"] = ForeignKey(\"%s\", \"%s\", \"%s\", \"%s\", %s, self, %s)" %(
#        #end.getClassToCreateName(SQL_TRANSLATOR_NAME),
#        otherEnd.getName(SQL_TRANSLATOR_NAME), #thisEnd.getUUID(),
#        thisEnd.getAttributeName(SQL_TRANSLATOR_NAME),
#        thisEnd.getType().getName(SQL_TRANSLATOR_NAME),
#        otherEnd.getType().getName(SQL_TRANSLATOR_NAME),
#        otherEnd.getAttributeName(SQL_TRANSLATOR_NAME),
#        otherEnd.getMultiplicity(),
#        classToCreateName
#        ))
    except KeyError, e:
      warn(str(thisEnd), RuntimeWarning)
      raise KeyError(e)

  init.append("  if self.db_session is not None:")
  init.append("    self.connect()")
  init.append("  if primary_key is not None:")
  init.append("    self.loadSelf(primary_key)")
  #init.append(u"  warn('finished init %s')" % (
  #                 classMetaInfo.getName(TRANSLATOR_NAME)))
  init.append(u"")
  
  return addIndentToStrings(indent, init)

def createUtilityAccessors(indent, classMetaInfo):
  """Create member functions for returning information
  not directly stored in the classes defining an association.
  """
  utilities = []

  # since we travel down the list of base classes for the key information
  # unless the user overrides, we should always provide the key methods
  # on the off chance that the user overrides the foreign key name.
  utilities.append(u"def getPrimaryKeyName(self):")
  utilities.append(u"  return '%s'" % (classMetaInfo.getPrimaryKeyName(SQL_TRANSLATOR_NAME)))
  #utilities.append(u"  return '%s'" % (classMetaInfo.getRootClass().getName(SQL_TRANSLATOR_NAME)+"_pk"))
  utilities.append(u"")
  utilities.append(u"def getForeignKeyName(self):")
  utilities.append(u"  return '%s'" % (classMetaInfo.getForeignKeyName(SQL_TRANSLATOR_NAME)))
  utilities.append(u"")
  utilities.append(u"def getClassName(self):")
  utilities.append(u"  return '%s'" % (classMetaInfo.getName(TRANSLATOR_NAME)))
  utilities.append(u"")
  utilities.append(u"def getTableName(self):")
  utilities.append(u"  return '%s'" % (classMetaInfo.getName(SQL_TRANSLATOR_NAME)))
  utilities.append(u"")

  # since the sequence is defined for the root class
  # we should ask only the root class to if there's a sequence
  # defined for us.
  if classMetaInfo.isRootClass():
    # FIXME: can there be an autosequence without a primary key?
    utilities.append(u"def isAutoSequence(self):")
    utilities.append(u"  return %d" % (classMetaInfo.isAutoSequence()))
    utilities.append(u"")

  return addIndentToStrings(indent, utilities)

def createAccessors(indent, attributes):
  # FIXME: accessors shouldn't allow modifying primary key.
  # FIXME: or at least doing so should load a different record
  accessors = []
  for attrib in attributes:
    description = createDocString(indent, attrib.getDescription())
    accessors.append(u"def %s(self):"%(attrib.getGetterName(TRANSLATOR_NAME)))
    if description is not None:
      accessors.extend(description)
    sqlName = attrib.getName(SQL_TRANSLATOR_NAME)
    accessors.append(u"  return self.fields[\"%s\"].value" % ( sqlName ))
    accessors.append(u"")
    accessors.append(u"def %s(self, value): " % (
                                     attrib.getSetterName(TRANSLATOR_NAME) ))
    if description is not None:
      accessors.extend(description)
    accessors.append(u"  self.fields[\"%s\"].setValue(value)" % ( sqlName ))
    accessors.append(u"")

  return addIndentToStrings(indent, accessors)

def createAssociations(indent, associationEnds):
  """Construct functions to construct objects our current table is linked to.
  """
  # FIXME: we should cache the object we created for update abilities.
  
  object_refs = []
  for thisEnd in associationEnds:
    otherEnd = thisEnd.getOppositeEnd()
    warn("assoc: (%s,%s)" % (thisEnd.getName(None), otherEnd.getName(None)),
         DebugWarning)

    
    # define getter
    object_refs.append(u"# t=%s, o=%s" % (thisEnd.getName(None),
                                          otherEnd.getName(None)))
    object_refs.append(u"def %s(self):" %(otherEnd.getGetterName(TRANSLATOR_NAME)))

    #sqlClassName = fkey.getClassToCreateName(SQL_TRANSLATOR_NAME)
    #uuid = thisEnd.getUUID()
    uuid = otherEnd.getName(SQL_TRANSLATOR_NAME)
    object_refs.append(u"  association = self.associations['%s']" % (uuid))
    object_refs.append(u"  return association.getObjects()")
    object_refs.append(u"")

    # define setter
    setterName = otherEnd.getSetterName(TRANSLATOR_NAME)
    object_refs.append(u"def %s(self, object):" % (setterName))
    object_refs.append(u"  association = self.associations['%s']" % (uuid))
    object_refs.append(u"  association.setObjects(object)")
    object_refs.append(u"")

    # define appender, only needed for many to one links
    if otherEnd.getMultiplicity() != fkeyTypes.OneToOne:
      appenderName = otherEnd.getAppenderName(TRANSLATOR_NAME)
      object_refs.append(u"def %s(self, object):" % (appenderName))
      object_refs.append(u"  association = self.associations['%s']" % (uuid))
      object_refs.append(u"  association.appendObjects(object)")
      object_refs.append(u"")

    # FIXME: should there be a remove?

  return addIndentToStrings(indent, object_refs)

#######################################
# Output Translater Interface

def writeClass(destination, classMetaInfo):
  """
  """
  className = classMetaInfo.getName(TRANSLATOR_NAME)
  warn("class %s assocs: %s" % (className,
                                str(classMetaInfo.getAssociationEnds().items())),
       DebugWarning)
  classAssociationEnds = classMetaInfo.getAssociationEnds().values()
  classAttributes =  classMetaInfo.getAttributes()
  classFilename = classMetaInfo.getFilename()

  # FIXME: the second element in this tuple needs to contain the package
  # FIXME: name
  packageName = classMetaInfo.getPackage()
  # FIXME: this isn't going to work until package support is more complete
  if 0 and packageName is not None:
    # FIXME: Need to ignore the default starting package. 
    packageName += '.'
  else:
    packageName = ""
    
  packageName += className
  packageInformation = (className, packageName)

  outputStream = getOutputStream(destination, className, ".py")

  body = []
  body.extend(createHeader(0, classMetaInfo))
  body.extend(createClassHeader(0, classMetaInfo))
  body.extend(createClassInit(2, classMetaInfo))
  body.extend(createUtilityAccessors(2, classMetaInfo))
  body.extend(createAccessors(2, classAttributes))
  body.extend(createAssociations(2, classAssociationEnds))

  bodyString = string.join(body, os.linesep) + os.linesep #add trailing newline
  outputStream.write(bodyString)
  outputStream.close()
  
  return packageInformation

class PackageTemplate(Template):
  def __init__(self, packageInformation):
    Template.__init__(self)
    self.packageInformation = packageInformation
    
  def import_modules(self):
    module_list = []
    for moduleName, modulePath in self.packageInformation:
      module_list += ["import %s" % (modulePath)]
    return string.join(module_list, os.linesep)

  def classes_list(self):
    module_list = ""
    
    for moduleName, packagePath in self.packageInformation:
      if type(packagePath) == types.ListType:
        modulePath = packagePath
      else:
        modulePath = [packagePath]
      modulePath.extend([moduleName])
      
      module_list += "('%s', %s), " % (moduleName, string.join(modulePath,'.'))
    return '['+module_list+']'

  def modules_list(self):
    """Return list of modules, useful for reloading when reinitializing
    """
    module_list = []
    for moduleName, modulePath in self.packageInformation:
      module_list += ["%s" % (moduleName)]
    return string.join(module_list, ", ")


def writeTemplateFile(package_macros, source_filename, destination_filename):
  # Get file handles
  source_file = open(source_filename)
  destination_file = open(destination_filename, "w")

  # start copying replacing any template information
  macro_re = re.compile("%%([A-Za-z0-9_]*)%%")
  for line in source_file.readlines():
    macro_match = macro_re.search(line)
    if macro_match is not None:
      macro = macro_match.group(1)
      replacement = package_macros.get(macro, None)
      if replacement is not None:
        line = re.sub("%%"+macro+"%%", replacement, line)
    destination_file.write(line)

  source_file.close()
  destination_file.close()

def writeInit(package_template, destination_pathname):
  init = ["import os"]
  init += ["import sys"]
  init += ["import types"]
  init += ["import psycopg as db_api"]
  init += ["from dbAPI import Functor"]
  init += ["from dbAPI import reloadModuleList"]
  init += ["from dbAPI import DBSessionImpl"]
  init += ["from dbAPI import TransactionManager"]
  init += [""]
  init += ["%(import_modules())s"]
  init += [""]
  init += ["moduleReload = Functor(reloadModuleList, (%(modules_list())s))"]
  init += [""]
  init += ["class DBSession(DBSessionImpl):"]
  init += ["  def __init__(self, dsn=None, database=None, user=None, password=None):"]
  init += ["    classes_to_load = %(classes_list())s"]
  init += [""]
  init += ["    DBSessionImpl.__init__(self, dsn, database, user, password)"]
  init += ["    self.loadClasses(classes_to_load)"]
  init += ["    self.connect()"]

  package_template.writeFile(init, destination_pathname)

def writePackage(destination, package_information):
  # write the package definition
  import pymerase.output.dbAPI
  module_pathname = pymerase.output.dbAPI.__path__[0]
  module_path = module_pathname

  warn("module_pathname: %s" % (module_pathname), DebugWarning)

  # parse package information
  package_template = PackageTemplate(package_information)

  writeInit(package_template, os.path.join(destination, "__init__.py"))

  files_to_copy = [('dbAPI.py', 'dbAPI.py'),
                   ('../../util/bool.py', 'bool.py'),
                   ('fkeyTypes.py', 'fkeyTypes.py')]

  # Get filenames
  for source_filename, destination_filename  in files_to_copy:
    source_pathname = os.path.join(module_path, source_filename)
    destination_pathname = os.path.join(destination, destination_filename)

    shutil.copy(source_pathname, destination_pathname)

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
