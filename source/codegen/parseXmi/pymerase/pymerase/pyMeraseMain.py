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
# Last Modified: $Date: 2007/01/01 13:36:52 $
#
# import system packages
from __future__ import nested_scopes

import glob
import imp
import os
import string
import sys
import types

# import pymerpase packages
from pymerase import output
from pymerase import input
from pymerase.util.bool import parseBoolValue
# import warning support
# note: pymerase.util.Warning adds to builtins
#import pymerase.util.Warnings
from pymerase.util.Warnings import DebugWarning
from pymerase.util.Warnings import InfoWarning
import pymerase.util.NameMangling
from pymerase.util.SortMetaInfo import computeDependencyGraph
import warnings
from warnings import warn
# this disables debug warnings by default
warnings.filterwarnings('ignore', category=DebugWarning, append=1)
warnings.filterwarnings('ignore', category=InfoWarning, append=1)

##################
#PYMERASE VERSION#
VERSION = "v0.2.1"
##################

# Override this to change which name mangling convention to use
# before executing the parse functionality.
# e.g.
#	 import pymerase
#	 import pymerase.util.NameMangler
#	 manglerClass = pymerase.util.NameMangler.nullMangler()
#	 pymerase.setNameMangler(manglerClass, outputTranslatorName)
#	 pymerase.parseInput(...)

class PymeraseConfig:
	"""Contains configuration information for the various translators

	pymeraseConfigVersion: in case we feel like pickling this as a config file.
	nameManglers: dictionary of classes to perform the variable name conversions
								for the various output translators
	defaultPackage: default package name to put things in.
	"""
	def __init__(self, defaultPackage=None):
		self.pymeraseConfigVersion=0
		self.nameManglers = {None: pymerase.util.NameMangling.CapWord(),
												 'CreateHTMLForm': pymerase.util.NameMangling.EnglishWord(),
												 'CreatePyTkWidgets': pymerase.util.NameMangling.EnglishWord(),
												 'CreateSQL': pymerase.util.NameMangling.underscore_word()}
		self.defaultPackage = defaultPackage

	def __setstate__(self, configState):
		self.pymeraseConfigVersion = configState['pymeraseConfigVersion']
		self.nameManglers					= configState['nameManglers']
		self.defaultPackage				= configState['defaultPackage']

	def __getstate__(self):
		configState = {}
		configState['pymeraseConfigVersion'] = self.pymeraseConfigVersion
		configState['nameManglers']					= self.nameManglers
		configState['defaultPackage']				= self.defaultPackage
		return configState

	def setDefaultPackage(self, defaultPackage):
		"""Set default package.

		Used by the generate API code to specify what package to place things in.
		"""
		self.defaultPackage = defaultPackage

	def getDefaultPackage(self):
		return self.defaultPackage

	def setNameMangler(self, nameMangler, translatorName=None):
		"""Provide a mangler that enforces a particular naming convention for
		class and variable names.

		translatorName specifies for which output module this name mangler
		applies to. (Mostly, other translators that produce code that
		are designed to interact with a different translator will also need
		to know. For example, the DBAPI module needs to know about the setting
		for the SQL module.)
		"""
		if not isinstance(nameMangler, pymerase.util.NameMangling.NameMangler):
			raise ValueError(
				"NameMangler must be a subclass of pymerase.util.NameMangling.NameMangler"
			)

		# set the current name mangler
		self.nameManglers[translatorName] = nameMangler


	def getNameMangler(self, translatorName=None):
		"""Returns the name mangler for a particular translator or
		the default if that translator has no setting.
		"""
		return self.nameManglers.get(translatorName, self.nameManglers[None])


