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
# Last Modified: $Date: 2007/01/02 09:14:59 $
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

#source='C:/_kldp/codegen/test/pymerase/pymerase-0.2.1/examples/linkDB/linkDB.xmi'
source='C:/_kldp/codegen/parseXmi/parseXmi/input/Party.xmi'
#loadModel(url,metamodel=None, toupdate = None):
model = loadModel(source)
 
print 'model: [',model,']'

print model.ownedElement

for xx in model.ownedElement:
	if isinstance(xx, UML13.Model):
	# 	print 'xx: [',xx,']'
		#print 'xx: [',dir(xx),']'
		
		print 'name: [',xx.name,']'		
		
classes = filter(lambda c: isinstance(c, UML13.Model), model.ownedElement)		

for xmiClass in classes:
	parsedClass = umlParser.parseXMIClass(classesInModel, xmiClass)
	if parsedClass is not None:
		classesInModel[parsedClass.getUUID()] = parsedClass

