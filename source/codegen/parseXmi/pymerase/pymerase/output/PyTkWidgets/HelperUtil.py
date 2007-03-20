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
#			 Authors: Brandon King
# Last Modified: $Date: 2007/01/01 13:36:52 $
#
import string
import re
#from pymerase.output.PyTkWidgets import ValidatingEntry

class HelperUtil:

	def __init__(self):
		self.rowCounter = 0
		self.colCounter = 0

	def setRowCounter(self, value):
		self.rowCounter = value

	def getRowCounter(self):
		counter = self.rowCounter
		self.rowCounter += 1
		return counter

	def resetRowCounter(self):
		self.rowCounter = 0


	def getPrimaryKeyLabel(self, name, value, isRequired=0):
		code = []
		
		code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s: %s\")" % \
								(label, label, value))
		code.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % (label, self.getRowCounter()))
		code.append("")
		code.append("%VAR_ELEMENT%")

		return string.join(code, '\n')


	def makeLabelEntry(self, name, labelText, isRequired=0):
		"""
		Creates the code for generating a Label & Entry pair and returns the code
		"""
		
		counter = self.getRowCounter()

		code = []
		if isRequired:
			labelText += "*"
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\", fg=\"red\")" %\
									(name, labelText))
		else:
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\")" % \
									(name, labelText))
		code.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % (name, counter))
		code.append("		self.%sEntry = Tkinter.Entry(self.parent)" % (name))
		code.append("		self.%sEntry.grid(row=%s, column=1, sticky=Tkinter.W)" % (name, counter))
		code.append("")
		code.append("%VAR_ELEMENT%")

		return string.join(code, '\n')

	def makeLabelIntegerEntry(self, name, labelText, isRequired=0):
		"""
		Creates the code for generating a Label & Entry pair and returns the code
		"""
		
		counter = self.getRowCounter()

		code = []
		if isRequired:
			labelText += "*"
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\", fg=\"red\")" % \
									(name, labelText))
		else:
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\")" % \
									(name, labelText))
		code.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % (name, counter))
		code.append("		self.%sEntry = ValidatingEntry.IntegerEntry(self.parent)" % (name))
		code.append("		self.%sEntry.grid(row=%s, column=1, sticky=Tkinter.W)" % (name, counter))
		code.append("")
		code.append("%VAR_ELEMENT%")

		return string.join(code, '\n')

	def makeLabelFloatEntry(self, name, labelText, isRequired=0):
		"""
		Creates the code for generating a Label & Entry pair and returns the code
		"""
		
		counter = self.getRowCounter()

		code = []
		if isRequired:
			labelText += "*"
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\", fg=\"red\")" % \
									(name, labelText))
		else:
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\")" % \
									(name, labelText))
		code.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % (name, counter))
		code.append("		self.%sEntry = ValidatingEntry.FloatEntry(self.parent)" % (name))
		code.append("		self.%sEntry.grid(row=%s, column=1, sticky=Tkinter.W)" % (name, counter))
		code.append("")
		code.append("%VAR_ELEMENT%")

		return string.join(code, '\n')

	def makeLabelMaxLengthEntry(self, name, labelText, max=None, isRequired=0):
		"""
		Creates the code for generating a Label & Entry pair and returns the code
		"""
		
		counter = self.getRowCounter()

		code = []
		if isRequired:
			labelText += "*"
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\", fg=\"red\")" % \
									(name, labelText))
		else:
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\")" % \
									(name, labelText))
		code.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % (name, counter))
		code.append("		self.%sEntry = ValidatingEntry.MaxLengthEntry(self.parent,"\
								"maxlength=%s)" % (name, max))
		if max is not None:
			if max >= 1 and max <= 20:
				code.append("		self.%sEntry['width'] = %s" % (name, max))
		code.append("		self.%sEntry.grid(row=%s, column=1, sticky=Tkinter.W)" % (name, counter))
		code.append("")
		code.append("%VAR_ELEMENT%")

		return string.join(code, '\n')



	def makeGetLabelEntry(self, name):

		code = []
		code.append("	def get%sEntry(self):" % (name))
		code.append("		return self.%sEntry.get()" % (name))
		code.append("")
		code.append("%GET_FUNCTION%")

		return string.join(code, '\n')

	def makeGetLabelIntegerEntry(self, name):

		code = []
		code.append("	def get%sEntry(self):" % (name))
		code.append("		data = self.%sEntry.get()" % (name))
		code.append("		if data == \"\":")
		code.append("			return None")
		code.append("		else:")
		code.append("			return int(data)") 
		code.append("")
		code.append("%GET_FUNCTION%")

		return string.join(code, '\n')

	def makeGetLabelFloatEntry(self, name):

		code = []
		code.append("	def get%sEntry(self):" % (name))
		code.append("		data = self.%sEntry.get()" % (name))
		code.append("		if data == \"\":")
		code.append("			return None")
		code.append("		else:")
		code.append("			return float(data)")
		code.append("")
		code.append("%GET_FUNCTION%")

		return string.join(code, '\n')

	def makeSetLabelEntry(self, name):

		code = []
		code.append("	def set%sEntry(self, text=None):" % (name))
		code.append("		self.%sEntry.delete(0, Tkinter.END)" % (name))
		code.append("		if text is not None:")
		code.append("			self.%sEntry.insert(0, str(text))" % (name))
		code.append("")
		code.append("%SET_FUNCTION%")

		return string.join(code, '\n')

	def makeSaveLabelEntry(self, name):
		code = []
		#FIXME: should uses getGetterName and getSetterName functions instead
		code.append("			if self.get%sEntry() is not None:" % (name))
		code.append("				obj.set%s(self.get%sEntry())" % (name,name))
		code.append("%SAVE_FUNCTION%")

		return string.join(code, '\n')

	def makeLoadLabelEntry(self, name):
		code = []
		#FIXME: should uses getGetterName and getSetterName functions instead
		code.append("		self.set%sEntry(obj.get%s())" % (name, name))
		code.append("%LOAD_FUNCTION%")

		return string.join(code, '\n')


	def makeLabelText(self, name, labelText, isRequired=0):
		"""
		Creates the code for generating a Label & Text pair and returns the code
		"""
		counter = self.getRowCounter()
		
		code = []
		if isRequired:
			labelText += "*"
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\", fg=\"red\")" % \
									(name, labelText))
		else:
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\")" % \
									(name, labelText))
		code.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % (name, counter))
		code.append("		self.%sText = Tkinter.Text(self.parent, width=40, height=5)" % (name))
		code.append("		self.%sText.grid(row=%s, column=1, sticky=Tkinter.W)" % (name, counter))
		code.append("")
		code.append("%VAR_ELEMENT%")

		return string.join(code, '\n')


	def makeGetLabelText(self, name):

		code = []
		code.append("	def get%sText(self):" % (name))
		code.append("		data = self.%sText.get(0.0, Tkinter.END)" % (name))
		code.append("		if data == \"\":")
		code.append("			return None")
		code.append("		else:")
		code.append("			return data")
		code.append("")
		code.append("%GET_FUNCTION%")

		return string.join(code, '\n')

	def makeSetLabelText(self, name):

		code = []
		code.append("	def set%sText(self, text=None):" % (name))
		code.append("		self.%sText.delete(0.0, Tkinter.END)" % (name))
		code.append("		if text is not None:")
		code.append("			self.%sText.insert(0.0, text)" % (name))
		code.append("")
		code.append("%SET_FUNCTION%")

		return string.join(code, '\n')
		
	def makeSaveLabelText(self, name):
		code = []
		#FIXME: should uses getGetterName and getSetterName functions instead
		code.append("			if self.get%sText() is not None:" % (name))
		code.append("				obj.set%s(self.get%sText())" % (name, name))
		code.append("%SAVE_FUNCTION%")

		return string.join(code, '\n')

	def makeLoadLabelText(self, name):
		code = []
		#FIXME: should uses getGetterName and getSetterName functions instead
		code.append("		self.set%sText(obj.get%s())" % (name, name))
		code.append("%LOAD_FUNCTION%")

		return string.join(code, '\n')

	def makeRadioBoolean(self, name, labelText, isRequired=0):
		"""
		Creates the code for generating a True/False Radiobutton pair and returns the code
		"""
		
		counter = self.getRowCounter()

		code = []
		code.append("		self.%sFrame = Tkinter.Frame(self.parent)" % (name))
		if isRequired:
			labelText += "*"
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\", fg=\"red\")" % \
									(name, labelText))
		else:
			code.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\")" % \
									(name, labelText))
		code.append("		self.%sBooleanVar = Tkinter.IntVar()" % (name))

		code.append("		self.%sRadioTrue = Tkinter.Radiobutton(self.%sFrame," \
								"text=\"True\", variable=self.%sBooleanVar, value=1)" % (name, name, name))
		
		code.append("		self.%sRadioFalse = Tkinter.Radiobutton(self.%sFrame," \
								"text=\"False\", variable=self.%sBooleanVar, value=0)" % (name, name, name))

		code.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % (name, counter))
		code.append("		self.%sRadioTrue.grid(row=0, column=0)" % (name))
		code.append("		self.%sRadioFalse.grid(row=0, column=1)" % (name))
		code.append("		self.%sFrame.grid(row=%s, column=1, sticky=Tkinter.W)" % (name, counter))
		code.append("")
		code.append("%VAR_ELEMENT%")

		return string.join(code, '\n')


	def makeGetRadioBoolean(self, name):

		code = []
		code.append("	def get%sRadioBoolean(self):" % (name))
		code.append("		return self.%sBooleanVar.get()" % (name))
		code.append("")
		code.append("%GET_FUNCTION%")

		return string.join(code, '\n')


	def makeSetRadioBoolean(self, name):

		code = []
		code.append("	def set%sRadioBoolean(self, num):" % (name))
		code.append("		self.%sBooleanVar.set(num)" % (name))
		code.append("")
		code.append("%SET_FUNCTION%")

		return string.join(code, '\n')

	def makeSaveRadioBoolean(self, name):
		code = []
		#FIXME: should uses getGetterName and getSetterName functions instead
		code.append("			obj.set%s(self.get%sRadioBoolean())" % (name, name))
		code.append("%SAVE_FUNCTION%")

		return string.join(code, '\n')


	def makeLoadRadioBoolean(self, name):
		code = []
		#FIXME: should uses getGetterName and getSetterName functions instead
		code.append("		self.set%sRadioBoolean(obj.get%s())" % (name, name))
		code.append("%LOAD_FUNCTION%")

		return string.join(code, '\n')


	def processFkVarElement(self, attrib, assoc, TRANSLATOR, code):

		attribName = attrib.getName(TRANSLATOR)

		counter = self.getRowCounter()

		newCode = []
		#Create Label Code
		newCode.append("		#%s Label" % (attribName))
		newCode.append("		self.%sLabel = Tkinter.Label(self.parent, text=\"%s:\")" % \
									 (attribName, assoc.getName(TRANSLATOR)))
		newCode.append("		self.%sLabel.grid(row=%s, column=0, sticky=Tkinter.E)" % \
									 (attribName, counter))
		newCode.append("")

		#Create OPTION_MENU Mode
		newCode.append("		#%s OPTION MODE" % (attribName))
		newCode.append("		if mode == modes.OPTION_MENU:")
		newCode.append("			self.%sVar = Tkinter.StringVar()" % \
									 (attribName))
		newCode.append("			self.%sOptionMenu = ExtendedOptionMenu(self.parent," % \
									 (attribName))
		newCode.append("																						 self.%sVar," % \
									 (attribName))
		newCode.append("																						 '<EMPTY>')")
		newCode.append("			self.%sOptionMenu.grid(row=%s, column=1, sticky=Tkinter.W)" % \
									 (attribName, counter))
		newCode.append("			self.%sOptionMenu['menu'].delete(0, Tkinter.END)" % \
									 (attribName))
		newCode.append("			self.%sOptionMenu['width'] = 20" % \
									 (attribName))

		#Create DEFAULT Mode
		newCode.append("")
		newCode.append("		#%s DEFAULT MODE" %(attribName))
		newCode.append("		else:")
		newCode.append("			self.%sEntry = ValidatingEntry.IntegerEntry(self.parent)" % \
									 (attribName))
		newCode.append("			self.%sEntry.grid(row=%s, column=1, sticky=Tkinter.W)" % \
									 (attribName, counter))
		newCode.append("")
		newCode.append("%VAR_ELEMENT%")

		newCode = string.join(newCode, "\n")

		return re.sub("%VAR_ELEMENT%", newCode, code)

	def makeGetOptionMenu(self, name):

		code = []

		code.append("	def get%sOptionMenu(self):" % (name))
		code.append("		return self.%sVar.get()" % (name))
		code.append("")
		code.append("%GET_FUNCTION%")

		return string.join(code, "\n")

	def makeSetOptionMenu(self, name):

		code = []

		code.append("	def set%sOptionMenu(self, list):" % (name))
		code.append("		self.%sOptionMenu.setMenuFromList(list)" % (name))
		code.append("")
		code.append("%SET_FUNCTION%")

		return string.join(code, '\n')
	

	def makeSelectOptionMenuItem(self, name):

		code = []

		code.append("	def select%sOptionMenuItem(self, name):" % \
								(name))
		code.append("		self.%sOptionMenu.selectItemByName(name)" % \
								(name))
		code.append("")
		code.append("%SET_FUNCTION%")

		return string.join(code, '\n')


	def makeAppendOptionMenu(self, name):

		code = []
		code.append("	def append%sOptionMenu(self, list):" % (name))
		code.append("		self.%sOptionMenu.appendListToMenu(list)" % (name))
		code.append("")
		code.append("%SET_FUNCTION%")

		return string.join(code, '\n')


	def makeOptionMenuDict(self, name, fClassName):

		code = []
		code.append("		if mode == modes.OPTION_MENU:")
		code.append("			self.%sOptionMenuDict = {}" % (name))
		code.append("			self.%sPkDict = {}" % (fClassName))
		code.append("			self.update%sOptionMenu()" % (name))
		code.append("")
		code.append("%OPTION_MENU_DICT%")

		return string.join(code, '\n')

	def makeUpdateOptionMenu(self, fClassName, attribName, getterName, pkGetter):
		#FIXME: Grabbing wrong end of Association
		code = []
		code.append("	def update%sOptionMenu(self):" % (attribName))
		code.append("		%sList = self.dbs.getAllObjects(self.dbs.%s)" % \
								(fClassName, fClassName))
		code.append("		%sNameList = []" % (fClassName))
		code.append("")
		code.append("		counter = 0")
		code.append("		for fObj in %sList:" % \
								(fClassName))
		code.append("			%sNameList.append(fObj.%s())" % \
								(fClassName, getterName))
		code.append("			self.%sOptionMenuDict[fObj.%s()] = counter" % \
								(attribName, getterName))
		code.append("			self.%sPkDict[fObj.%s()] = fObj.%s()" % \
								(fClassName, getterName, pkGetter))
		code.append("			counter += 1")
		code.append("")
		code.append("		self.set%sOptionMenu(%sNameList)" % \
								(attribName, fClassName))
		code.append("")
		code.append("%UPDATE_FUNCTIONS%")

		return string.join(code, '\n')

		
	def makeSaveFk(self, fClassName, attribName):

		code = []
		code.append("			if self.mode == modes.OPTION_MENU:")
		code.append("				fObjList = self.dbs.getObjects(self.dbs.%s," %\
								(fClassName))
		code.append("										 str(self.%sPkDict[self.get%sOptionMenu()]))" % \
								(fClassName, attribName))
		code.append("				if len(fObjList) == 1:")
		code.append("					obj.set%s(fObjList[0])" % (fClassName))
		code.append("				elif len(fObjList) > 1:")
		code.append("					print \"Many-to-one! Panic! Not implemented yet!\"")
		code.append("				else:")
		code.append("					pass")
		code.append("			else:")
		code.append("				if self.get%sEntry() is not None:" % (attribName))
		code.append("					obj.set%s(self.get%sEntry())" % (attribName, attribName))
		code.append("%SAVE_FUNCTION%")

		return string.join(code, '\n')


	def makeLoadFk(self, attribName, getterName, fClassName):

		code = []
		code.append("		if self.mode == modes.OPTION_MENU:")
		code.append("			fObjList = obj.get%s()" % (fClassName))
		code.append("			if len(fObjList) == 1:")
		code.append("				self.%sOptionMenu.selectItemByName(fObjList[0].%s())" % \
								(attribName, getterName))
		code.append("			elif len(fObjList) > 1:")
		code.append("				print \"Many-to-one linking, panic! It's not implemented yet!\"")
		code.append("				self.%sOptionMenu.selectItemByName(fObjList[0].%s())" % \
								(attribName, getterName))
		code.append("		else:")
		code.append("			self.set%sEntry(obj.get%s())" % (attribName, attribName))
		code.append("%LOAD_FUNCTION%")

		return string.join(code, '\n')
		