class Pymerase:
	"""Information about the currently running translation instance

	inputPath: pathname for directory of input modules
	inputTranslatorName: name of the translator (located in inputPath)
	outputPath: pathname for directory of output modules
	outputTranslatorName: name or class of the output translator
												(located in outputPath)
	pymeraseConfig: pymerase config class (see PymeraseConfig)
	"""

	def __init__(self, inputTranslator=None, outputTranslator=None, defaultPackage=None):
		# module path information
		self.inputPath = input.__path__
		self.inputTranslatorName = None
		self.outputPath = output.__path__
		self.outputTranslatorName = None

		self.setInputTranslator(inputTranslator)
		self.setOutputTranslator(outputTranslator)

		self.pymeraseConfig = PymeraseConfig(defaultPackage)

	def __setstate__(self, configState):
		self.inputTranslatorName	 = configState['inputTranslatorName']
		self.setInputTranslator(self.inputTranslatorName)
		self.outputTranslatorName	= configState['outputTranslatorName']
		self.setOutputTranslator(self.outputTranslatorName)
		self.inputPath						 = configState['inputPath']
		self.outputPath						= configState['outputPath']
		self.pymeraseConfig = configState['pymeraseConfig']

	def __getstate__(self):
		configState['inputTranslatorName']	= self.inputTranslatorName
		configState['outputTranslatorName']	= self.outputTranslatorName
		configState['inputPath']						 = self.inputPath
		configState['outputPath']						= self.outputPath
		configState['pymeraseConfig'] = self.pymeraseConfig
		return configState

	###############################
	# manipulate pymeraseConfig object

	def getPymeraseConfig(self):
		"""Return pymeraseConfig object for this app instance
		"""
		return self.pymeraseConfig

	def setPymeraseConfig(self, value):
		"""Return pymeraseConfig object for this app instance
		"""
		if isinstance(value, PymeraseConfig):
			self.pymeraseConfig = value
		else:
			raise ValueError("requires object of type PymeraseConfig")

	def setNameMangler(self, nameMangler, translatorName=None):
		"""Calls PymeraseConfig.setNameMangler
		"""
		self.pymeraseConfig.setNameMangler(nameMangler, translatorName)

	def getNameMangler(self, translatorName=None):
		"""calls PymeraseConfig.getNameMangler
		"""
		return self.pymeraseConfig.getNameMangler(translatorName)

	def setDefaultPackage(self, defaultPackage):
		"""Calls PymeraseConfig.setDefaultPackage
		"""
		self.pymeraseConfig.setDefaultPackage(defaultPackage)

	###############################
	# Functions to deal with translators
	def __getTranslator(self, module_path, translatorName):
		"""Given a translator name, load the appropriate module
		"""
		if type(translatorName) == types.ModuleType:
			return translatorName
		elif type(translatorName) == types.StringType or type(translatorName) == types.UnicodeType:
			file, filename, modType = imp.find_module(translatorName, module_path)
			return imp.load_module(translatorName, file, filename, modType)
		elif type(translatorName) == types.NoneType:
			return None
		else:
			raise ValueError("type [%s] invalid for translator"%type(translatorName))


	def setInputTranslator(self, translator):
		"""Set what input translator to use either by name or by passing a module.
		"""
		self.inputTranslatorName = translator
		self.inputTranslator = self.__getTranslator(self.inputPath, translator)

	def setOutputTranslator(self, translator):
		"""Set the output translator either by name or by passing a module.
		"""
		self.outputTranslatorName = translator
		self.outputTranslator = self.__getTranslator(self.outputPath, translator)


	######################
	# Code that does the work
	##def computeRootClassNames(self, parsedInput):
	##	"""Given a list of parsed objects determine the root objects for each
	##	class.
	##	"""
	##	classDictionary = computeDependencyGraph(parsedInput)
	##
	##	for currentClassRef in classDictionary.values():
	##		# track down the tree
	##		rootClassRef = currentClassRef
	##		# FIXME: This will probably break when inheriting from classes
	##		# FIXME: that aren't defined within the hiearchy.
	##		while len(currentClassRef.parents) > 0:
	##			# assume the first class is the most important
	##			rootClassRef = rootClassRef.parents[0]
	##
	##		currentClass = currentClassRef.classMetaInfo
	##		rootClass = rootClassRef.classMetaInfo
	##		currentClass.setRootClassName(rootClass.getName(None))


	def read(self, source, inputTranslator, classesInModel):
		"""Given a translator and source of input, parse object definitions.
		"""
		if inputTranslator is None:
			inputTranslator = self.inputTranslator
		else:
			inputTranslator = self.__getTranslator(input.__path__, inputTranslator)

		if inputTranslator is None:
			raise ValueError("Please set an input translator object")

		parsedInput = inputTranslator.read(source, self.pymeraseConfig, classesInModel)
		##self.computeRootClassNames(parsedInput)
		return parsedInput

	def write(self, parsedInput, destination, outputTranslator):
		"""Given parsed object definitions write output defined by
		an output_translator.
		"""
		if outputTranslator is None:
			outputTranslator = self.outputTranslator
		else:
			outputTranslator = self.__getTranslator(output.__path__,outputTranslator)

		if outputTranslator is None:
			raise ValueError("Please set an output translator object")

		outputTranslator.write(destination, parsedInput)


