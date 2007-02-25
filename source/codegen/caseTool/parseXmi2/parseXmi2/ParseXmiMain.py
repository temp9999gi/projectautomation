# -*- coding: utf-8 -*-
# start
import sys
from XmiSaxHandler import *
from xml.sax import make_parser, handler
import logging
import utils
import xmiCommonUtil as xmiUtil
from ModelInfo import *
from Constants import *
# ToDo: xmi파싱 부분을 공통화해라..
# utils.initLog('ParseXmiMain.log')
# utils.addConsoleLogging()
log = logging.getLogger('ParseXmiMain')

# CONS = Constants()

class ParseXmiMain:
	def getModelInfo(self, inFile):

		aModelInfo = ModelInfo()
		aModelInfo.setXMI(xmiUtil.getXMI(inFile))

		h = XmiSaxHandler(aModelInfo)
		parser = make_parser()
		parser.setContentHandler(h)
		parser.parse(inFile)

		aModelInfo.makeRelationOfAttribute(aModelInfo)
		aModelInfo.setClassAndOperation(aModelInfo)
		aModelInfo.makeRelationOfParameter(aModelInfo)

		xmiUtil.loadInitialValue(aModelInfo, inFile)


		return aModelInfo



