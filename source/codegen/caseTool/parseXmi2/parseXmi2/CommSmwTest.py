# -*- coding: utf-8 -*-
###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2002 by:																								 #
																											 #
###########################################################################
#
#			 Authors: kusung
# Last Modified: $Date: 2007/01/07 15:40:03 $
#
"""Attempts to load a model defined in an xmi file into pymerase.

Currently requires the novosoft uml reader, which implies the need for jython.
It was currently tested with 0.4.19 downloaded from the argo cvs.
"""
# import system packages
from __future__ import nested_scopes

from smw.metamodel import UML14
from smw.metamodel import UML13
from smw.io import loadModel

import sys
import logging
# import utils
import xmiCommonUtil as xmiUtil

def parseXMI_test(model):

	aAttributes = filter(lambda c: isinstance(c, UML13.Attribute), model.getAllParts())

	for attr in aAttributes:
		#UML:Expression body를 가지고 온다.
		print 'attr.initialValue.body', attr.initialValue.body
##		aClassAttribute = getAttributeByXmiId(attr.__XMIid__)
##		aInitialValue = getInitialValueByXmiId( attr.initialValue.__XMIid__)
##		aClassAttribute.setInitialValue(aInitialValue)

if __name__ == "__main__":
	from Constants import *
	CONS = Constants()
	inFile  = CONS.INPUT_DIR / 'Party.xmi'
	inFile = str(inFile)

	model = loadModel(inFile)
	parseXMI_test(model)