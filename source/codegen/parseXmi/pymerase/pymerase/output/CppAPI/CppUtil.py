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
# Last Modified: $Date: 2007/01/01 13:36:52 $
#			Revision: $ Revision $
#
import string

class CppUtil:

	def __init__(self):
		pass

	def getClassConstructor(self, className):
		code = []
		code.append("%s::%s() { /*FIXME: How to initilize a c++ class? */ }" % (className, className))
		code.append("")
		code.append("%CLASS_DEF%")

		code = string.join(code, '\n')
		return code

	def getSetterFunction(self, className, setterName, attribName, attribType, varName):
		code = []
		code.append("void %s::%s(%s %s)" % (className, setterName, attribType, attribName))
		code.append("{")
		code.append("	this->%s = %s;" % (varName, attribName))
		code.append("}")
		code.append("")
		code.append("%CLASS_DEF%")

		code = string.join(code, '\n')
		return code

	def getGetterFunction(self, className, getterName, attribType, varName):
		code = []
		code.append("%s %s::%s()" % (attribType, className, getterName))
		code.append("{")
		code.append("	return this->%s;" % (varName))
		code.append("}")
		code.append("")
		code.append("%CLASS_DEF%")

		code = string.join(code, '\n')
		return code
