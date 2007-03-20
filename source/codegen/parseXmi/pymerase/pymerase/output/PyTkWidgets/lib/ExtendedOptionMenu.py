###########################################################################
#																																				 #
# C O P Y R I G H T	 N O T I C E																				 #
#	Copyright (c) 2003 by:																								 #
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
# Last Modified: $Date: 2007/01/01 13:36:53 $
#

import Tkinter
import types

class ExtendedOptionMenu(Tkinter.OptionMenu):

	def __init__(self, master, variable, value, *values, **kwargs):

		args = [self, master, variable, value]
		args.extend(values)

		apply(Tkinter.OptionMenu.__init__, args, kwargs)

		self.myVar = variable
		self.__indexDict = {}
		self.__indexCounter = 0

	def __setIndexDict(self, list):

		self.__indexDict.clear()

		self.__indexCounter = 0

		if type(list) is types.ListType or \
			 type(list) is types.TupleType:
			for item in list:
				self.__indexDict[item] = self.__indexCounter
				self.__indexCounter += 1
		elif type(list) is types.StringType:
			self.__indexDict[list] = self.__indexCounter

	def selectItemByName(self, name):

		if self.__indexDict.has_key(name):
			self['menu'].invoke(self.__indexDict[name])

	#def getIndexDict(self):
	#	return self.__indexDict

	def setMenuFromList(self, list):
		"""
		Given a list or string, deletes old list and replaces with new list.
		"""

		#Delete old list
		self['menu'].delete(0, Tkinter.END)

		#Replace with new list
		self.appendListToMenu(list)

		#Create dictionary of indexes for loading by name
		self.__setIndexDict(list)
		
		#Select first item by default
		self['menu'].invoke(0)


	def appendListToMenu(self, list):
		#Replace with new list
		if type(list) is types.ListType or \
			 type(list) is types.TupleType:
			for item in list:
				self['menu'].add_command(label=item,
																 command=Tkinter._setit(self.myVar, item))
				self.__indexDict[item] = self.__indexCounter
				self.__indexCounter += 1

		#Well, if the user wants to pass a string
		elif type(list) is types.StringType:
			self['menu'].add_command(label=list,
															 command=Tkinter._setit(self.myVar, list))
