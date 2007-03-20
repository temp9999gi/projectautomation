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
# Last Modified: $Date: 2007/01/01 13:36:53 $
#

class Session:
		"""
		Allows web based interface to keep track of session status
		"""
		
		def __init__(self):
				self.DISPLAY_ON = 1
				self.DISPLAY_OFF = 0
				self.YES = 1
				self.NO = 0

				#Used for displaying error messages if user filled in a form incorrectly
				self.warnings = ""

				self.info = {}
				self.info['session'] = None
				self.info['user'] = None
				self.info['us_pk'] = None
				self.info['con_pk'] = None
				self.info['form'] = None
#--INSERT_SESSION_INFO--#

				self.menuStatus = {}
#--INSERT_MENU_STATUS--#

				#Current Stage of Web Based Session
				self.curStage = 'stage1'

				self.stageComplete = {}
#--INSERT_STAGE_COMPLETE--#

				self.tableStage = {}
#--INSERT_TABLE_STAGE--#










