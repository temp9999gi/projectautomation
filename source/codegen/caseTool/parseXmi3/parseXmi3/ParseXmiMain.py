# -*- coding: utf-8 -*-
# start
import sys
import logging
from ModelInfo import *
from Constants import *
# ToDo: xmi파싱 부분을 공통화해라..
# utils.initLog('ParseXmiMain.log')
# utils.addConsoleLogging()
log = logging.getLogger('ParseXmiMain')

# CONS = Constants()
from smw.metamodel import UML14
from smw.metamodel import UML13
from smw.io import loadModel

aModelInfo = ModelInfo()
class ParseXmiMain:
	def loadModel(self, inFile):
		self.aModelInfo = aModelInfo.loadModel(inFile)
		
	def getModelInfo(self):
		return self.aModelInfo