def run(source, inputTranslatorName, destination, outputTranslatorName):
	"""Parse input, and write a single type of output.
	"""
	# given source_path "/path/to/file.ext" set defaultPacge to 'file'
	defaultPackage = os.path.splitext(os.path.split(destination)[1])[0]

	translator = Pymerase(inputTranslatorName,
												outputTranslatorName,
												defaultPackage)

	parsedInput = translator.read(source, None, {})
	translator.write(parsedInput, destination, None)


###############################
# Code to handle parsing command line arguments
# FIXME: Should be moved?
def getOutputTranslatorList():
	"""
	returns list of output translators availble
	"""
	transList = []
	path = os.path.join(output.__path__[0], '*.py')
	rawList = glob.glob(path)
	for x in rawList:
		temp = x.split(os.sep)
		transName = temp[len(temp) - 1][:-3]
		if transName != '__init__':
			transList.append(transName)

	return transList


def getOutputTranslatorString(indent = 5):
	"""
	returns a formatted string for use with --help command line
	"""
	outputList = getOutputTranslatorList()

	for x in range(0, len(outputList)):
		#indent outputList by five spaces
		outputList[x] = ' ' * indent + outputList[x]

	text = string.join(outputList, os.linesep)

	return text


def getInputTranslatorList():
	"""
	returns list of input translators availble
	"""
	transList = []
	path = os.path.join(input.__path__[0], '*.py')
	rawList = glob.glob(path)
	for x in rawList:
		temp = x.split(os.sep)
		transName = temp[len(temp) - 1][:-3]
		if transName != '__init__':
			transList.append(transName)

	return transList


def getInputTranslatorString(indent = 5):
	"""
	returns a formatted string for use with --help command line
	"""
	inputList = getInputTranslatorList()

	for x in range(0, len(inputList)):
		#indent inputList by five spaces
		inputList[x] = ' ' * indent + inputList[x]

	text = string.join(inputList, os.linesep)

	return text


def getInputTranslatorVerbose(indent = 4):
	inputText = ""
	inputList = getInputTranslatorList()
	for myInput in inputList:
		try:
			#FIXME: getInputTranslator function merged to pymerase.getTranslator
			myMod = getInputTranslator(myInput)
		except:
			continue
		if myMod.__doc__ is not None:
			inputText += " " * indent + myInput + \
									 "-" + myMod.__doc__ + os.linesep
		else:
			inputText += " " * indent + myInput + \
									 "-" + "No Documentation Available" + os.linesep
		del myMod

	return inputText


def getOutputTranslatorVerbose(indent = 4):
	outputText = ""
	outputList = getOutputTranslatorList()

	for myOutput in outputList:
		try:
			#FIXME: getOutputTranslator function merged to pymerase.getTranslator
			myMod = getOutputTranslator(myOutput)
		except:
			continue
		if myMod.__doc__ is not None:
			outputText += " " * indent + myOutput + \
										"-" + myMod.__doc__ + os.linesep
		else:
			outputText += " " * indent + myOutput + \
										"-" + "No Documentation Available" + os.linesep
		del myMod

	return outputText







if __name__ == '__main__':
	#Commnad line feature moved to pymerase/bin/pymerase
	pass

